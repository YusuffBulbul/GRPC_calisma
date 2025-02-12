import deneme_pb2
import deneme_pb2_grpc
import grpc

def calis():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = deneme_pb2_grpc.servisStub(channel)

        cevap = stub.bolme(deneme_pb2.istek_sayilar(sayi_1 = 10, sayi_2 = 4))
        print(cevap)
        cevap = stub.selamla(deneme_pb2.istek_isim(isim="Yusuf"))
        print(cevap)

if __name__ == "__main__":
    calis()