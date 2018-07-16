# Python 3 Program to
# find nth term of 
# Arithmetic progression
 
def Nth_of_AP(a, d, N) :
 
	# using formula to find the 
	# Nth term t(n) = a(1) + (n-1)*d
	return (a + (N - 1) * d)
 
 
# Driver code
a = 2 # starting number
d = 1 # Common difference
N = 5 # N th term to be find
 
# Display the output
print( "The ", N ,"th term of the series is : ",
	Nth_of_AP(a, d, N))
 
 
 
# This code is contributed
# by Nikita Tiwari.# your code goes here
