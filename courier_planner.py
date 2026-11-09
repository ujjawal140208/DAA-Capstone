
import heapq


# ============================================================
# 1. PARCEL DATA
# ============================================================

class Parcel:
    def __init__(self, parcel_id, destination, weight, priority, deadline):
        self.parcel_id = parcel_id
        self.destination = destination
        self.weight = weight
        self.priority = priority
        self.deadline = deadline

    def __repr__(self):
        return (
            f"{self.parcel_id} -> {self.destination} | "
            f"Weight: {self.weight}kg | "
            f"Priority: {self.priority}"
        )


# ============================================================
# 2. SORTING - MERGE SORT
# ============================================================

def merge_sort(parcels):

    if len(parcels) <= 1:
        return parcels

    mid = len(parcels) // 2

    left = merge_sort(parcels[:mid])
    right = merge_sort(parcels[mid:])

    return merge(left, right)


def merge(left, right):

    result = []

    while left and right:

        # Higher priority first.
        # For equal priority, earlier deadline first.
        key_left = (-left[0].priority, left[0].deadline)
        key_right = (-right[0].priority, right[0].deadline)

        if key_left <= key_right:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result.extend(left)
    result.extend(right)

    return result


# ============================================================
# 3. DYNAMIC PROGRAMMING - 0/1 KNAPSACK
# ============================================================

def optimize_packing(parcels, capacity):

    n = len(parcels)

    # DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):

        weight = parcels[i - 1].weight
        value = parcels[i - 1].priority

        for w in range(capacity + 1):

            dp[i][w] = dp[i - 1][w]

            if weight <= w:

                dp[i][w] = max(
                    dp[i][w],
                    value + dp[i - 1][w - weight]
                )

    # Backtracking to find selected parcels
    selected = []
    remaining_capacity = capacity

    for i in range(n, 0, -1):

        if dp[i][remaining_capacity] != dp[i - 1][remaining_capacity]:

            parcel = parcels[i - 1]
            selected.append(parcel)

            remaining_capacity -= parcel.weight

    selected.reverse()

    return selected, dp[n][capacity]


# ============================================================
# 4. GRAPH - DIJKSTRA'S SHORTEST PATH ALGORITHM
# ============================================================

class DeliveryGraph:

    def __init__(self):
        self.graph = {}

    def add_location(self, location):
        if location not in self.graph:
            self.graph[location] = []

    def add_road(self, source, destination, distance):

        self.add_location(source)
        self.add_location(destination)

        self.graph[source].append((destination, distance))
        self.graph[destination].append((source, distance))

    def dijkstra(self, start):

        distances = {
            node: float('inf')
            for node in self.graph
        }

        distances[start] = 0

        pq = [(0, start)]

        while pq:

            current_distance, current_node = heapq.heappop(pq)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:

                new_distance = current_distance + weight

                if new_distance < distances[neighbor]:

                    distances[neighbor] = new_distance

                    heapq.heappush(
                        pq,
                        (new_distance, neighbor)
                    )

        return distances


# ============================================================
# 5. APPROXIMATION - DISTANCE MATRIX
# ============================================================

def build_distance_matrix(graph, locations):

    matrix = {}

    for source in locations:

        shortest_distances = graph.dijkstra(source)

        matrix[source] = {}

        for destination in locations:

            matrix[source][destination] = (
                shortest_distances.get(
                    destination,
                    float('inf')
                )
            )

    return matrix


# ============================================================
# 6. APPROXIMATION - NEAREST NEIGHBOUR
# ============================================================

def nearest_neighbour(matrix, depot, destinations):

    unvisited = set(destinations)
    route = [depot]

    current = depot

    while unvisited:

        next_location = min(
            unvisited,
            key=lambda location: matrix[current][location]
        )

        route.append(next_location)

        unvisited.remove(next_location)

        current = next_location

    route.append(depot)

    return route


# ============================================================
# 7. APPROXIMATION - 2-OPT IMPROVEMENT
# ============================================================

def two_opt(route, matrix):

    best_route = route[:]

    improved = True

    while improved:

        improved = False

        for i in range(1, len(best_route) - 2):

            for j in range(i + 1, len(best_route) - 1):

                new_route = (
                    best_route[:i]
                    + best_route[i:j + 1][::-1]
                    + best_route[j + 1:]
                )

                old_distance = sum(
                    matrix[best_route[k]][best_route[k + 1]]
                    for k in range(len(best_route) - 1)
                )

                new_distance = sum(
                    matrix[new_route[k]][new_route[k + 1]]
                    for k in range(len(new_route) - 1)
                )

                if new_distance < old_distance:

                    best_route = new_route
                    improved = True

    return best_route


# ============================================================
# 8. ROUTE DISTANCE
# ============================================================

def calculate_route_distance(route, matrix):

    total = 0

    for i in range(len(route) - 1):

        total += matrix[route[i]][route[i + 1]]

    return total


# ============================================================
# 9. MAIN COURIER PLANNING SYSTEM
# ============================================================

def courier_planner():

    print("\n========================================")
    print("     INTELLIGENT COURIER PLANNER")
    print("========================================")

    # Sample parcel data
    parcels = [

        Parcel("P101", "A", 4, 8, 2),
        Parcel("P102", "B", 3, 6, 3),
        Parcel("P103", "C", 5, 10, 1),
        Parcel("P104", "D", 2, 5, 4),
        Parcel("P105", "E", 6, 9, 2),
        Parcel("P106", "B", 2, 7, 1),
        Parcel("P107", "C", 3, 4, 5)

    ]

    vehicle_capacity = 12
    depot = "DEPOT"

    # --------------------------------------------------------
    # STEP 1: SORT PARCELS
    # --------------------------------------------------------

    print("\n1. SORTED PARCELS")

    sorted_parcels = merge_sort(parcels)

    for parcel in sorted_parcels:
        print(parcel)

    # --------------------------------------------------------
    # STEP 2: OPTIMIZE PACKING
    # --------------------------------------------------------

    print("\n2. OPTIMIZED PACKING PLAN")

    selected, total_priority = optimize_packing(
        sorted_parcels,
        vehicle_capacity
    )

    total_weight = sum(p.weight for p in selected)

    for parcel in selected:
        print(parcel)

    print("\nVehicle Capacity:", vehicle_capacity, "kg")
    print("Total Packed Weight:", total_weight, "kg")
    print("Remaining Capacity:", vehicle_capacity - total_weight, "kg")
    print("Total Priority Score:", total_priority)

    # --------------------------------------------------------
    # STEP 3: BUILD DELIVERY GRAPH
    # --------------------------------------------------------

    print("\n3. DELIVERY GRAPH")

    graph = DeliveryGraph()

    roads = [

        ("DEPOT", "A", 4),
        ("DEPOT", "B", 6),
        ("DEPOT", "C", 8),
        ("A", "B", 2),
        ("A", "D", 5),
        ("B", "C", 3),
        ("B", "D", 4),
        ("C", "D", 2),
        ("C", "E", 5),
        ("D", "E", 3),
        ("E", "DEPOT", 9)

    ]

    for source, destination, distance in roads:

        graph.add_road(source, destination, distance)

        print(source, "<-->", destination, ":", distance, "km")

    # --------------------------------------------------------
    # STEP 4: SHORTEST PATH DISTANCE MATRIX
    # --------------------------------------------------------

    destinations = sorted(
        set(p.destination for p in selected)
    )

    locations = [depot] + destinations

    matrix = build_distance_matrix(graph, locations)

    print("\n4. SHORTEST DISTANCE MATRIX")

    print("Locations:", locations)

    for location in locations:

        print(
            location,
            matrix[location]
        )

    # --------------------------------------------------------
    # STEP 5: APPROXIMATE DELIVERY ROUTE
    # --------------------------------------------------------

    print("\n5. OPTIMIZED DELIVERY ROUTE")

    initial_route = nearest_neighbour(
        matrix,
        depot,
        destinations
    )

    initial_distance = calculate_route_distance(
        initial_route,
        matrix
    )

    optimized_route = two_opt(
        initial_route,
        matrix
    )

    optimized_distance = calculate_route_distance(
        optimized_route,
        matrix
    )

    print("Initial Route:", " -> ".join(initial_route))
    print("Initial Distance:", initial_distance, "km")

    print("\nImproved Route:", " -> ".join(optimized_route))
    print("Optimized Distance:", optimized_distance, "km")

    # --------------------------------------------------------
    # STEP 6: FINAL DELIVERY REPORT
    # --------------------------------------------------------

    print("\n========================================")
    print("          FINAL DELIVERY REPORT")
    print("========================================")

    print("\nSelected Parcels:")

    for parcel in selected:
        print(parcel.parcel_id, "->", parcel.destination)

    print("\nDelivery Sequence:")

    for index, location in enumerate(optimized_route):

        if index == 0:
            print("START:", location)

        elif index == len(optimized_route) - 1:
            print("RETURN:", location)

        else:
            print(f"STOP {index}: {location}")

    print("\nTotal Parcels:", len(selected))
    print("Total Weight:", total_weight, "kg")
    print("Vehicle Capacity:", vehicle_capacity, "kg")
    print("Total Delivery Distance:", optimized_distance, "km")

    if initial_distance > 0:

        improvement = (
            (initial_distance - optimized_distance)
            / initial_distance
        ) * 100

        print("Route Improvement:", round(improvement, 2), "%")

    print("\nCourier Planning Completed Successfully!")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    courier_planner()
