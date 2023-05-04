#include <stdio.h>

#define SIZE 10

int main() {
  float values[SIZE];
  float sum = 0, max = 0, min = 0;

  // Get input values from user
  for (int i = 0; i < SIZE; i++) {
    printf("Enter a value: ");
    scanf("%f", &values[i]);

    // Calculate sum
    sum += values[i];

    // Update max and min values
    if (i == 0 || values[i] > max) {
      max = values[i];
    }

    if (i == 0 || values[i] < min) {
      min = values[i];
    }
  }

  // Calculate average
  float avg = sum / SIZE;

  // Print results
  printf("Minimum value: %.2f\n", min);
  printf("Maximum value: %.2f\n", max);
  printf("Average value: %.2f\n", avg);


  for (int i = 1; i <= 10; i++) {
  printf("%d\n", i);
  }
  
  for (int i = 10; i >= 1; i--) {
  printf("%d\n", i);
  }

  return 0;
}



