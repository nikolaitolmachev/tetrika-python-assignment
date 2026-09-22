"""Calculate overlapping presence intervals during a lesson."""

Interval = tuple[int, int]


def normalize_intervals(
    timestamps: list[int],
    lesson_start: int,
    lesson_end: int,
) -> list[Interval]:
    """Clip intervals to the lesson boundaries and merge overlaps."""
    intervals = []

    for index in range(0, len(timestamps), 2):
        start = max(timestamps[index], lesson_start)
        end = min(timestamps[index + 1], lesson_end)

        if start < end:
            intervals.append((start, end))

    if not intervals:
        return []

    intervals.sort()
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]

        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged


def calculate_overlap(
    pupil_intervals: list[Interval],
    tutor_intervals: list[Interval],
) -> int:
    """Return the total overlap between two interval sequences."""
    total = 0
    pupil_index = 0
    tutor_index = 0

    while (
        pupil_index < len(pupil_intervals)
        and tutor_index < len(tutor_intervals)
    ):
        pupil_start, pupil_end = pupil_intervals[pupil_index]
        tutor_start, tutor_end = tutor_intervals[tutor_index]

        overlap_start = max(pupil_start, tutor_start)
        overlap_end = min(pupil_end, tutor_end)

        if overlap_start < overlap_end:
            total += overlap_end - overlap_start

        if pupil_end < tutor_end:
            pupil_index += 1
        else:
            tutor_index += 1

    return total


def appearance(intervals: dict[str, list[int]]) -> int:
    """Return the shared presence time of pupil and tutor during the lesson."""
    lesson_start, lesson_end = intervals["lesson"]

    pupil_intervals = normalize_intervals(
        intervals["pupil"],
        lesson_start,
        lesson_end,
    )
    tutor_intervals = normalize_intervals(
        intervals["tutor"],
        lesson_start,
        lesson_end,
    )

    return calculate_overlap(pupil_intervals, tutor_intervals)
