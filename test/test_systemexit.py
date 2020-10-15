import pytest
from psdemoutils import foo


def test_for_exit():
    with pytest.raises(SystemExit):
        foo()
