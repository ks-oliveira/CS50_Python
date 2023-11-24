import seasons

def test_date():
    assert seasons.check_birthday("1999-01-01") == (1999, 1, 1)
    assert seasons.check_birthday("1999-1-1") == None
    assert seasons.check_birthday("Jan 1, 1999") == None
