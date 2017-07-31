# This is a class. It is a bigger grouping of code than a function and it is
# used to store both variables and functions that work together. Classes are
# often used in code to store and retrieve related information and describe
# complex objects in code. For example, a class to represent a car would have
# variables for the number of wheels and the maximum speed and functions such as
# drive and turn on. These variables and functions could then be used to create
# an object that behaves in code the way a car might behave in real life.
#
#
# Below is a class for a fighter in a game. I have written some examples for you
# and have marked the places where I want you to add additional things to the
# class. We'll start with the class for now and eventually make a game where
# two fighters duke it out for ultimate superiority.

class Fighter(object):
    def __init__(self, name, attack, armor):
        # variables that exist in classes are denoted by the term self.<variable>
        # where <variable is the name of the variable. The below code sets the
        # fighter's name to the name passed into the init function.
        self.name = name

        # Using the example above, complete the following code
        self.attack =

        # now that you've set the fighter's name and attack, create a variable
        # below this comment that sets the fighter's armor to the armor passed
        # into the function.
        

# Below is an example of how we would declare a variable as a fighter
# notice how the Fighter line does not say self? We don't need to include it!
# Python does that for us
fighter1 = Fighter("Steve", 10, 3)

 # class variables are referenced by doing <class>.<variable> where class
 # is the name of the variable representing the class and variable is the class
 # variable we want to reference
 print(fighter1.name)

# Add a second fighter below this comment we are going to be creating a method to
# make the fighters fight together. If you are done before everyone else, go
# through gameplan or work on either the Guess the Weight game or your Madlib/Text Adventure
