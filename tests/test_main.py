import pytest
from .. import program


class TestProgram:
    def test_adding_numbers_works(self):
        assert program.main(1, 1) == 2
        assert program.main(2, 1) == 3
        assert program.main(3, 3) == 6

    def test_returns_0_if_there_is_error(self):
        assert program.main(1, '1') == 0