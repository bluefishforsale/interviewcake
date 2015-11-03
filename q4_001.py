#!/usr/bin/python
# condense_meeting_times
#  takes a list of meeting time ranges and returns a list of condensed ranges.
# eg:
# input = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
# output = [(0, 1), (3, 8), (9, 12)]

def condense_meeting_times(times):
    # show what the imput times were
    print times

    # create an empty list for merged times
    merged_times = []

    # put all meetings in order by start time
    times.sort()

    # start one meeting window
    start =  times[0][0]
    end =  times[0][1]

    for i in range(1, len(times)):
        # if the current meeting being inspected
        # starts before the original one ends
        # set the new end time to the current meetings
        mystart = times[i][0]
        myend = times[i][1]
        if mystart <= end:
            if myend > end:
                end = myend
        # otherwise, add the original meeting to the list
        # then adjust the new start and end times
        else:
            merged_times.append((start, end))
            start = mystart
            end = myend

    # The edgepost cases of
    # last meeting
    # all time ranges overlap
    merged_times.append((start, end))

    return merged_times


# testing different inputs to the function
# Desired result:
#   [(0, 1), (3, 8), (9, 12)]
times = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
print condense_meeting_times(times)
print

# Desired result:
#   [(0, 12)]
times = [(0, 1), (0, 12), (2, 4), (3, 5), (3, 10), (4, 8), (9, 10), (10, 12)]
print condense_meeting_times(times)
print

# Desired result:
#   [(0, 7), (8, 9)]
times = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (8, 9)]
print condense_meeting_times(times)
print

# Desired result:
#   [(1, 5)]
times = [(1, 5), (2, 3)]
print condense_meeting_times(times)
