#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int i = 0;
    char name[20];

    printf("\n");
    printf("Please enter a number: ");
    scanf("%d", &i);
    printf("\n");
    printf("Your number is %d\n", i);
    printf("\n");
    printf("Please enter a name: ");
    scanf("%s", name);
    printf("The name you entered is %s\n", name);
    printf("\n");

    int num1, num2;
    printf("Enter two numbers: ");
    scanf("%d %d", &num1, &num2);

    if (num1 < num2) {
        printf("%d is the minimum value.\n", num1);
    }
    else {
        printf("%d is the minimum value.\n", num2);
    }

    float num;
    printf("Enter a floating point value: ");
    scanf("%f", &num);

    printf("-----------------------------\n");
    printf("Scientific notation: %e\n", num);
    printf("Fixed point notation: %f\n", num);
    printf("Shortest representation: %g\n", num);
    printf("-----------------------------\n");

    return EXIT_SUCCESS;
}
