from bank import value

def test_upper_hello():
    assert value("HELLO") == 0

def test_lower_hello():
    assert value("hello") == 0

def test_upper_h():
    assert value("H") == 20

def test_lower_h():
    assert value("h") == 20

def test_empty():
    assert value("") == 100
