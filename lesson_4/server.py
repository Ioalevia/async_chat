import socket
import sys
import json


def get_msg(tr_socket):
    encoded_resp = tr_socket.recv(1024)
    if isinstance(encoded_resp, bytes):
        json_resp = encoded_resp.decode("utf-8")
        resp = json.loads(json_resp)
        if isinstance(resp, dict):
            print(resp)
            return resp
        raise ValueError
    raise ValueError


def make_answer(answerclient: dict):
    if "action" in answerclient and answerclient["action"] == "presence" and "time" in answerclient \
            and "user" in answerclient and answerclient["user"]["account_name"] == 'user':
        print("response: 200")
        return {"response": 200}
    print("response: 400")
    return {
        "response": 400,
        "error": 'Bad Request'
    }


def send_msg(tr_socket, msgtoclient):
    js_msg = json.dumps(msgtoclient)
    encoded_msg = js_msg.encode("utf-8")
    tr_socket.send(encoded_msg)


def main():
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = 7777
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        print('no port')
        sys.exit(1)
    except ValueError:
        print('wrong port')
        sys.exit(1)
    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = ''
    except IndexError:
        print('no adress')
        sys.exit(1)
    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((listen_address, listen_port))
    transport.listen(5)
    while True:
        tr_socket, client_address = transport.accept()
        message_from_cient = get_msg(tr_socket)
        response = make_answer(message_from_cient)
        send_msg(tr_socket, response)
        print(f"Client: {client_address}")
        tr_socket.close()


if __name__ == '__main__':
    main()