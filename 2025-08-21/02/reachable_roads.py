"""Kattis : Reachable Roads"""

city_number = int(input())
for i in range(city_number):
    road_endpoint = int(input())
    r = int(input())
    for j in range(r):
        road = list(map(int, input().split(" ")))
    for k in range(len(road)-1):
        