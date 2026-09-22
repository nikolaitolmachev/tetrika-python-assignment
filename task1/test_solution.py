"""Tests for the strict runtime type-checking decorator."""

from typing import Any

import pytest

from task1.solution import strict


def test_accepts_correct_positional_arguments():
    """Accept arguments with matching positional types."""

    @strict
    def func(a: int, b: str, c: float):
        return f"{a}, {b}, {c}"

    assert func(10, "test", 3.14) == "10, test, 3.14"


def test_accepts_correct_keyword_arguments():
    """Accept arguments with matching keyword types."""

    @strict
    def func(a: int, b: str):
        return f"{a}, {b}"

    assert func(b="test", a=10) == "10, test"


def test_rejects_incorrect_type():
    """Reject an argument whose type does not match its annotation."""

    @strict
    def func(a: int, b: str, c: float):
        return f"{a}, {b}, {c}"

    invalid_value: Any = 2

    with pytest.raises(TypeError):
        func(1, invalid_value, 3.14)


def test_rejects_bool_for_int():
    """Treat bool and int as distinct argument types."""

    @strict
    def func(value: int):
        return value

    invalid_value: Any = True

    with pytest.raises(TypeError):
        func(invalid_value)


def test_rejects_int_for_bool():
    """Treat int and bool as distinct argument types."""

    @strict
    def func(value: bool):
        return value

    invalid_value: Any = 1

    with pytest.raises(TypeError):
        func(invalid_value)


def test_preserves_function_metadata():
    """Preserve metadata of the decorated function."""

    @strict
    def example(value: int):
        """Example function."""
        return value

    assert example.__name__ == "example"
    assert example.__doc__ == "Example function."
