#include <iostream>
using namespace std;
int main() {
  int integer = 0;
  cout << integer << endl;

  bool boolean = true;
  cout << boolean << endl;

  float floating = 0.0;
  cout << floating << endl;

  double double_precision = 0.0;
  cout << double_precision << endl;

  char character = 'a';
  cout << character << endl;

  int array[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

  for (int i : array) {
    cout << i << " ";
  }
  cout << endl;

  char string[] = "Hello World!";
  cout << string << endl;
  cout << endl;

  int *pointer = &integer;
  cout << pointer << " " << *pointer << endl;
}
