from unittest.mock import patch

from python_project.main import main


def test_main(capsys):
    with patch("python_project.main.random.randint", side_effect=[3, 7]):
        main()
    captured = capsys.readouterr()
    assert captured.out == "3 + 7 = 10\n3 * 7 = 21\n"
