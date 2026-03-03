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



## 1.
