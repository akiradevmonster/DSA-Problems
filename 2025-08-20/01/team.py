"""A. Team"""


def main():
    """Main function to solve the Team problem."""
    count = int(input())

    total_count = 0
    index = 0
    while index < count:
        solution = input()
        result = solution.count("1")
        if result >= 2:
            total_count += 1
        index += 1

    print(total_count)


if __name__ == "__main__":
    main()
