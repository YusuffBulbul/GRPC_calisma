# System Blueprint: YusuffBulbul/GRPC_calisma

> Architecture analysis
>
> Auto-generated on 2026-09-07 by Repo-to-Blueprint Architect

# English Version

## Project Purpose
This repository is a collection of gRPC (Google Remote Procedure Call) implementations and experiments in Python. It demonstrates service-to-service communication using Protocol Buffers (Protobuf) for various scenarios, including a simulated Order-Payment system and standard Greeter examples.

## Technical Stack
- **Language**: Python (.py)
- **Framework**: gRPC
- **Key Dependencies**: `protobuf` (inferred from `.proto` and `_pb2.py` files), `grpcio` (inferred from `_pb2_grpc.py` files).
- **Interface Definition**: Protocol Buffers (.proto)

## Architecture Blueprint

```mermaid
flowchart TD
    subgraph Protobuf_Layer ["Protobuf Definitions (.proto)"]
        P1["deneme.proto"]
        P2["order.proto"]
        P3["payment.proto"]
        P4["helloworld.proto"]
    end

    subgraph Service_Logic ["Service Implementation"]
        S1["OrderService.py"]
        S2["PaymentService.py"]
        S3["deneme_server.py"]
        S4["greeter_server.py"]
    end

    subgraph Client_Logic ["Client Implementation"]
        C1["last_client.py"]
        C2["yusuf_client.py"]
        C3["greet_client.py"]
        C4["deneme_client.py"]
    end

    P1 -.->|"generates"| S3
    P2 -.->|"generates"| S1
    P3 -.->|"generates"| S2
    P4 -.->|"generates"| S4

    C1 -->|"gRPC Call"| S1
    C4 -->|"gRPC Call"| S3
    C2 -->|"gRPC Call"| S3

    style P1 fill:#1f6feb,stroke:#58a6ff,color:#fff
    style P2 fill:#1f6feb,stroke:#58a6ff,color:#fff
    style P3 fill:#1f6feb,stroke:#58a6ff,color:#fff
    style P4 fill:#1f6feb,stroke:#58a6ff,color:#fff

    style S1 fill:#238636,stroke:#3fb950,color:#fff
    style S2 fill:#238636,stroke:#3fb950,color:#fff
    style S3 fill:#238636,stroke:#3fb950,color:#fff
    style S4 fill:#238636,stroke:#3fb950,color:#fff

```

## Request Flow

```mermaid
sequenceDiagram
    participant C as Client (deneme_client.py)
    participant G as gRPC Channel
    participant S as Server (deneme_server.py)

    C->>G: Initialize insecure_channel()
    C->>G: Request with Protobuf Message
    G->>S: Remote Procedure Call (RPC)
    Note over S: Executes service logic (deneme_pb2_grpc)
    S->>G: Serialized Protobuf Response
    G->>C: Decoded Python Object

```

## Evidence-Based Risks
1. **Lack of Encryption**: Implementation files such as `deneme_client.py` and `greeter_client.py` use `insecure_channel`, indicating that data is transmitted in plaintext without TLS/SSL.
2. **Hardcoded Configurations**: Service endpoints and ports are hardcoded directly within the server and client scripts (e.g., `deneme_server.py`, `yusuf_server.py`), complicating deployment across different environments.
3. **Manual Artifact Management**: The repository contains both `.proto` source files and generated `_pb2.py` / `_pb2_grpc.py` files in the same directories, which can lead to version mismatch risks if the Protobuf compiler is not synchronized across environments.

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
