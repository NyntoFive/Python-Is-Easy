'''
Homework Python-Is-Easy-#02 Functions

Let's return to the music example from assignment one. Pick 3 of the attributes you listed. 
For our example we're going to say "Genre", "Artist" and "Year". 
Create a new Python file and create 3 functions with the same name as those attributes.
So in this example we'd have one function named "genre" another named "artist" and another called "year".

When someone calls any of those functions, that function should return the corresponding value for that attribute. 
For example, if we call the "Artist" function our function would return "Dave Brubeck".
Yours should return whatever values make sense for your music choice.


Extra Credit:

One of the data types we haven't covered yet is called "booleans".
 When a variable is set to True or False, that's a boolean. 
 For extra credit, see if you can figure out how to use booleans,
 and add an extra function that returns a boolean value instead of a String or Number.

Hint: make sure to capitalize the first letter in the words True or False when you use them. 
 We'll cover booleans more in the lecture on "if" statements coming up next in the course.
'''


def songTitle():  # string
    songTitle = "So Long, and Thanks for All the Fish"
    return songTitle


def artist():  # string
    artist = "A Perfect Circle"
    return artist


def length():  # float
    length = 4.26
    return length


def isArtistCheck():  # Boolean
    if artist() == "A Perfect Circle":
        return True
    else:
        return False


def main():  # Print the return values with some concatenation
    print()
    print("Title: " + songTitle())
    print("Artist: " + artist())
    print("Length: " + str(length()))
    print("Is Artist True or False? " + str(isArtistCheck()))

def simple_main():  # prints return values only
    print()
    print(songTitle())
    print(artist())
    print(length())
    print(isArtistCheck())


main()
simple_main()