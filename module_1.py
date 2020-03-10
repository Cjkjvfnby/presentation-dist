"""
Module for documentation examples.
"""

class Bar:
    """
    Class with a constructor.
    """

    def __init__(self):
        """Makes a Bar"""
        pass


class FooBar(Bar):
    """
    Class inherited from Bar.
    """


def foo1(n):
    """
    Without type annotation
    """
    return n


def foo2(n: int) -> int:
    """
    With type annotation.
    It is like :py:func:`~foo1` but uses :py:class:`int`

    """
    return n


def foo3(n):
    """
    Special docstring syntax.

    It is like :py:func:`~foo1` but uses :py:class:`float`

    :param float n: input argument
    :return: first argument
    :rtype: float
    """
    return n
