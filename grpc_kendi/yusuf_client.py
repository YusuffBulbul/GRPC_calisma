import grpc_pb2
import grpc_pb2_grpc
import grpc

def calis():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = grpc_pb2_grpc.YusufStub(channel)
        cevap = stub.toplama(grpc_pb2.istek_sayi(birinci=10,ikinci=20))
        print(cevap.toplam)

        selam = stub.selamla(grpc_pb2.istek_isim(isim = "Yusuf"))
        print(selam.mesaj)


if __name__== "__main__":
    calis()






































