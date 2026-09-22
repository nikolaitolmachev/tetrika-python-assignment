"""Runtime type validation using function annotations."""

from functools import wraps
from inspect import signature


def strict(func):
    """Validate function arguments against their annotated types."""
    func_signature = signature(func)

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound_arguments = func_signature.bind(*args, **kwargs)

        for name, value in bound_arguments.arguments.items():
            expected_type = func_signature.parameters[name].annotation

            if type(value) is not expected_type:
                raise TypeError(
                    f'Argument "{name}" must be of type {expected_type.__name__}, got {type(value).__name__}'
                )

        return func(*args, **kwargs)

    return wrapper
