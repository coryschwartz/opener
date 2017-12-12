from socketserver import TCPServer,  StreamRequestHandler
from tempfile import NamedTemporaryFile
import webbrowser


class CopyOpener(StreamRequestHandler):
  def handle(self):
    with NamedTemporaryFile(delete=False) as f:
      while True:
        buf = self.rfile.read(4096)
        if not buf:
          break
        f.write(buf)
    webbrowser.open_new_tab('file://' + f.name)


def run(port_number):
  with TCPServer(('127.0.0.1', port_number), CopyOpener) as server:
    server.serve_forever()
