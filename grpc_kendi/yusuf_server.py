import grpc_pb2_grpc
import grpc_pb2
import grpc

from concurrent import futures
import time

class Yusuf():
    def toplama(self,request,context):
        return grpc_pb2.cevap_toplam(toplam = request.birinci + request.ikinci)
    def selamla(self,request,context):
        return grpc_pb2.cevap_selamlama(mesaj = f"Selamunaleyküm {request.isim}")
    
def servis():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_pb2_grpc.add_YusufServicer_to_server(Yusuf(),server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    servis()




































