import last_dance_pb2
import last_dance_pb2_grpc
import grpc

def calis():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = last_dance_pb2_grpc.son_servisStub(channel)

        response = stub.toplama(last_dance_pb2.istek_sayilar(sayi_1 = 10,sayi_2 = 20))
        print(response.toplam)

        response = stub.birlestirme(last_dance_pb2.istek_isimler(isim_1 = "Yusuf",isim_2 = "Enes"))
        print(response.isim)
    

if __name__ == "__main__":
    calis()
