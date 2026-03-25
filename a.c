#include<stdio.h>

void display(int a[], int n) {
    for(int i=0;i<n;i++){
        printf("%d",a[i]);
    }
    printf("\n");
}

void bubble(int a[], int n){
    for(int i=0;i<n-1;i++){
        printf(" Pass %d:\n ", i+1 );
        for(int j=0; j<n-i-1; j++){
            if(a[j]>a[j+1]){
                int t=a[j];
                a[j]=a[j+1];
                a[j+1]=t;
            }
            display(a,n);
        }
        printf("\n");

    }
}
void selection(int a[], int n){
    for(int i=0; i<n-1; i++){
        int min = i;
        for(int j=i+1; j<n; j++){
            if(a[j]<a[min]){
                min = j;
            }
        }
        int t=a[i];
        a[i]=a[min];
        a[min]=t;

        printf(" step %d: ", i+1 );
        display(a,n);

    }
}

int main(){
    int s;
    printf("Enter the size of array: ");
    scanf("%d", &s);
    int a[s];
    int n=5;
    for(int i=0;i<n;i++){
        printf("Enter the elements: ");
        scanf("%d",&a[i]);
    }
    printf(" Original Array:\n ");
    display(a,n);

    bubble(a,n);

    return 0;


}