from mock.mock import Mock

from app.utils import create_log_file


def test_create_log_file(mocker):
    cwd_mock = Mock()
    mocker.patch("app.utils.os.getcwd", cwd_mock)
    cwd_mock.return_value = "C://user//sender"

    makedirs_mock = Mock()
    mocker.patch("app.utils.os.makedirs", return_value=makedirs_mock)

    datetime_mock = Mock()
    mocker.patch("app.utils.datetime", datetime_mock)
    datetime_mock.date.today.return_value = "2025-01-20"

    actual_value = create_log_file()
    expected_value = "C://user//sender/logs/2025-01-20.log"

    assert actual_value == expected_value
