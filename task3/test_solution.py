"""Tests for lesson presence interval processing."""

import pytest

from task3.solution import appearance


@pytest.mark.parametrize(
    ("intervals", "expected"),
    [
        (
            {
                "lesson": [1594663200, 1594666800],
                "pupil": [
                    1594663340,
                    1594663389,
                    1594663390,
                    1594663395,
                    1594663396,
                    1594666472,
                ],
                "tutor": [
                    1594663290,
                    1594663430,
                    1594663443,
                    1594666473,
                ],
            },
            3117,
        ),
        (
            {
                "lesson": [1594702800, 1594706400],
                "pupil": [
                    1594702789,
                    1594704500,
                    1594702807,
                    1594704542,
                    1594704512,
                    1594704513,
                    1594704564,
                    1594705150,
                    1594704581,
                    1594704582,
                    1594704734,
                    1594705009,
                    1594705095,
                    1594705096,
                    1594705106,
                    1594706480,
                    1594705158,
                    1594705773,
                    1594705849,
                    1594706480,
                    1594706500,
                    1594706875,
                    1594706502,
                    1594706503,
                    1594706524,
                    1594706524,
                    1594706579,
                    1594706641,
                ],
                "tutor": [
                    1594700035,
                    1594700364,
                    1594702749,
                    1594705148,
                    1594705149,
                    1594706463,
                ],
            },
            3577,
        ),
        (
            {
                "lesson": [1594692000, 1594695600],
                "pupil": [1594692033, 1594696347],
                "tutor": [
                    1594692017,
                    1594692066,
                    1594692068,
                    1594696341,
                ],
            },
            3565,
        ),
    ],
)
def test_original_cases(intervals, expected):
    """Match the expected results from the original task."""
    assert appearance(intervals) == expected


def test_full_overlap():
    """Count the complete shared interval."""
    intervals = {
        "lesson": [0, 200],
        "pupil": [100, 150],
        "tutor": [100, 150],
    }

    assert appearance(intervals) == 50


def test_no_overlap():
    """Return zero when presence intervals do not overlap."""
    intervals = {
        "lesson": [0, 2000],
        "pupil": [0, 1000],
        "tutor": [1000, 2000],
    }

    assert appearance(intervals) == 0


def test_clips_intervals_to_lesson():
    """Ignore presence time outside the lesson boundaries."""
    intervals = {
        "lesson": [100, 200],
        "pupil": [50, 250],
        "tutor": [0, 300],
    }

    assert appearance(intervals) == 100


def test_merges_overlapping_intervals():
    """Avoid double-counting overlapping presence intervals."""
    intervals = {
        "lesson": [0, 100],
        "pupil": [10, 50, 20, 70],
        "tutor": [30, 60],
    }

    assert appearance(intervals) == 30


def test_handles_unsorted_intervals():
    """Handle presence intervals supplied out of chronological order."""
    intervals = {
        "lesson": [0, 100],
        "pupil": [60, 90, 10, 40],
        "tutor": [20, 80],
    }

    assert appearance(intervals) == 40


def test_empty_presence():
    """Return zero when one participant has no presence intervals."""
    intervals = {
        "lesson": [0, 100],
        "pupil": [],
        "tutor": [20, 80],
    }

    assert appearance(intervals) == 0
