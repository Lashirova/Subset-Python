
def Subsets(arr, n, v, sum) :
	if (sum == 0) :
		for value in v :
			print(value, end=" ")
		print()
		return
	if (n == 0):
		return
	Subsets(arr, n - 1, v, sum)
	v1 = [] + v
	v1.append(arr[n - 1])
	Subsets(arr, n - 1, v1, sum - arr[n - 1])

def AllSubsets(arr, n, sum):
	v = []
	Subsets(arr, n, v, sum)

arr = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]
sum = 23
n = len(arr)
AllSubsets(arr, n, sum)
