"""Single source shortest path, non-negative weights"""

from queue import PriorityQueue


def main():
    """Single source shortest path, non-negative weights : main function"""
    while True:
        textline_1 = input().split(" ")
        n = int(textline_1[0])
        m = int(textline_1[1])
        q = int(textline_1[2])
        s = int(textline_1[3])

        edges = []
        for _ in range(m):
            edge = input().split(" ")
            edges.append((int(edge[0]), int(edge[1]), int(edge[2])))

        queries = []
        for _ in range(q):
            queries.append(int(input()))

        graph = {v: [] for v in range(0, n)}
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        dist = {v: float("inf") for v in graph}
        dist[0] = 0
        visited = set()
        pq = PriorityQueue()

        pq.put((0, s))

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
        for _ in range(q):
            if dist[queries[_]] == float("inf"):
                print("Impossible")
            else:
                print(dist[queries[_]])


if __name__ == "__main__":
    main()
