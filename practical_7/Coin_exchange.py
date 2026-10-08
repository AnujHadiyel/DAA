def coin(N, coins):
    m = len(coins)
    dp = [[0] * (N + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = 1

    for i in range(1, m + 1):
        for j in range(1, N + 1):
            if j < coins[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = (
                    dp[i - 1][j]
                    + dp[i][j - coins[i - 1]]
                )

    return dp[m][N]


N = int(input("Enter target amount: "))
m = int(input("Enter number of coins: "))
coins = list(map(int, input("Enter coin values: ").split()))

result = coin(N, coins)

print("Number of ways =", result)