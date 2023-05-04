#include <stdio.h>

int minimum(int a, int b) {
  if (a < b) {
    return a;
  } else {
    return b;
  }
}

int main() {
  int num1, num2;
  printf("Enter two numbers: ");
  scanf("%d %d", &num1, &num2);

  int min = minimum(num1, num2);
  printf("The minimum value is %d\n", min);

  return 0;
}
