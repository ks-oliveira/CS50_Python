from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar2 = Jar(4)
    assert jar2.capacity == 4
    with pytest.raises(ValueError):
        jar3 = Jar(-4)



def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(4)
    assert jar.size == 4
    jar.deposit(3)
    assert jar.size == 7
    with pytest.raises(ValueError):
        jar.deposit(6)


def test_withdraw():
    jar = Jar()
    jar.deposit(8)
    jar.withdraw(4)
    assert jar.size == 4
    jar.withdraw(3)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(3)
