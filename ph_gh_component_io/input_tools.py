# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

"""Utility functions for cleaning and handling user-inputs"""


try:
    from typing import Any, List, Optional, TypeVar

    T = TypeVar("T")
except ImportError:
    pass  # Python 3

import re

try:
    from scriptcontext import sticky  # type: ignore
except ImportError:
    pass  # Not in Rhino Grasshopper


def input_to_int(_input_value, _default=None):
    # type: (Any, Any) -> int | None
    """For 'selection' type inputs, clean and convert input to int.

    ie: if the Grasshopper input allows:
        "1-A First Type"
        "2-A Second Type"

    will strip the string part and return just the integer value, or raise SelectionInputError.
    """

    if not _input_value:
        return _default

    # "\d" is a special character in regular expressions that matches any digit from 0 to 9.
    # "+" is a quantifier that specifies that the preceding pattern (in this case, \d) should match one or more times.
    # So the regular expression "\d+" will match one or more consecutive digits in a string.
    result = re.search(r"\d+", str(_input_value))
    try:
        if not result:
            raise ValueError
        return int(result.group(0))
    except ValueError:
        msg = (
            'Input Error: Cannot use input "{}" [{}].\n'
            "Please check the allowable input options.".format(
                _input_value, type(_input_value)
            )
        )
        raise Exception(msg)
    except AttributeError as e:
        # If no 'group', ie: no int part supplied in the string
        msg = 'Error trying to find the integer input part of input: "{}", type: {}'.format(
            _input_value, type(_input_value)
        )
        raise Exception(msg)


def clean_tree_get(_tree, _i, _default=None):
    try:
        return _tree.Branch(_i)
    except:
        try:
            return _tree.Branch(0)
        except:
            return _default


def clean_get(_list, _i, _default=None):
    # type: (List[T], int, Optional[T]) -> Optional[T]
    """Get list item cleanly based on index pos. If IndexError, will try getting _list[0] instead.

    This is useful for gh-components with multiple list inputs which are sometimes
    the same length, and sometimes not the same length.

    Arguments:
    ---------
        * _list: Any iterable to get the item from.
        * _i: The index position to try and get
        * _default: The optional default value to use if _list[0] fails.

    Returns:
    --------
        * Any
    """
    try:
        return _list[_i]
    except IndexError:
        try:
            return _list[0]
        except IndexError:
            return _default


def cleaner_get(_list, _i, _default):
    # type: (List[T], int, T) -> T
    """Get list item cleanly based on index pos. If IndexError, will try getting _list[0] instead.

    This function *requires* a default values to be supplied, and therefor will never return None (unless
    the default value is None). This is more type-safe than the 'clean_get' function.

    This is useful for gh-components with multiple list inputs which are sometimes
    the same length, and sometimes not the same length.

    Arguments:
    ---------
        * _list: Any iterable to get the item from.
        * _i: The index position to try and get
        * _default: A required default value to use if _list[0] fails.

    Returns:
    --------
        * Any
    """
    try:
        return _list[_i]
    except IndexError:
        try:
            return _list[0]
        except IndexError:
            return _default


def memoize(func):
    """Simple caching decorator using function arguments as key.

    Uses the Grasshopper 'sticky' dict to store values.

    https://book.pythontips.com/en/latest/function_caching.html

    Usage:
    >>> @memoize
    >>> def fibonacci(n):
    >>>     if n < 2: return n
    >>>    return fibonacci(n - 1) + fibonacci(n - 2)
    >>>
    >>> fibonacci(25)
    """

    def wrapper(*args, **kwargs):
        try:
            return sticky[args]
        except KeyError:
            rv = func(*args, **kwargs)
            sticky[args] = rv
            return rv

    return wrapper
