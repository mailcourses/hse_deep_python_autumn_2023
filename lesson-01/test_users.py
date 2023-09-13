import unittest
from unittest import mock

from user import User


class TestUsers(unittest.TestCase):
    def test_greetings(self):
        user = User("Steve", 42)

        self.assertEqual("Steve", user.name)
        self.assertEqual("Hello, Steve!", user.greetings())

    def test_greetings_empty_name(self):
        user = User("", 42)

        self.assertEqual("", user.name)
        self.assertEqual("Hello, !", user.greetings())

    def test_birthday(self):
        user = User("Steve", 42)

        self.assertEqual(42, user.age)
        self.assertEqual(43, user.birthday())
        self.assertEqual(43, user.age)

    def test_get_friends_no_part(self):
        with mock.patch("user.fetch_vk_api") as mock_fetch:
            mock_fetch.return_value = ["f1", "f2"]

            user = User("Steve", 42)

            friends = user.get_friends()
            self.assertEqual(["f1", "f2"], friends)

            expected_call = [
                mock.call("/friends", "Steve", None)
            ]
            self.assertEqual(
                expected_call, mock_fetch.mock_calls
            )

    def test_get_friends_with_part(self):
        with mock.patch("user.fetch_vk_api") as mock_fetch:
            mock_fetch.return_value = ["f1", "f2"]

            user = User("Steve", 42)

            friends = user.get_friends(name_part="f")
            self.assertEqual(["f1", "f2"], friends)

            friends = user.get_friends(name_part="2")
            self.assertEqual(["f2"], friends)

            expected_call = [
                mock.call("/friends", "Steve", "f"),
                mock.call("/friends", "Steve", "2"),
            ]
            self.assertEqual(
                expected_call, mock_fetch.mock_calls
            )

    def test_get_friends_throw_error(self):
        with mock.patch("user.fetch_vk_api") as mock_fetch:
            # mock_fetch.side_effect = lambda *a: ["f1", "f2"]
            mock_fetch.side_effect = Exception("WRONG!")

            user = User("Steve", 42)

            with self.assertRaises(Exception) as err:
                user.get_friends()

            self.assertEqual("WRONG!", str(err.exception))
            self.assertIsInstance(err.exception, Exception)

            expected_call = [
                mock.call("/friends", "Steve", None)
            ]
            self.assertEqual(
                expected_call, mock_fetch.mock_calls
            )

    def test_get_friends_several_calls(self):
        with mock.patch("user.fetch_vk_api") as mock_fetch:
            mock_fetch.side_effect = [["f1"], ["f2", "f3"]]

            user = User("Steve", 42)

            friends = user.get_friends(name_part="f")
            self.assertEqual(["f1"], friends)

            friends = user.get_friends()
            self.assertEqual(["f2", "f3"], friends)

            expected_call = [
                mock.call("/friends", "Steve", "f"),
                mock.call("/friends", "Steve", None),
            ]
            self.assertEqual(
                expected_call, mock_fetch.mock_calls
            )

            # friends = user.get_friends(name_part="f")
            # self.assertEqual(["f1"], friends)
