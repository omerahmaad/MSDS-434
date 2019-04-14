from myrepolib import repomod


def test_func():
    result = repomod.myfunc()
    result2 = repomod.sum_two(2,2)
    assert result == 1
    assert result2 == 4

