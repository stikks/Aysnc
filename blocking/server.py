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

    if len(args) != 1:
        parsed.error('Provide exactly one poetry file.')

    poetry_file = args[0]

    if not os.path.exists(args[0]):
        parsed.error('No such file: %s' % poetry_file)

    return options, poetry_file


def serve(listener, filename):
    while True:
        connection, address = listener.accept()

        print('Client {} seeking to connect'.format(address))

        with open(filename) as _file:
            data = _file.read()
            try:
                connection.sendall(data)
            except socket.error as err:
                connection.close()
                print("Socket error: {}".format(err))
                return


def connect(host, port):
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(3)

    print('Listening on port - {}'.format(port))

    return sock


def main():

    options, filepath = parse_args()
    sock = connect(options.host, options.port)

    serve(sock, filepath)

if __name__ == '__main__':
    main()