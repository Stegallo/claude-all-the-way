from python_project.operations import add, mul


def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(-4, -6) == -10


def test_mul():
    assert mul(2, 3) == 6
    assert mul(0, 5) == 0
    assert mul(-1, 1) == -1
    assert mul(-4, -6) == 24
