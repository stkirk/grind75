'''
Given an array of non overlapping intervals, intervals:
    - intervals[i] = [starti, endi]
    - intervals[i] represents the start and end of the ith interval
Also Given a newInterval [start, end]
    - Insert newInterval into intervals, such that intervals is still sorted in ascending order by starti
    - AND intervals does not have any overlapping intervals
    - if intervals overlap, merge them together as 1 new interval
Return intervals after insertion
'''
# overlapping means even if the endi == starti+1, those must be merged too
def insert_interval(intervals, newInterval):
    # add new interval to intervals
    # sort intervals in place
    intervals.append(newInterval)
    intervals.sort(key=lambda interval: interval[0])
    merged = []
    # edge case if we're given an empry list of intervals
    if len(intervals) == 1:
        return intervals
    for i in range(1, len(intervals)):
        cur = intervals[i]
        prev = intervals[i-1]
        # look back 1 index, if [i-1][1] < i[0] and [i-1][1] < i[1]:
        if prev[1] < cur[0] and prev[1] < cur[1]:
            # append [i-1] to merged 
            merged.append(prev)
            
        # elif [i-1][1] >= i[0]:
        # could be elif prev[1] >= cur[0]
        else:
            # reset i's values
            # [i][0] = [i-1][0]
            cur[0] = prev[0]
            #max if [i][1] < [i-1][1]:
                # [i][1] = [i-1][1]
            cur[1] = max(prev[1], cur[1])

        # if last index, append it, either i-1 has appended - meaning i is good or i-1 wasn't appended i is transformed and can't conflict with any other idex
        if i == len(intervals)-1:
            merged.append(cur)

    return merged



print(insert_interval([[1,3],[6,9]], [2,5])) # [[1,5],[6,9]]
print(insert_interval([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])) # [[1,2],[3,10],[12,16]]
# first step [[1,2],[3,5],[4,8],[6,7],[8,10],[12,16]]
print(insert_interval([], [5,7])) # [[5,7]]
