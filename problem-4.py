#A palindromic number reads the same both ways.  The largest palindrome made from the product 
#of two 2-digit numbers is 9009 = 91 x 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

from eulermath import is_palindromic_number
		
largest_palindrome = 0
for i in xrange(1000):
	for j in xrange(1000):
		temp = i*j
		if is_palindromic_number(temp):
			if temp > largest_palindrome:
				largest_palindrome = temp
print str(largest_palindrome)