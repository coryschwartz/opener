from sys import argv, stdin
import socket

class SocketConnection(Exception):
  pass

def copy(f, socket_path):
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
      try:
        sock.connect(socket_path)
      except:
        raise SocketConnection
      while True:
        buf = f.read(4096)
        if not buf:
          break
        sock.send(buf)


def run(files, socket_path):
  for f in files:
    copy(f, socket_path)
