#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, num):
        """Override == opeartor with != behavior."""
        return self.real != num

    def __ne__(self, num):
        """Override != operator with == behavior."""
        return self.real == num
