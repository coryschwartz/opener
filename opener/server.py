from socketserver import UnixStreamServer,  StreamRequestHandler
from subprocess import call
from sys import argv
from threading import Thread
from tempfile import NamedTemporaryFile
from time import sleep


class CopyOpener(StreamRequestHandler):
  def handle(self):
    with NamedTemporaryFile(delete=False) as f:
      while True:
        buf = self.rfile.read(4096)
        if not buf:
          break
        f.write(buf)
      call(['xdg-open', f.name])


def run(socket_file):
  with UnixStreamServer(socket_file, CopyOpener) as server:
    server.serve_forever()
