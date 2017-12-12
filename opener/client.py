from sys import argv, stdin
import socket


def copy(f, port_number):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
      sock.connect(('127.0.0.1', port_number))
      while True:
        buf = f.read(4096)
        if not buf:
          break
        sock.send(buf)


def run(files, socket_path):
  for f in files:
    copy(f, socket_path)
