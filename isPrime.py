#### to check long integers prime
from math import sqrt; from itertools import count, islice
def isPrime(number):
	return number > 1 and all(number%i for i in islice(count(2), int(sqrt(number)-1)))
  
