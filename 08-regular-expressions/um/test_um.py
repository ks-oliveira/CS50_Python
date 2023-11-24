import um

def test_words():
    assert um.count("um") == 1
    assert um.count("UM") == 1
    assert um.count("yummi") == 0
    assert um.count("ALBUM") == 0

def test_phrase():
    assert um.count("Um, thanks for the album.") == 1
    assert um.count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2
    assert um.count("This is so yummi") == 0

def test_expression():
    assert um.count("um?") == 1
    assert um.count("Hum!?") == 0
    assert um.count("Um, thanks, um...") == 2
