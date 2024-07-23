from twttr import shorten

def test_upper():
    assert shorten("AEIOU") == ""

def test_lower():
    assert shorten("aeiou") == ""
