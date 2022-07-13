import pytest
from ..bookkeeping import show_document_info
from unittest.mock import patch

@patch('input')
def sum( a = input(),b = input()):
    return a+b



class TestFunctions:
    def setup(self) -> None:
        pass
    def teardown(self) -> None:
        pass
    def test_show_document_info(self):
       assert sum(3,4) == 7