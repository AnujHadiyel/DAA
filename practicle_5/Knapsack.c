#include <stdio.h>

int max(int a, int b)
{
    if (a > b)
        return a;
    else
        return b;
}

int knapsack(int weight[], int value[], int n, int capacity)
{
    int dp[n + 1][capacity + 1];

    for (int i = 0; i <= n; i++)
    {
        for (int w = 0; w <= capacity; w++)
        {
            if (i == 0 || w == 0)
            {
                dp[i][w] = 0;
            }
            else if (weight[i - 1] <= w)
            {
                dp[i][w] = max(
                    value[i - 1] + dp[i - 1][w - weight[i - 1]],
                    dp[i - 1][w]
                );
            }
            else
            {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    return dp[n][capacity];
}

int main()
{
    int n, capacity;

    printf("Enter number of items: ");
    scanf("%d", &n);

    int weight[n], value[n];

    printf("Enter weights of items: ");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &weight[i]);
    }

    printf("Enter values of items: ");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &value[i]);
    }

    printf("Enter capacity of knapsack: ");
    scanf("%d", &capacity);

    int result = knapsack(weight, value, n, capacity);

    printf("Maximum value = %d\n", result);

    return 0;
}