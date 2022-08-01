import java.lang.Math;

class Interval {

    int start;
    int end;
    int height;
    int index;

    public Interval(int currStart, int currEnd, int currHeight, int currIndex) {
        start = currStart;
        end = currEnd;
        height = currHeight;
        index = currIndex;
    }
}

class Solution {
    public List<Integer> fallingSquares(int[][] positions) {
        // TreeSet intervalTree = new TreeSet();
        List<Interval> intervalList = new ArrayList<Interval>();
        List<Integer> heights = new ArrayList<Integer>();
        Interval initialInterval = new Interval(0, 100000000, 0, 0);
        int currHighest = 0;

        for (int[] position : positions) {
            side_length = position[1];
            for (Interval interval : intervalList) {
                if (interval.start <= position[0]) {
                    if (interval.end > position[0]) {
                        if (interval.end > position[0] + side_length) {

                        } else {

                        }
                    }
                }
            }
            // cases: start < position[0], end <= position[0]
            //              keep looking
            //        start < position[0], position[0] < end < position[0] + side_length
            //              need to split up this interval
            //              need to find intervals until end >= position[0] + side_length
            //              if last interval end > position[0] + side_length, split that interval
            //              else, update height
            //              delete all unnecessary intervals
            //        start < position[0], end == position[0] + side_length
            //              split up this interval
            //        start == position[0], position[0] < end < position[0] + side_length
            //              update height of this interval
            //              find end of position[0] + side_length as above
            //        start == position[0], end == position[0] + side_length
            //              update height of this interval
            //        start == position[0], end > position[0] + side_length
            //              split this interval
            //        position[0] < start < position [0] + side_length, position[0] < end < position [0] + side_length
            //              this should never happen, because you'll have found a start before this one

        }
        return heights;
    }
}


/*
Test cases:
[0, 1], [1, 1], [4, 1], [20, 10] -> [1, 1, 1, 10]
[90000000, 10000000] -> [10000000]
[4, 1], [20, 10], [1, 1], [0, 1] -> [1, 10, 10, 10]

*/
