#include <stdio.h>

int main() {
    int num = 121, original, reverse = 0, rem;
    original = num;

    while(num != 0) {
        rem = num % 10;
        reverse = reverse * 10 + rem;
        num /= 10;
    }

    if(original == reverse)
        printf("Palindrome");
    else
        printf("Not Palindrome");

    return 0;
}