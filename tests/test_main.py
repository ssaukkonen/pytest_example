import pytest
from unittest.mock import MagicMock
from .. import program


class TestProgram:
    def test_main_function_runs(self):
        program.main()

    def test_main_calls_add(self, monkeypatch):
        mock_add = MagicMock()
        monkeypatch.setattr(program, "add", mock_add)
        program.main()
        mock_add.assert_called()

    def test_adding_numbers_works(self):
        assert program.add(1, 1) == 2
        assert program.add(2, 1) == 3
        assert program.add(3, 3) == 6
    
    def test_add_returns_0_if_there_is_error(self):
        assert program.add(1, '1') == 0