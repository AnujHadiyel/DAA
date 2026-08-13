#include <stdio.h>

int main()
{
    int arr[5], i, j, num;

    printf("Enter 5 elements:\n");

    for(i = 0; i < 5; i++)
    {
        scanf("%d", &arr[i]);
    }

    // Insertion Sort
    for(i = 1; i < 5; i++)
    {
        num = arr[i];
        j = i - 1;

        while(j >= 0 && arr[j] > num)
        {
            arr[j + 1] = arr[j];
            j--;
        }

        arr[j + 1] = num;
    }

    printf("Sorted Array:\n");

    for(i = 0; i < 5; i++)
    {
        printf("%d ", arr[i]);
    }

    return 0;
}