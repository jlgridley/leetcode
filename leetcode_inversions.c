/*
local is linear (just go through it once)

naive version of global:
n^2: for each number, go through the whole list

base case (N == 2):
local inversion

base case + 1:
local inversion plus previous space's local inversion
(just global inversion for last element)

2 1 0
1 2 0

space n

###i####n

i <= n
do nothing

i > n
1 + i's global inversions

keep track of greatest number seen so far?

0   1   1 ... 1   0
900 1   2 ... 899 901 3
900 900 900   900 901

3 1 2 0
local: 2
global: 5

1 0 3 2 5 4

0 1 2 3 4 5 6 7 8 9
0 2 1 3 5 4 7 8 9 6

*/
#include <stdio.h>
#include <stdlib.h>

int main() {
	/* For each number i:
		if A[i] > i + 1 or A[i] < i - 1:
			return false
		return true
	*/
	int A[] = {0, 2, 1, 3, 5, 4, 6, 7, 9, 8};
	int ASize = 10;
	for (int i = 0; i < ASize; i++) {
		if (A[i] > i + 1 || A[i] < i - 1) {
			printf("false\n");
			return 0;
		}
	}
	printf("true\n");
	return 0;
}
