/* Collin's Intro to C++
This section is called a comment. Put these throughout your code to describe
what you are doing!! Like we saw with assembly, a smattering of commands and
numbers are hard to read...comments help!

This program is designed to show you different features of C++ and be a starting
point for the rest of our C++ day.
*/

/* These are the preprocessor directives they start with a hashtag and allow
you to include files for now we are including iostream which allows us to read
from the keyboard and write to the screen*/

#include<iostream>

using namespace std; // This is another type of comment. The command to the left
                     // tells us about the namespaces we use for our program
                     // don't worry about namespaces for now just know this is
                     // here.
// The entry point for C++ programs is called the main function
// Every program needs a main function it is always int main(){}

int main(){
  int i_am_an_integer = 4;
  double i_have_a_decimal_point = 3.0;
  char i_am_a_letter = 'A';
  string i_am_a_sentence = "Hi! I'm a sentence.";
  cout << "Hello World!" << endl;
  return 0;
}
