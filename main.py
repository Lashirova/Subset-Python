
def Subsets(arr, n, val, sum) :
	if (sum == 0) :
		for value in val :
			print(value, end=" ")
		print()
		return
	if (n == 0):
		return
	Subsets(arr, n - 1, val, sum)
	v1 = [] + val
	v1.append(arr[n - 1])
	Subsets(arr, n - 1, v1, sum - arr[n - 1])

def AllSubsets(arr, n, sum):
	val = []
	Subsets(arr, n, val, sum)

arr = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]
sum = 23
n = len(arr)
AllSubsets(arr, n, sum)
