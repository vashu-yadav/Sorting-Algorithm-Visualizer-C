#include <stdio.h>

int main() {
    FILE *fp;

    fp = fopen("test.txt", "w");

    if(fp == NULL) {
        printf("File not opened");
        return 1;
    }

    fprintf(fp, "Hello, this is file handling in C.");

    fclose(fp);

    printf("Data written to file");

    return 0;
}