def build_tree():
    tree = {}
    
    while True:
        node = input("Enter a node (or 'done' to finish): ")
        if node == 'done':
            break
        
        children = input(f"Enter children of '{node}' separated by spaces: ").split()
        tree[node] = children
    
    return tree

def hill_climbing(tree, start, goal):
    current_node = start
    path = [current_node]

    while current_node != goal:
        if current_node not in tree:
            print(f"Node '{current_node}' not found in the tree.")
            break

        children = tree[current_node]
        if not children:
            print(f"Node '{current_node}' has no children.")
            break

        best_child = None
        best_cost = float('inf')

        for child in children:
            cost = float(input(f"Enter the cost from '{current_node}' to '{child}': "))
            if cost < best_cost:
                best_child = child
                best_cost = cost

        if best_child:
            path.append(best_child)
            current_node = best_child
        else:
            print("No valid child found. Hill climbing terminated.")
            break

    return path

tree = build_tree()
start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")

path = hill_climbing(tree, start_node, goal_node)
print(f"Optimal path from {start_node} to {goal_node}: {path}")
