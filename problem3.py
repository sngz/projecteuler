import sys
sys.setrecursionlimit(1000000)

def maxPrimeFact(num, divider):
	if (num != 1):
		if (num % divider == 0):
			num = num / divider
			return maxPrimeFact(num, divider)
		else:
			divider+=1
			return maxPrimeFact(num, divider)
	else:
		print divider
		return num


print maxPrimeFact(600851475143, 2)