from unittest.mock import patch

from python_project.main import add, mul, main


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


def test_main(capsys):
    with patch("python_project.main.random.randint", side_effect=[3, 7]):
        main()
    captured = capsys.readouterr()
    assert captured.out == "3 + 7 = 10\n3 * 7 = 21\n"
