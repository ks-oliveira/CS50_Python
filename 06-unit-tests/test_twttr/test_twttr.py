import twttr

def main():
    test_twttr()
    test_number()
    test_punctuation()

def test_twttr():
    assert twttr.shorten("twitter") == "twttr"
    assert twttr.shorten("TEXT") == "TXT"
    assert twttr.shorten("LaTeX") == "LTX"

def test_number():
    assert twttr.shorten("123") == "123"

def test_punctuation():
    assert twttr.shorten(",.?") == ",.?"


if __name__ == "__main__":
    main()