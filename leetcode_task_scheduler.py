"""
A: 0
B: 1
C: 0

cooldown: 5

greedy algorithm:
    1. among those not subject to the cooldown, choose the one with largest number of remaining tasks of the same type
    2. among those that ARE subject to the cooldown, select based on how long its been since the last tasks of their type

Choose 1. when possible, and 2. when not.

    O(n log n)

assume that there are more B's than A's and that this is an optimal solution:
A B ..... B ... A ...
if you do this:
B A ..... B ... A ...
you do no worse since at the worst, you can deduct 1 second due to the change for B and add one second due to A

Assume this is an optimal solution:
A B ..... B ... A ...
q r       s     t
Then if you change it to this:
A B ..... A ... B ...
q r       s     t
you do no worse and possibly better since originally, the penalty is max(0, cooldown - (t-q) + 1) + max(0, cooldown - (s-r) + 1).
The penalty for the modified order is max(0, cooldown - (s-q) +1) + max(0, cooldown - (t-r) + 1)

Since q < r < s < t:

    s - q < t - q
    and
    s - r < t - r

Thus, in the worst case (i.e. when both types of tasks in both arrangements are susceptible to the cooldown),

    cooldown - t + q + 1 + cooldown - s + r + 1 = cooldown - (s-q) +1 + cooldown - (t-r) + 1
->  - t + q - s + r = -s + q - t + r



B A C B A B:
 1 2 3 7 8 13

B A C A B B:
 1 2 3 8 9 15

B A B C A B:
 1 2 7 8 9 13

heaps?

maxheap of number of instances of tasks of a particular type
minheap of time since the last task of that kind





"""
