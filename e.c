#include <stdio.h>

int main() {
    int arr[10] = {10, 20, 30, 40, 50};
    int n = 5, i;

    // Insertion: insert 25 at index 2
    for(i = n; i > 2; i--) {
        arr[i] = arr[i-1];
    }
    arr[2] = 25;
    n++;

    // Array after insertion
    printf("After Insertion: ");
    for(i = 0; i < n; i++)
        printf("%d ", arr[i]);

    // Deletion: delete element at index 4
    for(i = 4; i < n-1; i++) {
        arr[i] = arr[i+1];
    }
    n--;

    // Array after deletion
    printf("\nAfter Deletion: ");
    for(i = 0; i < n; i++)
        printf("%d ", arr[i]);

    return 0;
}