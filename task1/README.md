# Task 1 — Strict Type Checking

## Task

Implement a `@strict` decorator that validates function arguments against their type annotations at runtime.

The decorated functions use only the following argument types:

* `bool`
* `int`
* `float`
* `str`

If an argument does not exactly match its annotated type, the decorator must raise `TypeError`.

## Approach

The solution uses `inspect.signature()` to bind positional and keyword arguments to their corresponding function parameters.

Each bound argument is validated against its annotation using exact type comparison:

```python
type(value) is expected_type
```

This ensures strict runtime type matching for all supported argument types.

`functools.wraps()` preserves the original function's metadata.

## Testing

The test suite covers:

* valid positional arguments;
* valid keyword arguments;
* invalid argument types;
* strict distinction between `bool` and `int`;
* preservation of function metadata.
