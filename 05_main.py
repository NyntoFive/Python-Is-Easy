'''
Python is Easy Homework #5: Basic Loops
Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".

Extra Credit:

Instead of only printing "fizz", "buzz", and "fizzbuzz", add a fourth print statement: "prime".
You should print this whenever you encounter a number that is prime (divisible only by itself and one).
As you implement this, don't worry about the efficiency of the algorithm you use to check for primes.
It's okay for it to be slow.
'''



def fizzyBuzzer():
    for num in range(100):
        if num % 3 == 0 and num % 5 == 0: #FizzBuzz
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        elif isPrime(num) == True:
            print("prime")
        else:
            print(num)

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

fizzyBuzzer()
