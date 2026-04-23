"""Define a class SymmetricGroup with group operations and validation."""

from example_code import groups
import numpy as np


class SymmetricGroup(groups.Group):
    """Define a class SymmetricGroup with group operations and validation."""

    symbol = "S"

    def _validate(self, value):
        """Ensure that value is an allowed element value in this group."""
        try:
            if list(sorted(value)) != [i for i in range(self.n)]:
                raise ValueError("Element value must be a sequence of integers"
                                 f" in the range [0, {self.n})")
        except AttributeError:
            raise ValueError("Element value must be a sequence of integers"
                             f" in the range [0, {self.n})")

    def operation(self, a, b):
        """Perform the group operaation on two elements in this group."""
        return np.array([a[i] for i in b])
