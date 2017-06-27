#include <iostream>

using namespace std;

int main(){
  // boolean variables (bool) are true or false. You can use these variables to
  // control the behavior of your program.
  bool thing1 = true;
  bool thing2 = false;

  // run this program to see the behavior of && (and)
  // try the other operators || (or) and ! (not)

  if(thing1 && thing2){
    cout << thing1 << endl;
  } else {
    cout << thing2 << endl;
  }

  // When you run this code you will get either a 0 for false
  // or a 1 for true. Does this remind you of binary at all?

  // Try replacing the statement in parentheses with 1 < 2. What happens?
  // You can use less than (<), greater than(>), equal to(==), not equal to(!=),
  // less than or equal to(<=), and greater than or equal to(>=)
  // in if statements.
}
