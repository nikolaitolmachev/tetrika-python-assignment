"""Tests for Wikipedia category aggregation."""

import csv
from unittest.mock import Mock, patch

import pytest
import requests

from task2.solution import (
    RUSSIAN_ALPHABET,
    count_by_initial,
    iter_category_titles,
    write_csv,
)


@patch("task2.solution.requests.get")
def test_iter_category_titles_handles_pagination(mock_get):
    """Collect titles across multiple API pages."""
    first_response = Mock()
    first_response.json.return_value = {
        "continue": {
            "cmcontinue": "next-page",
            "continue": "-||",
        },
        "query": {
            "categorymembers": [
                {"title": "Аист"},
                {"title": "Акула"},
            ]
        },
    }

    second_response = Mock()
    second_response.json.return_value = {
        "batchcomplete": True,
        "query": {
            "categorymembers": [
                {"title": "Бобр"},
            ]
        },
    }

    mock_get.side_effect = [first_response, second_response]

    titles = list(iter_category_titles())

    assert titles == ["Аист", "Акула", "Бобр"]
    assert mock_get.call_count == 2

    first_params = mock_get.call_args_list[0].kwargs["params"]
    second_params = mock_get.call_args_list[1].kwargs["params"]

    assert "cmcontinue" not in first_params
    assert second_params["cmcontinue"] == "next-page"

    first_response.raise_for_status.assert_called_once()
    second_response.raise_for_status.assert_called_once()


def test_count_by_initial():
    """Count Russian initials and ignore unsupported characters."""
    titles = [
        "Аист",
        "Акула",
        "Бобр",
        "Ёж",
        "ёжик",
        "Aardvark",
        "123",
        "",
    ]

    counts = count_by_initial(titles)

    assert list(counts) == list(RUSSIAN_ALPHABET)
    assert counts["А"] == 2
    assert counts["Б"] == 1
    assert counts["Ё"] == 2
    assert sum(counts.values()) == 5


def test_write_csv(tmp_path):
    """Write aggregated counts in CSV format."""
    output_file = tmp_path / "beasts.csv"

    write_csv({"А": 2, "Б": 1}, output_file)

    with output_file.open(encoding="utf-8-sig", newline="") as file:
        rows = list(csv.reader(file))

    assert rows == [["А", "2"], ["Б", "1"]]


@patch("task2.solution.requests.get")
def test_http_error_is_propagated(mock_get):
    """Propagate HTTP errors returned by Wikipedia."""
    mock_get.return_value.raise_for_status.side_effect = requests.HTTPError

    with pytest.raises(requests.HTTPError):
        list(iter_category_titles())
