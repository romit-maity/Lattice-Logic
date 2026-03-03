import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv
from graph_constructor import build_graph

# 1. Define the GCN Architecture
class RiskGNN(torch.nn.Module):
    def __init__(self, num_node_features):
        super(RiskGNN, self).__init__()
        # First layer: Processes features (Status/Priority)
        self.conv1 = GCNConv(num_node_features, 16)
        # Second layer: Outputs a single Risk Score per node
        self.conv2 = GCNConv(16, 1)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        
        # Pass through first layer with ReLU activation
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        
        # Pass through second layer to get the final risk score
        x = self.conv2(x, edge_index)
        return x

def run_risk_audit():
    # Load the graph we built in Task 2.2
    data = build_graph()
    
    # Initialize the model (2 input features: Status, Priority)
    model = RiskGNN(num_node_features=2)
    
    # Set to evaluation mode
    model.eval()
    
    # Generate Risk Scores
    with torch.no_grad():
        risk_scores = model(data)
    
    print("\n--- Risk Audit Results ---")
    for i, score in enumerate(risk_scores[:5]): # Show first 5 tasks
        print(f"Task AETH-{i+1}: Predicted Risk Score = {score.item():.4f}")
    
    # Phase 2 Benchmark Check
    if torch.any(risk_scores != 0):
        print("\n[✓] Benchmark Met: Non-zero risk scores generated.")
    else:
        print("\n[X] Benchmark Failed: Scores are zero. Check graph connectivity.")

if __name__ == "__main__":
    run_risk_audit()