# Task 3 — Lesson Presence Overlap

## Task

Calculate the total time, in seconds, during which both the pupil and the tutor were present in the lesson.

Presence data is provided as timestamp pairs:

* `lesson` — lesson start and end;
* `pupil` — pupil presence intervals;
* `tutor` — tutor presence intervals.

Only overlapping presence within the lesson boundaries should be counted.

## Approach

The solution first normalizes the pupil and tutor intervals:

1. clip each interval to the lesson boundaries;
2. discard empty intervals;
3. sort intervals chronologically;
4. merge overlapping intervals.

The two normalized interval sequences are then processed with a two-pointer algorithm to calculate their total overlap.

This ensures overlapping intervals are counted once and allows the input intervals to be provided in any order.

## Complexity

Let `P` and `T` be the numbers of pupil and tutor intervals.

The overall time complexity is:

```text
O(P log P + T log T)
```

## Testing

The test suite covers:

* all original task cases;
* complete overlap;
* no overlap;
* intervals outside lesson boundaries;
* overlapping intervals within one participant's data;
* unsorted intervals;
* empty presence data.
