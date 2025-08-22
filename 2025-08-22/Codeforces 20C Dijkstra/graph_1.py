"""Codeforces 20C Dijkstra"""

from queue import PriorityQueue


def main():
    """Main function"""
    input_1 = input().split(" ")
    n = int(input_1[0])
    m = int(input_1[1])

    edges = []
    for _ in range(m):
        edge = input().split(" ")
        edges.append((int(edge[0]), int(edge[1]), int(edge[2])))

    graph = {v: [] for v in range(1, n + 1)}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    dist = {v: float("inf") for v in graph}
    dist[1] = 0
    visited = set()
    pq = PriorityQueue()

    pq.put((0, 1))

    while not pq.empty():
        (_, u) = pq.get()
        if u in visited:
            continue
        visited.add(u)

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pq.put((dist[v], v))

    print(dist)


if __name__ == "__main__":
    main()
