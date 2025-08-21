"""Kattis : Reachable Roads"""

city_number = int(input())

for i in range(city_number):
    road_endpoint = int(input())
    r = int(input())
    road = []
    for j in range(r):
        roadtemp = list(map(int, input().split(" ")))
        road.append([roadtemp[0], roadtemp[1]])

    total_count = 0
    for k in range(road_endpoint - 1):
        useful = False
        for val in road:
            if (val[0] == k and val[1] == k + 1) or (val[1] == k and val[0] == k + 1):
                useful = True
        if not useful:
            total_count += 1
    # for k in range(r):
    #     total_count = 0
    #     for val in enumerate(road):
    #         if val[0] == k or val[1] == k:
    #             total_count += 1
    #     if total_count < 2:
    #         useless_endpoint.append(k)
    print(total_count)

# This problem is completed now.
