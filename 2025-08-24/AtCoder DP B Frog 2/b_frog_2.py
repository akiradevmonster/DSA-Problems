"""AtCoder DP B : Frog 2"""


def main():
    """AtCoder DP B : Frog 2"""

    input_1 = input().split()
    n = int(input_1[0])
    k = int(input_1[1])
    h = list(map(int, input().split()))
    dp = [float("inf")] * n
    dp[0] = 0

    for i in range(1, n):
        for j in range(1, k + 1):
            if i - j >= 0:
                dp[i] = min(dp[i], dp[i - j] + abs(h[i] - h[i - j]))

    print(dp[n - 1])


if __name__ == "__main__":
    main()
