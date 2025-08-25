"""Checkposts"""


def main():
    """Main function"""
    n = int(input())
    costs = list(map(int, input().split()))

    m = int(input())

    g = [[] for _ in range(n)]
    gr = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        gr[v].append(u)

    # Step 1: order by finishing time (Kosaraju)
    visited = [False] * n
    order = []

    def dfs1(u):
        visited[u] = True
        for v in g[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)

    for i in range(n):
        if not visited[i]:
            dfs1(i)

    # Step 2: process in reverse order
    visited = [False] * n
    sccs = []

    def dfs2(u, comp):
        visited[u] = True
        comp.append(u)
        for v in gr[u]:
            if not visited[v]:
                dfs2(v, comp)

    for u in reversed(order):
        if not visited[u]:
            comp = []
            dfs2(u, comp)
            sccs.append(comp)

    total_cost = 0
    ways = 1

    for comp in sccs:
        min_cost = min(costs[u] for u in comp)
        count_min = sum(1 for u in comp if costs[u] == min_cost)
        total_cost += min_cost
        ways = ways * count_min

    print("")
    print(total_cost, ways)


if __name__ == "__main__":
    main()
