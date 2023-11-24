import bank

def main():
    test_hello()
    test_h()
    test_others()


def test_hello():
    assert bank.value("hello") == 0
    assert bank.value("Hello") == 0
    assert bank.value("HELLO") == 0

def test_h():
    assert bank.value("hi") == 20
    assert bank.value("How are you") == 20
    assert bank.value("H") == 20
    assert bank.value("h") == 20

def test_others():
    assert bank.value("Whats your name?") == 100
    assert bank.value("Just saying hi") == 100


if __name__ == "__main__":
    main()