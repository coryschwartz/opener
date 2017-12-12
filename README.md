this is a client and server program.

The server listens on a unix domain socket.
When it receives a connection, it copies from the socket into a temp file,
and then opens it.

The client connects to the unix socket, and copies files into the socket.


The problem it solves is file viewing on remote servers.

Forward the unix domain socket with ssh -R and you can 'opener' video and image files easily. 

It also works if you use a mail client like mutt if you put opener as the mailcap.
