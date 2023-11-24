import numb3rs

def test_valid():
    assert numb3rs.validate("127.0.0.1") == True
    assert numb3rs.validate("255.255.255.255") == True

def test_invalid():
    assert numb3rs.validate("1") == False
    assert numb3rs.validate("1.2") == False
    assert numb3rs.validate("1.2.3") == False
    assert numb3rs.validate("1.512.512.512") == False
    assert numb3rs.validate("1.2.512.512") == False
    assert numb3rs.validate("1.2.3.1000") == False
    assert numb3rs.validate("4000.3.2.1") == False
    assert numb3rs.validate("4000.3000.2.1") == False
    assert numb3rs.validate("4000.3000.2000.1") == False
    assert numb3rs.validate("4000.3000.2000.1000") == False
    assert numb3rs.validate("a.b.c.d") == False
    assert numb3rs.validate("cat") == False