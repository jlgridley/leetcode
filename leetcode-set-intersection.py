"""
Max:
No overlapping intervals: # of intervals * 2
Min:
All overlap same 2 numbers: 2

only 2 intervals:

1 number overlaps: 3
2 numbers overlap: 2

naive solutions:
iterate over every single combination of 2, 3, 4,... numbers within intervals
backtracking?
    start with smaller intervals first?

Can ignore intervals that completely eclipse other intervals

recurse on disconnected components?

sort by first value

cases:
no overlap
1 overlap
>=2 overlap


"""
