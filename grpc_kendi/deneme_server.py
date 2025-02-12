import deneme_pb2
import deneme_pb2_grpc
import grpc

import time
from concurrent import futures

class servis():
    def bolme(self,request,context):
        bolme= (int)(request.sayi_1 / request.sayi_2)
        kalmis = (request.sayi_1 % request.sayi_2)
        return deneme_pb2.cevap_bolme(bolum = bolme , kalan = kalmis)
    def selamla(self,request,context):
        return deneme_pb2.cevap_selamla(mesaj = f"Selam {request.isim}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    deneme_pb2_grpc.add_servisServicer_to_server(servis(),server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()