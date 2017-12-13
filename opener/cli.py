import argparse
import signal
import sys

from opener import client, server

parser = argparse.ArgumentParser(description='Opens files copied through a socket')
parser.add_argument('--port', help='Server Port number', type=int, default='10987')
parser.add_argument('--server', help='start in server mode instead', action='store_true')
parser.add_argument('infile', nargs='*', type=argparse.FileType('rb'))

def cleanup(signum, frame):
  sys.exit()

def main():
  parsed = parser.parse_args()
  if parsed.server:
    signal.signal(signal.SIGTERM, cleanup)
    signal.signal(signal.SIGHUP, cleanup)
    signal.signal(signal.SIGINT, cleanup)
    server.run(parsed.port)
  else:
    if isinstance(parsed.infile, list):
      files = parsed.infile
    else:
      files = [parsed.infile]
    if not files:
      files = [sys.stdin.buffer]
    try:
      client.run(files, parsed.port)
    except ConnectionRefusedError:
      print('Cannot connect to socket. Server running?', file=sys.stderr)
      sys.exit(1)


if __name__ == '__main__':
  main()
