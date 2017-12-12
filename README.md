this is a client and server program for copying and opening files over a socket

The server listens on a TCP socket.
When it receives a connection, it copies from the socket into a temp file,
and then opens it.

The client connects to the unix socket, and copies files into the socket.


The problem it solves is file viewing on remote servers.

Forward the unix domain socket with ssh -R and you can 'opener' video and image files easily. 

It also works if you use a mail client like mutt if you put opener as the mailcap.


Example usage:

Running the server:
```bash
opener --server
```

Forwarding the socket to a remote server:
```bash
ssh -R 127.0.0.1:10987:127.0.0.1:10987 remote_machine
```

On the remote machine, using the provided client or any socket client works.
```bash
opener [file1, file2, filen...]
opener <some_unweildy_binary_file.pdf

nc 127.0.0.1 10987 <video_file.mp4
```
