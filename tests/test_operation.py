from src.math_operations import add, sub

def test_add():
    assert add(2,3) == 5

def test_sub():
    assert sub(5,3) == 2
    assert sub(13,6) == 7  