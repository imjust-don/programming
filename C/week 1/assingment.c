#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int i = 0;
    char name[20];

    printf("Please enter a number: ");
    scanf("%d", &i);
    printf("Your number is %d\n", i);
    printf("Please enter a name: ");
    scanf("%s", name);
    printf("The name you entered is %s\n", name);


    return EXIT_SUCCESS;
}
