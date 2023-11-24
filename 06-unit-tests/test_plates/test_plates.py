import plates

def test_valid():
    assert plates.is_valid("CS50") == True

def test_starts_with_0():
    assert plates.is_valid("CS05") == False

def test_number_in_middle():
    assert plates.is_valid("CS50P") == False

def test_puctuation():
    assert plates.is_valid("PI3.14") == False

def test_one_letter():
    assert plates.is_valid("H") == False

def test_more_than_six_digits():
    assert plates.is_valid("OUTATIME") == False

def test_two_first_not_letter():
    assert plates.is_valid("1CS5") == False
    assert plates.is_valid("C123") == False
    assert plates.is_valid("1234") == False
