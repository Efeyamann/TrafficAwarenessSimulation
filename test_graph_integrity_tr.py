from story_data import STORY_GRAPH

def validate_graph():
    print("Validating Story Graph (Turkish Nodes)...")
    errors = []
    
    # Check start node existence
    if "baslangic" not in STORY_GRAPH:
        errors.append("Critical: 'baslangic' node is missing!")

    for node_id, node_data in STORY_GRAPH.items():
        # Check if node has options or is final
        if node_data.get("type") == "final":
            continue
            
        options = node_data.get("options", [])
        if not options and node_data.get("type") != "final":
             errors.append(f"Node '{node_id}' has no options and is not marked as final.")
             
        for opt in options:
            next_node = opt.get("next_node")
            if not next_node:
                errors.append(f"Node '{node_id}' has an option without 'next_node'.")
            elif next_node not in STORY_GRAPH:
                errors.append(f"Node '{node_id}' points to non-existent node '{next_node}'.")
                
    if errors:
        print("ERRORS FOUND:")
        for e in errors:
            print(f"- {e}")
    else:
        print("Graph validation successful! All paths match.")

if __name__ == "__main__":
    validate_graph()
