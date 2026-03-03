import json
import random
import os

def generate_synthetic_data(output_path="data/jira_tasks.json"):
    """
    Generates synthetic Jira-like tasks with intentional 
    dependency chains to test GNN risk prediction.
    """
    tasks = []
    # 1. Define some sample developers
    devs = ["Alice", "Bob", "Charlie", "Dave"]
    
    # 2. Create 20 tasks with varying 'Risk' attributes
    for i in range(1, 21):
        task = {
            "task_id": f"AETH-{i}",
            "developer": random.choice(devs),
            "status": random.choice(["Done", "In Progress", "Blocked"]),
            "priority": random.randint(1, 5),
            "description": f"Feature component {i} implementation",
            "depends_on": [] # We will fill this next
        }
        tasks.append(task)

    # 3. Create "Cascading Failure" Dependencies
    # We force AETH-10 to depend on many things to make it 'Critical'
    for i in range(1, 5):
        tasks[9]["depends_on"].append(f"AETH-{i}")
        
    # Ensure the data directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as f:
        json.dump(tasks, f, indent=4)
    
    print(f"Successfully generated {len(tasks)} tasks at {output_path}")

if __name__ == "__main__":
    generate_synthetic_data()