# Technical Design Document

---

# Phase 1: Infrastructure & Environment

## 1. Infrastructure

#### **Decision**: Implementation of a Dockerized Multi-Database Stack.

- **Why Neo4j?** 
  
  - Standard relational databases fail at deep dependency nesting. 
  
  - Neo4j's native graph processing allows **Project Aether** to calculate ***Node Criticality*** or ***Risk*** across infinite links.

- **Why ChromaDB?**
  
  - To enable **Hybrid RAG**, combining ***structured graph data***  with ***unstructured historical text (Post-Mortems)***.

- **Security**
  
  - Implemented ***.env*** masking to comply with production standards.

## 

## 2. Database Connectivity & Benchmarking

#### Decision: Using a centralized *DatabaseManager* class.

- **Why?**
  
  - Centralizing the connection logic ensures that we handle ***"Graceful Shutdowns"*** and ***connection pooling*** in one place.
  
  - Prevents memory leaks in production.

- **Protocol:**
  
  - Benchmarking via **heartbeat()** for **ChromaDB**.
  
  - Benchmarking via **RETURN 1 Cypher query**  for **Neo4j**.
  
  - Ensures the ***"Ground Truth*** is reachable before any logic is executed.

---

# Phase 2: GNN Ingestion

## 1. GNN Data Engineering

#### Decision: Generating synthetic JSON logs with intentional *"padding"* and *"bottlenecks"*.

- **Why?**
  
  - **GNNs** require "Data Density" to learn patterns.
  
  - By forcing specific tasks ***(like AETH-10)*** to have ***high dependency counts***, we create a "Ground Truth" for the model to identify as a ***high-risk failure point***.

- **Protocol:**
  
  - JSON format ensures compatibility with both the **Neo4j ingestion (Graph)** and the **PyTorch Geometric Data object (Tensors)**.



## 2. Graph Construction & Feature Encoding

#### Decision: Mapping string IDs to an Adjacency Matrix *('edge_index')*.

- **Why?**
  
  - **Neural networks** cannot process strings. 
  
  - We use a ***"Label Encoding*** strategy for ***task status*** to ensure the **GNN** can mathematically differentiate between 'Blocked' and 'Done'.

- **Data Object:**
  
  - Utilizing the ***torch_geometric.data*** data structure to store ***node features (x)*** and ***connectivity (edge_index)*** in a GPU-ready format.

---
