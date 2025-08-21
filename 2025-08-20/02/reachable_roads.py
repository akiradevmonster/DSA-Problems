"""Kattis : Reachable Roads"""


def main():
    """Main Function"""
    city_number = int(input())

    i = 0
    while i < city_number:
        road_endpoint = int(input())
        r = int(input())
        road = []
        j = 0
        while j < r:
            roadtemp = list(map(int, input().split(" ")))
            road.append([roadtemp[0], roadtemp[1]])
            j += 1

        total_count = 0

        # main search logic
        for k in range(road_endpoint - 1):
            useful = False
            for val in road:
                if (val[0] == k and val[1] == k + 1) or (
                    val[1] == k and val[0] == k + 1
                ):
                    useful = True
            if not useful:
                total_count += 1
        print(total_count)
        i += 1


if __name__ == "__main__":
    main()
