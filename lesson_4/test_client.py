import client
import unittest


class TestClient(unittest.TestCase):
    def test_presence(self, user="user"):
        self.user = user
        test_client = client.presence(self.user)
        test_client["time"] = 1
        self.assertEqual(test_client, {"action": "presence", "time": 1, "user": {"account_name": self.user}})

    def test_send_message(self, host="127.0.0.1", port=7777):
        self.host = host
        self.port = port
        a = client.send_message(self.host, self.port)
        self.assertEqual(a,"<socket.socket fd=344, family=2, type=1, proto=0, laddr=('127.0.0.1', 60099), raddr=('127.0.0.1', 7777)>", "test ok")

    def test_get_message(self, host="127.0.0.1", port=7777):
        self.host = host
        self.port = port
        s = client.get_message(client.send_message(self.host, self.port))
        try:
            self.assertEqual(s, {'response': 200})
        except:
            self.assertEqual(s, {'response': 400})

    def test_get_answer(self, host="127.0.0.1", port=7777):
        self.host = host
        self.port = port
        s = client.get_message(client.send_message(self.host, self.port))
        try:
            self.assertEqual(client.get_answer(s), "200 : OK")
        except:
            self.assertEqual(client.get_answer(s), "400 : Bad Request")

if __name__ == '__main__':
    unittest.main()
