import os
from dotenv import load_dotenv
from neo4j import GraphDatabase
import chromadb

# Load environment variables from .env
load_dotenv()

class DatabaseManager:
    def __init__(self):
        self.neo4j_uri = os.getenv("NEO4J_URI")
        self.neo4j_password = os.getenv("NEO4J_PASSWORD")
        self.neo4j_driver = GraphDatabase.driver(self.neo4j_uri, auth=("neo4j", self.neo4j_password))
        
        # Initialize ChromaDB Client
        self.chroma_client = chromadb.HttpClient(host='localhost', port=8000)

    def check_connections(self):
        # Test Neo4j
        with self.neo4j_driver.session() as session:
            result = session.run("RETURN 'Neo4j Connected' AS message")
            neo4j_status = result.single()["message"]
        
        # Test ChromaDB
        chroma_status = "ChromaDB Connected" if self.chroma_client.heartbeat() else "ChromaDB Failed"
        
        return neo4j_status, chroma_status

    def close(self):
        self.neo4j_driver.close()

if __name__ == "__main__":
    db = DatabaseManager()
    n_status, c_status = db.check_connections()
    print(f"[✓] {n_status}")
    print(f"[✓] {c_status}")
    db.close()