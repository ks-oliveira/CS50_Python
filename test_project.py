import project

def test_insert():
    table = [['ID','Status','Item'],['1','To Do','first item'],['2','To Do','Second item']]
    assert project.insert_item(table, 'Last item') == [['ID','Status','Item'],['1','To Do','first item'],['2','To Do','Second item'],['3','To Do','Last item']]

def test_delete():
    table = [['ID','Status','Item'],['1','To Do','first item'],['2','To Do','Second item']]
    assert project.delete_item(table, '1') == [['ID','Status','Item'],['1','To Do','Second item']]

def test_update():
    table = [['ID','Status','Item'],['1','To Do','first item'],['2','To Do','Second item']]
    assert project.update_item(table, 'U', 2, 'Last item') == [['ID','Status','Item'],['1','To Do','first item'],['2','To Do','Last item']]
    assert project.update_item(table, 'M', 1, 'Doing') == [['ID','Status','Item'],['1','Doing','first item'],['2','To Do','Last item']]
