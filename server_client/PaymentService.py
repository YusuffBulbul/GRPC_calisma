import grpc
from concurrent import futures
import payment_pb2
import payment_pb2_grpc

class PaymentService(payment_pb2_grpc.PaymentServiceServicer):
    def ProcessPayment(self, request, context):
        print(f"Processing payment of ${request.amount}...")
        return payment_pb2.PaymentResponse(success=True)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    payment_pb2_grpc.add_PaymentServiceServicer_to_server(PaymentService(), server)
    server.add_insecure_port('[::]:50052')
    print("PaymentService running on port 50052...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
