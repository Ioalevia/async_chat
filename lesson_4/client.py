import sys
import json
import socket
import time


def presence(user):
    output = {
        "action": "presence",
        "time": time.time(),
        "user": {"account_name": user}
    }
    return output


def send_message(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    send_msg = presence("user")
    json_send_msg = json.dumps(send_msg)
    encoded_msg = json_send_msg.encode("utf-8")
    s.send(encoded_msg)
    return s


def get_message(socketsession):
    encoded_resp = socketsession.recv(1024)
    if isinstance(encoded_resp, bytes):
        json_resp = encoded_resp.decode("utf-8")
        resp = json.loads(json_resp)
        if isinstance(resp, dict):
            return resp
        raise ValueError
    raise ValueError


def get_answer(answer):
    if "response" in answer:
        if answer["response"] == 200:
            print(f"200 : OK")
            return '200 : OK'
        return f'400 : {answer["error"]}'
    raise ValueError


def main():
    try:
        server_host = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_host = "127.0.0.1"
        server_port = 7777
    except ValueError:
        print('wrong port')
        sys.exit(1)
    S = send_message(server_host, server_port)
    get_answer(get_message(S))

if __name__ == '__main__':
    main()
