#include <stdio.h>

int main() {
  int choice;

  do {
    printf("Please choose from the following items:\n");
    printf("1. T-shirt - $10\n");
    printf("2. Sunglasses - $20\n");
    printf("3. Backpack - $30\n");
    printf("4. Headphones - $40\n");
    printf("5. Sneakers - $50\n");
    printf("6. Exit");
    printf("Enter your choice (1-6): ");
    scanf("%d", &choice);

    switch(choice) {
      case 1:
        printf("\n");
        printf("You have selected a T-shirt. The price is $10.\n");
        printf("\n");
        break;
      case 2:
        printf("\n");
        printf("You have selected Sunglasses. The price is $20.\n");
        printf("\n");
        break;
      case 3:
        printf("\n");
        printf("You have selected a Backpack. The price is $30.\n");
        printf("\n");
        break;
      case 4:
        printf("\n");
        printf("You have selected Headphones. The price is $40.\n");
        printf("\n");
        break;
      case 5:
        printf("\n");
        printf("You have selected Sneakers. The price is $50.\n");
        printf("\n");
        break;
      case 6:
         printf("\n");
         printf("Thank you for coming\n");
         printf("\n");
      default:
        printf("\n");
        printf("Invalid choice. Please choose again.\n");
        printf("\n");
        break;
    }

  } while (choice != 6);

  return 0;
}
