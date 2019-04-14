from myrepolib import repomod


def test_func():
    result = repomod.myfunc()
    result_2 = repomod.addition(2,2)
    assert result == 9
    assert result_2 == 4
