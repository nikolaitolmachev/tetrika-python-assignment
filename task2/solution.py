"""Collect and aggregate animal entries from Russian Wikipedia."""

import csv
from collections.abc import Iterable, Iterator
from pathlib import Path

import requests


API_URL = "https://ru.wikipedia.org/w/api.php"
CATEGORY = "Категория:Животные_по_алфавиту"
RUSSIAN_ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
REQUEST_TIMEOUT = 10
OUTPUT_FILE = Path(__file__).with_name("beasts.csv")

USER_AGENT = (
    "tetrika-python-assignment/1.0 "
    "(https://github.com/nikolaitolmachev/tetrika-python-assignment)"
)


def iter_category_titles() -> Iterator[str]:
    """Yield all article titles from the Wikipedia category."""
    params = {
        "action": "query",
        "list": "categorymembers",
        "cmtitle": CATEGORY,
        "cmnamespace": 0,
        "cmlimit": "max",
        "format": "json",
        "formatversion": 2,
    }

    while True:
        response = requests.get(
            API_URL,
            params=params.copy(),
            headers={"User-Agent": USER_AGENT},
            timeout=REQUEST_TIMEOUT,
        )
        response.raise_for_status()

        data = response.json()

        for member in data["query"]["categorymembers"]:
            yield member["title"]

        continuation = data.get("continue")
        if continuation is None:
            break

        params["cmcontinue"] = continuation["cmcontinue"]


def count_by_initial(titles: Iterable[str]) -> dict[str, int]:
    """Count titles by their first Russian letter."""
    counts = dict.fromkeys(RUSSIAN_ALPHABET, 0)

    for title in titles:
        if not title:
            continue

        initial = title[0].upper()

        if initial in counts:
            counts[initial] += 1

    return counts


def write_csv(counts: dict[str, int], path: Path = OUTPUT_FILE) -> None:
    """Write letter counts to a CSV file."""
    with path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(counts.items())


def main() -> None:
    counts = count_by_initial(iter_category_titles())
    write_csv(counts)


if __name__ == "__main__":
    main()
