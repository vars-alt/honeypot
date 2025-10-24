from socket import socket, AF_INET, SOCK_STREAM
import threading
import datetime

def handle_client(conn, addr):
    with open('honeypot_log.csv', 'a') as f:
        f.write(f"{datetime.datetime.now()},{addr[0]},{addr[1]}\n")
    conn.send(b"SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.3\r\n")
    conn.close()

def start_honeypot(port):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('0.0.0.0', port))
    s.listen(5)
    print(f"Honeypot listening on port {port}")
    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    for port in [22, 80]:
        threading.Thread(target=start_honeypot, args=(port,)).start()
