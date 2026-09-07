# System Blueprint: YusuffBulbul/GRPC_calisma

> Architecture analysis
>
> Auto-generated on 2026-09-07 by Repo-to-Blueprint Architect

# English Version

## Project Purpose
This repository is a collection of gRPC implementation exercises and prototypes in Python. It demonstrates service-to-service communication using Protocol Buffers across various domains including greeting services and basic order/payment processing.

## Technical Stack
- **Language**: Python (`.py`)
- **Framework**: gRPC (indicated by `pb2_grpc.py` and `pb2.py` artifacts)
- **Key Dependencies**: `grpcio`, `protobuf` (evidenced by `.proto` files and generated stubs)

## Architecture Blueprint

```mermaid
flowchart TD
    subgraph Protobuf ["IDL Layer (.proto)"]
        P1["deneme.proto"]
        P2["helloworld.proto"]
        P3["order.proto"]
        P4["payment.proto"]
    end

    subgraph Generated ["gRPC Generated Code"]
        G1["*_pb2.py (Messages)"]
        G2["*_pb2_grpc.py (Services)"]
    end

    subgraph Logic ["Application Logic"]
        S1["OrderService.py"]
        S2["PaymentService.py"]
        S3["*_server.py"]
        C1["*_client.py"]
    end

    P1 & P2 & P3 & P4 --> G1 & G2
    G2 --> S1 & S2 & S3
    G2 --> C1
    C1 -->|"gRPC/HTTP2"| S1 & S2 & S3

    style Protobuf fill:#1f6feb,stroke:#58a6ff,color:#fff
    style Generated fill:#8b949e,stroke:#c9d1d9,color:#fff
    style Logic fill:#238636,stroke:#3fb950,color:#fff

```

## Request Flow

```mermaid
sequenceDiagram
    participant C as Client (e.g., deneme_client.py)
    participant G as gRPC Channel
    participant S as Server (e.g., deneme_server.py)

    C->>G: Invoke Remote Procedure (Stub)
    G->>S: Transmit Serialized Protobuf (HTTP/2)
    S->>S: Execute Service Logic
    S-->>G: Return Response Message
    G-->>C: Deserialize & Return to Caller

```

## Evidence-Based Risks
1. **Redundant Codebase**: The repository contains multiple duplicated implementations of similar gRPC patterns (`grpc_kendi`, `python_grpc`, `grpc_quickstart`), suggesting a lack of a unified project structure or shared library.
2. **Missing Dependency Management**: There are no `requirements.txt` or `pyproject.toml` files in the tree, which makes environment reproduction and version pinning for `grpcio` and `protobuf` impossible.
3. **Manual Artifact Tracking**: Compiled files (`*_pb2.py`) are committed directly to the repository alongside source `.proto` files. This is a risk for version mismatch if `.proto` files are updated without regenerating the Python stubs.

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
