from test import Transmit
from test.ttypes import *
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
import socket


class TransmitHandler:
    def __init__(self):
        self.log = {}

    def put(self, msg):
        print(msg.seqId,msg.content)


if __name__=="__main__":
    handler = TransmitHandler()
    processor = Transmit.Processor(handler)
    transport = TSocket.TServerSocket('127.0.0.1', 8013)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory() 
    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print("Starting python server...")
    server.serve()
