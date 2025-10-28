def astarAlgo(start_node, stop_node):
    open_set = {start_node}
    closed_set = set()
    g = {}
    parents = {}

    g[start_node] = 0
    parents[start_node] = start_node

    while open_set:
        n = None
        for v in open_set:
            if n is None or g[v] + get_heuristic(v) < g[n] + get_heuristic(n):
                n = v

        print(f"\nEvaluating node: {n} (g: {g[n]}, h: {get_heuristic(n)}, f: {g[n] + get_heuristic(n)})")
        print(f"Open set: {open_set}")
        print(f"Closed set: {closed_set}")

        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found:', path)
            return path

        print(f"Exploring neighbors of {n}:")
        for (m, weight) in Graph_nodes.get(n, []):
            h_m = get_heuristic(m)
            print(f"Neighbor: {m}, weight: {weight}, h({m}): {h_m}")
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
                print(f"Added {m} to open set with g({m}) = {g[m]} and f({m}) = {g[m] + h_m}")
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)
                        print(f"Updated {m} to have a shorter path with g({m}) = {g[m]} and f({m}) = {g[m] + h_m}")

        open_set.remove(n)
        closed_set.add(n)

    print('Path does not exist!')
    return None

def get_heuristic(n):
    H_dist = {
        'S': 5,
        'A': 3,
        'B': 4,
        'C': 2,
        'D': 6,
        'G': 0,
    }
    return H_dist.get(n, 0)

Graph_nodes = {
    'S': [('A', 1), ('G', 10)],
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 5)],
    'C': [('D', 3), ('G', 4)],
    'D': [('G', 2)],
}
astarAlgo('S', 'G')


""" output::


Evaluating node: S (g: 0, h: 5, f: 5)
Open set: {'S'}
Closed set: set()
Exploring neighbors of S:
Neighbor: A, weight: 1, h(A): 3
Added A to open set with g(A) = 1 and f(A) = 4
Neighbor: G, weight: 10, h(G): 0
Added G to open set with g(G) = 10 and f(G) = 10

Evaluating node: A (g: 1, h: 3, f: 4)
Open set: {'A', 'G'}
Closed set: {'S'}
Exploring neighbors of A:
Neighbor: B, weight: 2, h(B): 4
Added B to open set with g(B) = 3 and f(B) = 7
Neighbor: C, weight: 1, h(C): 2
Added C to open set with g(C) = 2 and f(C) = 4

Evaluating node: C (g: 2, h: 2, f: 4)
Open set: {'C', 'B', 'G'}
Closed set: {'S', 'A'}
Exploring neighbors of C:
Neighbor: D, weight: 3, h(D): 6
Added D to open set with g(D) = 5 and f(D) = 11
Neighbor: G, weight: 4, h(G): 0

Evaluating node: G (g: 6, h: 0, f: 6)
Open set: {'G', 'B', 'D'}
Closed set: {'S', 'A', 'C'}
Path found: ['S', 'A', 'C', 'G']

"""
