#!/usr/bin/python

def merge(a,b):
	i = 0
	j = 0
	output = []
	length = len(a) + len(b)
	for x in xrange(0, length):
		if i < len(a) and (j >= len(b) or a[i] < b[j]):
			output.append(a[i])
			i = i + 1
		else:
			output.append(b[j])
			j = j + 1
	return output

def merge_sort(n):	
	length = len(n)
	middle = length / 2

	if length == 1:
		return n
	elif length == 2:
		if n[0] < n[1]:
			return n
		else:
			return [n[1], n[0]]

	a = merge_sort(n[:middle])
	b = merge_sort(n[middle:])
	return merge(a, b)
	
n = [3,2,1,6,7,4]
m = len(n) /2
print merge_sort(n)