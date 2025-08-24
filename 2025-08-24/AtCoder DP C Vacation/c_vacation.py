"""AtCoder DP C – Vacation"""


def vacation():
    """Main function"""

    n = int(input().strip())
    activities = [tuple(map(int, input().split())) for _ in range(n)]

    dp = [[0] * 3 for _ in range(n)]
    a1, b1, c1 = activities[0]
    dp[0] = [a1, b1, c1]

    for i in range(1, n):
        a, b, c = activities[i]
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + a
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + b
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + c

    print(max(dp[n - 1]))


if __name__ == "__main__":
    vacation()
