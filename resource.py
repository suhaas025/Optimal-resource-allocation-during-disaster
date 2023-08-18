import tkinter as tk


class Node:
    def _init_(self, name):
        self.name = name
        self.neighbors = {}
        self.resources = {}

    def add_neighbor(self, neighbor, distance):
        self.neighbors[neighbor] = distance


class Graph:
    def _init_(self):
        self.nodes = {}

    def add_node(self, name):
        self.nodes[name] = Node(name)

    def add_edge(self, node1, node2, distance):
        self.nodes[node1].add_neighbor(self.nodes[node2], distance)
        self.nodes[node2].add_neighbor(self.nodes[node1], distance)


def build_graph():
    num_nodes = int(input("Enter the number of nodes: "))
    graph = Graph()

    for i in range(num_nodes):
        name = input(f"Enter the name for node {i + 1}: ")
        graph.add_node(name)

    for i in range(num_nodes):
        current_node_name = input(f"Enter the name of node {i + 1}: ")
        current_node = graph.nodes[current_node_name]

        neighbors = input(f"Enter the neighbors for node {current_node_name} (space-separated): ").split()

        for neighbor in neighbors:
            distance = int(input(f"Enter the distance between {current_node_name} and {neighbor}: "))
            graph.add_edge(current_node_name, neighbor, distance)

    return graph



def get_demand(graph):
    node_names = list(graph.nodes.keys())
    demand_dict = {}

    for name in node_names[1:]:
        root = tk.Tk()
        root.title(f"Demand for {name}")
        demand_label = tk.Label(root, text=f"Enter the demand for node {name}:")
        demand_label.pack()
        demand_entry = tk.Entry(root)
        demand_entry.pack()

        def save_demand():
            demand = demand_entry.get()
            demand_dict[name] = int(demand)
            root.destroy()

        save_button = tk.Button(root, text="Save", command=save_demand)
        save_button.pack()

        root.mainloop()

    return demand_dict


def main():
    graph = build_graph()
    
    

    print("\nGraph:")
    for node in graph.nodes.values():
        print(f"Node: {node.name}")
        print("Neighbors:")
        for neighbor, distance in node.neighbors.items():
            print(f"  Neighbor: {neighbor.name}, Distance: {distance}")
    demand_dict = get_demand(graph)
    sorted_demand = sorted(demand_dict.items(), key=lambda x: x[1], reverse=True)
    print("\nDemand List:")
    for node, demand in sorted_demand:
        print(f"Node {node}: {demand}")
        
    
    
    
    visited = set()
    total_distance = 0
    current_node = graph.nodes[list(graph.nodes.keys())[0]]  # Start from Node 1

    print("\nTraversed Path:")
    print(current_node.name)

    visited.add(current_node.name)
    
    for node, _ in sorted_demand:
        if node != list(graph.nodes.keys())[0]:
            for neighbor, distance in current_node.neighbors.items():
                if neighbor.name == node:
                    total_distance += distance
                    current_node = neighbor
                    print(current_node.name)
                    visited.add(current_node.name)
                    break

# Continue traversal to visit any remaining unvisited nodes
    while len(visited) < len(graph.nodes):
        for neighbor, distance in current_node.neighbors.items():
            if neighbor.name not in visited:
                total_distance += distance
                current_node = neighbor
                print(current_node.name)
                visited.add(current_node.name)
                break

    print("\nTotal Distance:", total_distance)




if _name_ == "_main_":
    main()
