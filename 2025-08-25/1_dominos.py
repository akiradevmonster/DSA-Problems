"""Dominos"""


def solve():
    """Dominos Main function"""
    t = int(input().strip())

    for _ in range(t):
        n, m = map(int, input().split())

        graph = [[] for _ in range(n + 1)]
        reverse_graph = [[] for _ in range(n + 1)]

        for _ in range(m):
            x, y = map(int, input().split())
            graph[x].append(y)
            reverse_graph[y].append(x)

        visited = [False] * (n + 1)
        order = []

        # First DFS - store finishing order
        def dfs1(u):
            visited[u] = True
            for v in graph[u]:
                if not visited[v]:
                    dfs1(v)
            order.append(u)

        for u in range(1, n + 1):
            if not visited[u]:
                dfs1(u)

        # Second DFS - assign SCC ids
        visited = [False] * (n + 1)
        scc_id = [0] * (n + 1)
        current_id = 0

        def dfs2(u, id):
            visited[u] = True
            scc_id[u] = id
            for v in reverse_graph[u]:
                if not visited[v]:
                    dfs2(v, id)

        while order:
            u = order.pop()
            if not visited[u]:
                current_id += 1
                dfs2(u, current_id)

        # Build DAG and calculate indegrees
        indegree = [0] * (current_id + 1)

        for u in range(1, n + 1):
            for v in graph[u]:
                if scc_id[u] != scc_id[v]:
                    indegree[scc_id[v]] += 1

        # Count SCCs with no incoming edges
        answer = sum(1 for i in range(1, current_id + 1) if indegree[i] == 0)
        print(answer)


# Run if executed directly
if __name__ == "__main__":
    solve()
