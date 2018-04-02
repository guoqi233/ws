# coding:utf-8
from socketIO_client import SocketIO, BaseNamespace
import sys
from threading import Thread

HOST = 'http://192.168.10.165'
PORT = 80


class TestNamespace(BaseNamespace):
    def on_reconnect(self):
        super(TestNamespace, self).on_reconnect()
        print "reconnect"

    def on_error(self, data):
        super(TestNamespace, self).on_error(data)
        print 'error'


class ListenThread(Thread):
    def __init__(self, namespace,  path, *args, **kwargs):
        super(ListenThread, self).__init__(*args, **kwargs)
        self.sock = SocketIO(HOST, PORT)
        self.path = path
        self.namespace = namespace

    def run(self):
        sys.stdout.write("\r{}...\n".format(self.name))
        sys.stdout.flush()
        self.sock.define(self.namespace, self.path)


def main():
    p = ListenThread(namespace=TestNamespace, path='/test', name='listen')
    p.start()
    p.join()

if __name__ == '__main__':
    main()
