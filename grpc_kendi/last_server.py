import last_dance_pb2
import last_dance_pb2_grpc
import grpc

import time
from concurrent import futures

class son_servis():
    def toplama(self,request,context):
        return last_dance_pb2.cevap_toplam(toplam = (request.sayi_1 + request.sayi_2))
    def birlestirme(self,request,context):
        return last_dance_pb2.cevap_isim(isim = f"{request.isim_1} {request.isim_2}")
    
def servis():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    last_dance_pb2_grpc.add_son_servisServicer_to_server(son_servis(),server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    servis()