#!/usr/bin/env python3

def crackSafe(n, k):
	"""
	:type n: int
	:type k: int
	:rtype: str
	"""

	pw_str = '0' * n
	num_done = 1
	done = set()
	done.add(pw_str)
	return crackSafeRecursive(n, k, done, num_done, pw_str)



def crackSafeRecursive(n, k, done, num_done, pw_str):
	"""
	Base case:
	num_done == k^n
	return pw_str

	for i in range(k):
		tack on i and see if the string of the last n chars is in done
		if not, call the recursive function with this new string
		if the recursive call returns with a string, return the string
		otherwise, continue

	return -1
	"""
	if num_done == pow(k, n):
		return pw_str
	for i in range(k):
		new_str = pw_str + str(i)
		window = new_str[-n:]
		if window not in done:
			done.add(window)
			num_done += 1
			res = crackSafeRecursive(n, k, done, num_done, new_str)
			if res != -1:
				return res
			else:
				done.remove(window)
				num_done -= 1
	return -1

print(crackSafe(2, 3))
