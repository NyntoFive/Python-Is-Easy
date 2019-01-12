"""
Homework #1: Variables
  I want to assign song statistics to variables and print them out
  I'll use global variables and then print them individually.

"""

# Variables

songTitle = "So Long, and Thanks for All the Fish"  #string
artist = "A Perfect Circle"
album = "Eat the Elephant"
length = 4.26  # float
releaseYear = 2018  # int
genre = "Rock"  # string


# print the variables
print("Title: " + songTitle)
print('Artist: ' + artist)
print("Album: " + album)
print("Length: " + str(length) + " minutes")  # I had to use str() to print this float variable as a string.
print("Release Year: " + str(releaseYear))  # I had to use str() to print this integer as at string.
print("Genre: " + genre)
