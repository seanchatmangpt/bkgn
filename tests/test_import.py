"""Test bkgn."""

import bkgn


def test_import() -> None:
    """Test that the app can be imported."""
    assert isinstance(bkgn.__name__, str)
