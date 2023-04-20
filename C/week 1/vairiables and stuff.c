#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int i = 17;
    short s = 15;
    long l = 60;
    char c = 'a';


    printf("The number is %d. The size is %ld\n", i, sizeof(i));
    printf("The character is %c, the numeric value is %d, The size is %ld\n", c, c, sizeof(c));

    return EXIT_SUCCESS;
}

int nun(void) {
    int a[5];

    a[0] = 6;
    a[2] = 34;
    a[3] = 1234;
    a[4] = 4563;

    printf("%d %d %d %d %d\n", a[0], a[1], a[2], a[3], a[4]);

    char name[15] = "Harry";
    printf("The name is %s\n", name);

    return EXIT_SUCCESS;
}