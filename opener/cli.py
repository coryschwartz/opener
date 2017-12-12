import argparse
import signal
import sys
import os

from opener import client, server

parser = argparse.ArgumentParser(description='Open files through a unix socket)')
parser.add_argument('--socket', help='location of the unix socket', default='/tmp/opener.sock')
parser.add_argument('--server', help='start in server mode instead', action='store_true')
parser.add_argument('infile', nargs='*', type=argparse.FileType('rb'))

def cleanup(socket_file):
  def inner(signum, frame):
    os.remove(socket_file)
    sys.exit()
  return inner

def main():
  parsed = parser.parse_args()
  if parsed.server:
    signal.signal(signal.SIGTERM, cleanup(parsed.socket))
    signal.signal(signal.SIGHUP, cleanup(parsed.socket))
    signal.signal(signal.SIGINT, cleanup(parsed.socket))
    server.run(parsed.socket)
  else:
    if isinstance(parsed.infile, list):
      files = parsed.infile
    else:
      files = [parsed]
    if not files:
      files = [sys.stdin.buffer]
    try:
      client.run(files, parsed.socket)
    except client.SocketConnection:
      print('Cannot connect to socket. Server running?', file=sys.stderr)
      sys.exit(1)


if __name__ == '__main__':
  main()
