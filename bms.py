def build_tree():
    tree = {}

    while True:
        node = input("Enter a node (or 'done' to finish): ")
        if node == 'done':
            break

        children_str = input(f"Enter children of '{node}' separated by spaces (or 'none' for no children): ")
        if children_str != 'none':
            children = children_str.split()
            tree[node] = []

            for child in children:
                cost = int(input(f"Enter the cost from '{node}' to '{child}': "))
                tree[node].append((child, cost))

    return tree

def find_all_paths(tree, start_node, end_node, path=None, cost=0):
    if path is None:
        path = []

    path = path + [start_node]

    if start_node == end_node:
        return [(path, cost)]

    if start_node not in tree:
        return []

    paths = []
    for child, edge_cost in tree[start_node]:
        if child not in path:
            new_paths = find_all_paths(tree, child, end_node, path, cost + edge_cost)
            for new_path, new_cost in new_paths:
                paths.append((new_path, new_cost))

    return paths

def main():
    tree = build_tree()
    start_node = input("Enter the start node: ")
    end_node = input("Enter the end node: ")

    paths = find_all_paths(tree, start_node, end_node)

    if not paths:
        print(f"No path found from '{start_node}' to '{end_node}'.")
    else:
        print(f"All possible paths from '{start_node}' to '{end_node}':")
        for i, (path, cost) in enumerate(paths, start=1):
            print(f"Path {i}: {' -> '.join(path)}, Cost: {cost}")

main()  # Call the main function directly
