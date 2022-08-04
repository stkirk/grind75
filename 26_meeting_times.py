'''
Given an array of meeting times, intervals, consisting of start and end times
    # intervals = [[s1,e1], [s2,e2],... [si,ei],]
    # si < ei
# If a person could attend all the meetings:
    #   return True
    #   else return False
'''

def attend_all_meetings(interval):
    # sort by start time, interval[i][0]
    meetings = sorted(interval, key=lambda times: times[0])
    # loop through i in range(len(interval) - 2), if we check second to last meeting the last index is all good
    for i in range(len(meetings) - 1):
        # if end time of i > start time i+1 return False
        if meetings[i][1] > meetings[i+1][0]:
            return False
    
    return True

print(attend_all_meetings([[5,10], [0,30], [15,20]])) # False - conflict between [0,30] and the other two meetings
