# System Blueprint: YusuffBulbul/GRPC_calisma

> Architecture analysis
>
> Auto-generated on 2026-09-07 by Repo-to-Blueprint Architect

# English Version

## Project Purpose
This project serves as a comprehensive study and implementation laboratory for gRPC (Google Remote Procedure Call) using Python. It demonstrates unary and potentially streaming communication patterns through various service implementations including greeting systems, order management, and payment processing.

## Technical Stack
- **Language**: Python
- **Framework**: gRPC
- **Key Dependencies**: `grpcio`, `protobuf` (Inferred from `_pb2.py` and `_pb2_grpc.py` files)

## Architecture Blueprint

```mermaid
flowchart TD
    subgraph Protobuf ["Interface Definitions (.proto)"]
        P1["deneme.proto"]
        P2["helloworld.proto"]
        P3["order.proto"]
        P4["payment.proto"]
    end

    subgraph Generated ["gRPC Stubs & Messages"]
        G1["deneme_pb2_grpc.py"]
        G2["helloworld_pb2_grpc.py"]
        G3["order_pb2_grpc.py"]
        G4["payment_pb2_grpc.py"]
    end

    subgraph Logic ["Service Implementations"]
        S1["deneme_server.py"]
        S2["greeter_server.py"]
        S3["OrderService.py"]
        S4["PaymentService.py"]
    end

    subgraph Clients ["Client Applications"]
        C1["deneme_client.py"]
        C2["greeter_client.py"]
        C3["greet_client.py"]
    end

    P1 -.-> G1
    P2 -.-> G2
    P3 -.-> G3
    P4 -.-> G4

    G1 --> S1
    G2 --> S2
    G3 --> S3
    G4 --> S4

    C1 --> G1
    C2 --> G2
    C3 --> G2

    style Protobuf fill:#1f6feb,stroke:#58a6ff,color:#fff
    style Generated fill:#8b949e,stroke:#c9d1d9,color:#fff
    style Logic fill:#238636,stroke:#3fb950,color:#fff
    style Clients fill:#1f6feb,stroke:#58a6ff,color:#fff

```

## Request Flow

```mermaid
sequenceDiagram
    participant Client as Client Application (e.g., yusuf_client.py)
    participant Stub as gRPC Generated Stub
    participant Server as gRPC Server (e.g., yusuf_server.py)

    Note over Client, Server: Connection initialized on localhost:50051
    Client->>Stub: Call RPC Method (Request Object)
    Stub->>Server: Serialize & Send Proto Request
    Server->>Server: Execute Business Logic
    Server->>Stub: Return Proto Response
    Stub->>Client: Deserialize & Return Result

```

## Evidence-Based Risks
1. **Hardcoded Configurations**: Service endpoints (e.g., `localhost:50051`) are hardcoded directly within `client.py` and `server.py` files across all subdirectories, hindering environment portability.
2. **Lack of Encryption**: No evidence of `grpc.ssl_channel_credentials()` usage in client files or secure port binding in server files, indicating the use of insecure channels.
3. **Redundant Codebase**: Multiple directories (`grpc_kendi`, `python_grpc`, `grpc_quickstart`) contain overlapping logic and duplicate `.proto` definitions, increasing maintenance overhead and risk of version mismatch.

---

## Repository Stats
| Metric | Value |
|---|---|
| Total Files | 40 |
| Total Directories | 7 |
| Generated | 2026-09-07 |
| Source | [YusuffBulbul/GRPC_calisma](https://github.com/YusuffBulbul/GRPC_calisma) |

---

*Repo-to-Blueprint Architect via n8n*
