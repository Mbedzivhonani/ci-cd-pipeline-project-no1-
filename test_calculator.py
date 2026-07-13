from calculator import import add

def test_addition():
    # This checks if 2 + 3 equals 5
    assert add(2, 3) == 5

def test_negative_addition():
    # This checks if -1 + 1 equals 0
    assert add(-1, 1) == 0
