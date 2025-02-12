import grpc
from concurrent import futures
import order_pb2
import order_pb2_grpc
import payment_pb2
import payment_pb2_grpc

# ---------------- OrderService as gRPC Server ----------------

class OrderService(order_pb2_grpc.OrderServiceServicer):
    def CreateOrder(self, request, context):
        print(f"Received order from user {request.user_id}, contacting PaymentService...")

        # gRPC Client olarak PaymentService çağırıyoruz
        channel = grpc.insecure_channel('localhost:50052')  # PaymentService'in adresi
        payment_stub = payment_pb2_grpc.PaymentServiceStub(channel)

        # Payment işlemi için istek gönderiyoruz
        payment_response = payment_stub.ProcessPayment(payment_pb2.PaymentRequest(amount=100))

        if payment_response.success:
            return order_pb2.OrderResponse(order_id="ORD-123", status="Confirmed")
        else:
            return order_pb2.OrderResponse(order_id="ORD-123", status="Failed")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_pb2_grpc.add_OrderServiceServicer_to_server(OrderService(), server)
    server.add_insecure_port('[::]:50051')
    print("OrderService running on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
