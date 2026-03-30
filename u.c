#include <stdio.h>
#include <math.h>

int main() {
    int num = 153, original, sum = 0, rem, n = 0;

    original = num;

    // count digits
    while(original != 0) {
        original /= 10;
        n++;
    }

    original = num;

    while(num != 0) {
        rem = num % 10;
        sum += pow(rem, n);
        num /= 10;
    }

    if(sum == original)
        printf("Armstrong Number");
    else
        printf("Not Armstrong");

    return 0;
}