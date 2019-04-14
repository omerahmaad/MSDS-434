from myrepolib import repomod


def test_func():
    result = repomod.myfunc()
    assert result == 9
    
def test_addition():
    result = repomod.addition(2,2)
    assert result = 4
