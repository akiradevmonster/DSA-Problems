"""Kattis : Reachable Roads"""

city_number = int(input())
for i in range(city_number):
    road_endpoint = int(input())
    r = int(input())
    road = []
    for j in range(r):
        road = list(map(int, input().split(" ")))

    useless_endpoint = []
    for k in range(r):
        total_count = 0
        for val in enumerate(road):
            if val[0] == k or val[1] == k:
                total_count += 1
        if total_count < 2:
            useless_endpoint.append(k)
    print(len(useless_endpoint) - 1)

# This problem is not completed yet.
