
# 🚚 Intelligent Courier Planning System
### A DAA-Based Parcel Packing and Delivery Route Optimization Prototype

## 📌 1. Project Overview

The **Intelligent Courier Planning System** is a Python-based prototype designed to simulate an intelligent courier management system.

The system accepts a collection of parcels, their delivery destinations, weights, priorities, and deadlines. It processes this information using different algorithmic techniques to generate an optimized parcel packing plan and an efficient delivery route.

The primary objective is to minimize delivery distance while maximizing the priority value of parcels loaded into a vehicle with limited carrying capacity.

This project demonstrates the practical application of multiple concepts from **Design and Analysis of Algorithms (DAA)**.

---

## 🎯 2. Project Objectives

- Sort parcels based on delivery priority and deadlines.
- Optimize vehicle loading using Dynamic Programming.
- Represent delivery locations using Graph Data Structures.
- Calculate shortest paths between delivery locations.
- Generate an approximate delivery route.
- Improve the initial route using local optimization.
- Generate a final delivery planning report.

---

## 🧠 3. Algorithms and DAA Concepts Used

The project integrates four major algorithmic approaches.

| DAA Concept | Algorithm | Purpose |
|---|---|---|
| Sorting | Merge Sort | Prioritize parcels |
| Dynamic Programming | 0/1 Knapsack | Optimize parcel selection |
| Graph Algorithms | Dijkstra's Algorithm | Find shortest paths |
| Approximation Algorithms | Nearest Neighbour | Generate delivery route |
| Local Optimization | 2-opt | Improve delivery route |

### 3.1 Merge Sort – Parcel Prioritization

Merge Sort is used to arrange parcels in descending order of priority.

If two parcels have the same priority, the parcel with the earlier deadline is placed first.

**Approach:**
1. Divide the parcel list into two halves.
2. Recursively sort both halves.
3. Merge the sorted halves.
4. Produce the final prioritized parcel list.

**Time Complexity:** O(n log n)

### 3.2 Dynamic Programming – 0/1 Knapsack

The vehicle has a limited carrying capacity.

The Knapsack algorithm selects parcels such that the total weight does not exceed the vehicle capacity while maximizing the sum of their priority scores.

**Approach:**
1. Create a DP table.
2. Consider each parcel individually.
3. Check whether the parcel can fit into the remaining capacity.
4. Compare including and excluding the parcel.
5. Select the combination with the maximum priority score.
6. Backtrack through the DP table to identify selected parcels.

**Time Complexity:** O(nW)

Where:
- n = Number of parcels.
- W = Vehicle capacity.

### 3.3 Dijkstra's Algorithm – Shortest Path

Delivery locations are represented as vertices in a weighted graph.

Roads connecting these locations are represented as edges, with distances assigned as weights.

Dijkstra's algorithm calculates the shortest distance from one location to every other reachable location.

A distance matrix is then generated using these shortest-path calculations.

**Time Complexity:** O((V + E) log V)

Where:
- V = Number of vertices.
- E = Number of edges.

### 3.4 Nearest Neighbour – Approximate TSP

The Travelling Salesman Problem (TSP) involves finding a route that visits every required destination and returns to the starting location.

Finding an optimal TSP route is computationally expensive for large datasets.

The Nearest Neighbour algorithm generates an approximate solution.

**Approach:**
1. Start from the delivery depot.
2. Find the nearest unvisited destination.
3. Travel to that destination.
4. Repeat until all destinations are visited.
5. Return to the depot.

**Time Complexity:** O(k²)

Where k = Number of delivery locations.

### 3.5 2-opt – Route Improvement

The 2-opt algorithm improves an existing delivery route by exchanging pairs of route edges.

It attempts to eliminate unnecessary travel distance.

**Approach:**
1. Take the initial delivery route.
2. Select two edges.
3. Reverse the intermediate route segment.
4. Calculate the new route distance.
5. Keep the change if the distance decreases.
6. Repeat until no improvement is found.

**Time Complexity:** O(k³) per full improvement pass.

---

## 🏗️ 4. System Architecture

The system follows a sequential algorithmic pipeline.

```text
              INPUT DATA
                  |
                  v
        +---------------------+
        |   Parcel Database   |
        +---------------------+
                  |
                  v
        +---------------------+
        |      Merge Sort     |
        |  Priority Sorting   |
        +---------------------+
                  |
                  v
        +---------------------+
        |   0/1 Knapsack DP   |
        |  Packing Optimizer  |
        +---------------------+
                  |
                  v
        +---------------------+
        |    Delivery Graph   |
        +---------------------+
                  |
                  v
        +---------------------+
        |  Dijkstra Algorithm |
        |  Distance Matrix    |
        +---------------------+
                  |
                  v
        +---------------------+
        |   Nearest Neighbour |
        |  Initial Route      |
        +---------------------+
                  |
                  v
        +---------------------+
        |       2-opt         |
        |  Route Improvement  |
        +---------------------+
                  |
                  v
        +---------------------+
        |   FINAL REPORT      |
        | Packing + Delivery  |
        +---------------------+
```

---

## 📂 5. Project Structure

```text
Intelligent-Courier-Planner/
│
├── courier_planner.py
│
└── README.md
```

The entire prototype is currently implemented in a single Python file.

---

## ⚙️ 6. Technologies Used

| Technology | Application |
|---|---|
| Python 3 | Core programming language |
| Heap / Priority Queue | Dijkstra's algorithm |
| Lists | Parcel storage and route representation |
| Dictionaries | Graph representation and distance matrix |
| Dynamic Programming | Vehicle packing optimization |
| Graph Theory | Delivery network representation |

No external Python packages are required.

---

## ▶️ 7. Installation and Execution

### Step 1: Clone the repository

```bash
git clone <your-repository-url>
```

### Step 2: Navigate to the project directory

```bash
cd Intelligent-Courier-Planner
```

### Step 3: Run the Python program

```bash
python courier_planner.py
```

The program will execute the complete courier planning pipeline and display the final delivery report.

---

## 📊 8. Sample Dataset

The prototype uses the following parcel dataset:

| Parcel ID | Destination | Weight | Priority | Deadline |
|---|---|---|---|---|
| P101 | A | 4 kg | 8 | 2 |
| P102 | B | 3 kg | 6 | 3 |
| P103 | C | 5 kg | 10 | 1 |
| P104 | D | 2 kg | 5 | 4 |
| P105 | E | 6 kg | 9 | 2 |
| P106 | B | 2 kg | 7 | 1 |
| P107 | C | 3 kg | 4 | 5 |

**Vehicle Capacity:** 12 kg

Multiple parcels may share the same delivery destination.

The route optimizer visits each selected destination once, even if multiple parcels need to be delivered there.

---

## 📈 9. Complexity Analysis

| Algorithm | Best / Typical Complexity | Purpose |
|---|---|---|
| Merge Sort | O(n log n) | Parcel sorting |
| 0/1 Knapsack | O(nW) | Parcel selection |
| Dijkstra | O((V+E) log V) | Shortest paths |
| Distance Matrix | O(V(V+E) log V) | All-pairs shortest paths |
| Nearest Neighbour | O(k²) | Route generation |
| 2-opt | O(k³) per pass | Route improvement |

### Variables

- n = Number of parcels.
- W = Vehicle capacity.
- V = Number of graph vertices.
- E = Number of graph edges.
- k = Number of selected delivery locations.

---

## ⚠️ 10. Current Limitations

The current implementation is a prototype and has some limitations:

1. Parcel data is currently hardcoded.
2. Vehicle capacity is fixed in the sample.
3. Delivery deadlines are used only as a sorting tie-breaker.
4. Knapsack optimization maximizes priority score, not deadline feasibility.
5. The system currently supports one vehicle.
6. Delivery locations are represented using a manually defined graph.
7. Nearest Neighbour and 2-opt do not guarantee a globally optimal TSP solution.
8. The system assumes road distances are non-negative and roads are bidirectional.
9. Packing is performed before route generation, so the system does not account for delivery deadlines when selecting parcels.

---

## 🚀 11. Future Enhancements

The prototype can be extended with the following features:

### Algorithmic Enhancements
- Multiple vehicle optimization.
- Multiple depot support.
- Deadline-aware parcel selection.
- Time-window-constrained routing.
- Advanced TSP approximation techniques.
- Improved packing strategies.

### Application Enhancements
- Interactive parcel input.
- Real-time delivery route visualization.
- Map integration.
- Courier performance dashboard.
- Delivery analytics and reports.
- Database integration for parcel management.

---

## 🎓 12. Learning Outcomes

Through this project, the following DAA concepts are demonstrated:

- Divide and Conquer through Merge Sort.
- Dynamic Programming through 0/1 Knapsack.
- Greedy techniques through Nearest Neighbour.
- Graph representation and traversal concepts.
- Shortest path optimization through Dijkstra.
- Approximation techniques for NP-hard optimization problems.
- Local search optimization through 2-opt.
- Analysis of time and space complexity.

---

## 🏁 13. Conclusion

The Intelligent Courier Planning System demonstrates how multiple algorithmic techniques can work together to solve a real-world logistics problem.

By combining sorting, dynamic programming, graph algorithms, and approximation techniques, the prototype creates a systematic approach to parcel selection, vehicle packing, and delivery route planning.

The project highlights the practical importance of Design and Analysis of Algorithms in developing efficient computational solutions for real-world problems.

---

**Project:** Intelligent Courier Planning System  
**Domain:** Design and Analysis of Algorithms  
**Language:** Python  
**Project Type:** Academic Capstone Prototype
