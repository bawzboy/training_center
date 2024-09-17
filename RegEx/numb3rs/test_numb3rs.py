from numb3rs import validate

def test_3_octets():
    assert validate("123.123.123") == False

def test_5_octets():
    assert validate("123.123.123.123.123") == False
    