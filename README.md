Minimalist nonblocking sockets.

Technical features to note:
- A listening sock is a "read" socket and will be returned in select.select.  I use this feature to check an accept() call every time the loop hits the listening socket.

- Multiple sockets can all reside on the same port (here, 1060).  The listening socket spawns off other sockets on the same port.  The listening socket can only create new sockets - it cannot send or receive data.  Its nature is permanently altered once the call to listen() is made.  

- The call to listen(5) allows up to five connections to wait in backlog.  This is *not* a limit on the number of new sockets the listening socket can spawn.

Useful resources:
http://docs.python.org/dev/howto/sockets.html

docs: 
http://docs.python.org/2/library/select.html
http://docs.python.org/2/library/socket.html 