import networkx as nx

def get_input():
    train_count = 3  # Always set the number of trains to 3
    stations = []
    train_routes = []

    for _ in range(train_count):
        train_route = []
        num_stations = int(input("Enter the number of stations for this train: "))

        for i in range(num_stations):
            station_name = input(f"Enter station {i + 1} name: ")
            stations.append(station_name)
            train_route.append(station_name)

        train_routes.append(train_route)

    return stations, train_routes

def create_graph(stations):
    graph = nx.Graph()

    for i in range(len(stations)):
        for j in range(i + 1, len(stations)):
            distance = float(input(f"Enter distance between {stations[i]} and {stations[j]}: "))
            graph.add_edge(stations[i], stations[j], weight=distance)
            graph.add_edge(stations[j], stations[i], weight=distance)  # Add the reverse edge

    return graph

def find_longest_route(graph, train_routes):
    longest_path = None
    longest_distance = -1

    for source in graph.nodes:
        for target in graph.nodes:
            if source != target:
                distance = nx.shortest_path_length(graph, source=source, target=target, weight='weight')
                if distance > longest_distance:
                    longest_distance = distance
                    longest_path = nx.shortest_path(graph, source=source, target=target, weight='weight')

    return longest_path, longest_distance

def remove_stopped_station(graph, stopped_station):
    for station in stopped_station:
        graph.remove_node(station)

def find_second_longest_route(graph, train_routes):
    second_longest_path = None
    second_longest_distance = -1

    for source in graph.nodes:
        for target in graph.nodes:
            if source != target:
                distance = nx.shortest_path_length(graph, source=source, target=target, weight='weight')
                if distance > second_longest_distance:
                    second_longest_distance = distance
                    second_longest_path = nx.shortest_path(graph, source=source, target=target, weight='weight')

    return second_longest_path, second_longest_distance

def main():
    print("Welcome to the Railway Track Planning System")

    stations, train_routes = get_input()
    graph = create_graph(stations)

    for i in range(3):  # Always set the number of trains to 3
        print(f"Train {i + 1} Route: {train_routes[i]}")
        stopped_station = input(f"Enter the station where Train {i + 1} stops (or press Enter if none): ").split()
        if stopped_station:
            remove_stopped_station(graph, stopped_station)

    longest_path, longest_distance = find_longest_route(graph, train_routes)
    print(f"The longest route is: {longest_path} with distance {longest_distance}")

    second_longest_path, second_longest_distance = find_second_longest_route(graph, train_routes)
    print(f"The second longest route is: {second_longest_path} with distance {second_longest_distance}")

if __name__ == "__main__":
    main()
