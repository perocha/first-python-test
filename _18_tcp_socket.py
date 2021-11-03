'''
Use tcp socket library
'''
import socket
import urllib.request

def main():
    ''' Main function'''
    print ("\n******** Using socket library ********\n")

    with socket.socket (socket.AF_INET, socket.SOCK_STREAM) as mysocket:
        mysocket.connect (('data.pr4e.org', 80))
        cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
        mysocket.send (cmd)

        while True:
            data = mysocket.recv (512)
            if len (data) < 1:
                break
            print (data.decode(), end='')

        print ("\n******** Using urllib.request library ********\n")

        with urllib.request.urlopen('http://data.pr4e.org/romeo.txt') as fhand:
            for line in fhand:
                print(line.decode().strip())

main()
