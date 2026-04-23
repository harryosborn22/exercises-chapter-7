"""Define some verified subclasses of sets."""

import numbers


class UniquenessError(KeyError):
    """Define an exception to raise when an item is not unique."""

    pass


class VerifiedSet(set):
    """Define a subclass of set that is verified according to conditions."""

    def __init__(self, value):
        self._verify(value)
        super().__init__(value)

    def _verify(self, value):
        raise NotImplementedError

    def add(self, value):
        """Verify the entries and then call the add method."""
        self._verify(value)
        super().add(value)

    def update(self, value):
        """Verify the entries and then call the update method."""
        self._verify(value)
        super().update(value)

    def symmetric_difference_update(self, value):
        """Verify the entries and then call the symmetric_difference_update method."""  # noqa E501
        self._verify(value)
        super().symmetric_difference_update(value)

    def union(self, value):
        """Verify the entries and then call the union method."""
        self._verify(value)
        return IntSet(super().union(value))

    def intersection(self, value):
        """Verify the entries and then call the intersection method."""
        self._verify(value)
        return IntSet(super().intersection(value))

    def difference(self, value):
        """Verify the entries and then call the difference method."""
        self._verify(value)
        return IntSet(super().difference(value))

    def symmetric_difference(self, value):
        """Verify the entries and then call the symmetric_difference method."""
        self._verify(value)
        return IntSet(super().symmetric_difference(value))

    def copy(self):
        """Call the copy method."""
        return IntSet(super().copy())


class IntSet(VerifiedSet):
    """Define a verified set with the condition that only numbers may be added."""  # noqa D205

    def _verify(self, value):
        iterable = (isinstance(value, set) or isinstance(value, tuple)
                    or isinstance(value, list))
        if not isinstance(value, numbers.Integral) and not iterable:
            raise TypeError("IntSet expected an integer,"
                            f"got a {type(value)}.")
        if iterable:
            for x in value:
                self._verify(x)


class UniqueSet(VerifiedSet):
    """Define a verified set with the condition that every entry must be unique."""  # noqa D205

    def _verify(self, value):
        iterable = (isinstance(value, set) or isinstance(value, tuple)
                    or isinstance(value, list))
        for x in self:
            if x == value:
                raise UniquenessError
        if iterable:
            for y in value:
                self._verify(y)
