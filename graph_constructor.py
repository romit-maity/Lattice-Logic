import json
import torch
from torch_geometric.data import Data

def build_graph(file_path="data/jira_tasks.json"):
    with open(file_path, "r") as f:
        tasks = json.load(f)

    # 1. Map Task IDs to numeric indices (0, 1, 2...)
    id_map = {task["task_id"]: i for i, task in enumerate(tasks)}
    
    # 2. Encode Features (Status & Priority)
    # Status Map: Done=0, In Progress=1, Blocked=2
    status_map = {"Done": 0, "In Progress": 1, "Blocked": 2}
    
    node_features = []
    for task in tasks:
        features = [
            status_map.get(task["status"], 1), 
            task["priority"]
        ]
        node_features.append(features)
    
    x = torch.tensor(node_features, dtype=torch.float)

    # 3. Define Edges (Dependencies)
    edge_index_list = []
    for task in tasks:
        target_idx = id_map[task["task_id"]]
        for dep_id in task["depends_on"]:
            if dep_id in id_map:
                source_idx = id_map[dep_id]
                # Edge goes from Dependency -> Task
                edge_index_list.append([source_idx, target_idx])

    # Convert to PyG format [2, num_edges]
    edge_index = torch.tensor(edge_index_list, dtype=torch.long).t().contiguous()

    # 4. Create the Data Object
    data = Data(x=x, edge_index=edge_index)
    
    print(f"[✓] Graph Construction Successful")
    print(f"Nodes: {data.num_nodes}, Edges: {data.num_edges}")
    return data

if __name__ == "__main__":
    build_graph()