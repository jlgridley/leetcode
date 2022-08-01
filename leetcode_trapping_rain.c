#include <stdio.h>
#include <stdlib.h>

/*

Find the two greatest numbers at indices i, j in the array.
total += min(height[i], height[j]) * (j-i-1)
for k in i...j:
	total -= height[k]

return total + height[0,i] + height[j,n]

test cases:
{}
{4}
{1, 3}
{1, 2, 1} => 0
{2, 0, 3} => 2
{2, 0, 2} => 2
{1, 2, 1, 2, 0, 3} => 3
{3, 2, 0} => 0
{4, 1, 2, 0, 2} => 3
{3, 0, 1, 0, 2} => 5
{1, 0, 5, 5, 2} => 1
*/

int get_trapped_area(int* height, int heightSize) {
	if (heightSize <= 2) {
		return 0;
	}
	int highest = -1;
	int highest_index = -1;
	for (int i = 0; i < heightSize; i++) {
		if (height[i] > highest) {
			highest = height[i];
			highest_index = i;
		}
	}
	int second_highest = -1;
	int second_highest_index = -1;
	for (int i = 0; i < heightSize; i++) {
		if (i < highest_index) {
			if (height[i] >= second_highest) {
				second_highest = height[i];
				second_highest_index = i;
			}
		} else if (i > highest_index) {
			if (height[i] > second_highest) {
				second_highest = height[i];
				second_highest_index = i;
			}
		}
	}
	if (highest == -1 || highest_index == -1 || second_highest == -1 || second_highest_index == -1) {
		return -1;
	}
	if (second_highest_index > highest_index) {
		int total = (second_highest_index - highest_index - 1) * second_highest;
		for (int i = highest_index + 1; i < second_highest_index; i++) {
			total -= height[i];
		}
		int right = get_trapped_area(height, highest_index + 1);
		int left = get_trapped_area(height + second_highest_index, heightSize - second_highest_index);
		return total + right + left;
	} else {
		int total = (highest_index - second_highest_index - 1) * second_highest;
		for (int i = second_highest_index + 1; i < highest_index; i++) {
			total -= height[i];
		}
		int right = get_trapped_area(height, second_highest_index + 1);
		int left = get_trapped_area(height + highest_index, heightSize - highest_index);
		if (right == -1 || left == -1) {
			return -1;
		}
		return total + right + left;
	}
}

int main() {
	int height[] = {1, 0, 5, 5, 2};
	int heightSize = 5;
	printf("%d\n", get_trapped_area(height, heightSize));
	return 0;
}
