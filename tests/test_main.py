from src.main import get_message, add

def test_hello_world():
    assert get_message() == "Hello World"

def test_basic_addition():
    assert add(2, 3) == 5
