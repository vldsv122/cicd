import pytest
import task

@pytest.fixture
def get_keywoard():
    return "sova"

def check_file_lines():
    content = "123\n456\n789\n"
    assert task.get_file_lines(content) == ["123", "456", "789"]

def test_filter_lines_by_keywoard():
    lines = ["123", "456", "789"]
    keyword = "6"
    assert task.filter_lines_by_keywoard(lines, keyword) == ["456"]

def test_filter_lines_by_keywoard_empty():
    lines = ["123", "456", "789"]
    keyword = "sova"
    assert task.filter_lines_by_keywoard(lines, keyword) == []

