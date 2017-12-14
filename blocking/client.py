import socket
import optparse
import os


def parse_args():
    usage = """
    parse raw input arguments
    """
    parsed = optparse.OptionParser(usage)

    parsed.add_option('--port', type=int, help="The port to listen on. Default to a random available port.")
    parsed.add_option('--host', default='localhost', help="The interface to listen on. Default is localhost.")

    options, args = parsed.parse_args()

    if not options.port or not isinstance(options.port, int):
        parsed.error("Provide valid port --port [PORT]")

    return options


def retrieve(host, port):
    sock = socket.socket()
    sock.connect((host, port))

    print('Listening on port - {}'.format(port))

    while True:

        data = sock.recv(1024)

        if not data:
            sock.close()

        print data


def main():

    options = parse_args()

    retrieve(options.host, options.port)

if __name__ == '__main__':
    main()