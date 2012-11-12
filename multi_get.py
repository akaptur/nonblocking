import select
import socket

HOST = '127.0.0.1'
PORT = 1060


def make_listen_sock():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(5) #  listen for connections, up to 5 in backlog
    print "Listening on %d" % PORT
    return sock



if __name__ == '__main__':
    listen_sock = make_listen_sock()
    games = {}
    print listen_sock.fileno()
    sockets = {listen_sock.fileno(): listen_sock}


    while True:
        r_list, w_list, _ = select.select(sockets, sockets, '')
        # print "r:", r_list
        # print "w:", w_list
        for sock_num in r_list:
            if sock_num is listen_sock.fileno():
                game_sock, sockname = listen_sock.accept() # will block until first connection made
                game_sock.setblocking(False)
                sockets[game_sock.fileno()] = game_sock
            
        for sock_num in w_list:
            sock = sockets[sock_num]
            sock.sendall("Acknowledged")
            sock.close()
            del sockets[sock_num]  # remove from dict
            
