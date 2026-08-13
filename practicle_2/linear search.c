#include <stdio.h>

int main()
{
    int arr[100], n, key, i;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter elements: ");
    for(i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    printf("Enter element to search: ");
    scanf("%d", &key);

    for(i = 0; i < n; i++)
    {
        if(arr[i] == key)
        {
            printf("Element found at position %d", i + 1);
            return 0;
        }
    }

    printf("Element not found");

    return 0;
}