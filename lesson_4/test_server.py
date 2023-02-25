import server, client
import unittest


class TestServer(unittest.TestCase):

    def test_get_msg(self):
        host = "127.0.0.1"
        port = 7777
        msg = client.send_message(host, port)
        try:
            self.assertEqual(server.get_msg(msg), {'response': 200})
        except:
            self.assertEqual(server.get_msg(msg), {'response': 400})

    def test_make_answer(self):
        a = {"action": "presence", "time": 1, "user": {"account_name": "user"}}
        try:
            self.assertEqual(server.make_answer(a), {'response': 200})
        except:
            self.assertEqual(server.make_answer(a), {'response': 400, 'error': 'Bad Request'})

    def send_msg(self):
        host = "127.0.0.1"
        port = 7777
        msg = client.send_message(host, port)
        answer = {'response': 200}
        self.assertEqual(server.send_msg(msg, answer), msg)


if __name__ == '__main__':
    unittest.main()