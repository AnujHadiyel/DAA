#include <stdio.h>

int factorial(int n)
{
    int fact = 1;
    int i;

    for(i = 1; i <= n; i++)
    {
        fact = fact * i;
    }

    return fact;
}

int main()
{
    int n, result;

    printf("Enter a number: ");
    scanf("%d", &n);

    result = factorial(n);

    printf("Factorial = %d", result);

    return 0;
}