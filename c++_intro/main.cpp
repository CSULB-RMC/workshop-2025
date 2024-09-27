#include <iostream>
using namespace std;
class C{
  public:
    string pub = "Public Variable: 4321";
    C(string p){
      priv = p;
    }
    void getPrivate(){
      cout << priv << endl;
    }
  private:
    string priv;
};

int main() {
  int integer = 0;
  cout << integer << endl;

  bool boolean = true;
  cout << boolean << endl;

  float floating = 0.2;
  cout << floating << endl;

  double double_precision = 0.1;
  cout << double_precision << endl;

  char character = 'a';
  cout << character << endl;

  int array[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

  for (int i : array) {
    cout << i << " ";
  }
  cout << endl;

  string str = "Hello World!";
  cout << str << endl;
  cout << endl;

  int *pointer = &integer;
  cout << pointer << " " << *pointer << endl;

  char charArray[] = "Bye World";
  char *ptr = charArray;
  //ptr++;
  cout << pointer << " " << *ptr << endl;

  C myClass("Private: 1234");

  cout << myClass.pub << endl;

  myClass.getPrivate();
}
