from __future__ import print_function

def first(elem):
    return elem.start

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
    merged = []
    intervals.sort(key=first)
    l = len(intervals)
    i = 0
    while i < l-1:
        if intervals[i].end < intervals[i+1].start:
            merged.append(intervals[i])
            i += 1
        else:
            intervals[i+1].start = intervals[i].start
            intervals[i+1].end = max(intervals[i].end, intervals[i+1].end)
            i += 1
    
    merged.append(intervals[l-1])
    
    return merged
 
    
    
def main():
    print([1, 4], [2, 5], [1, 2], [7, 9])
    intervals = [Interval(1, 4), Interval(2, 5), Interval(1, 2), Interval(7, 9)]
    print("Merged intervals: ")
    for i in merge(intervals):
        i.print_interval()
    print()
    print('--------------')
    
    print([6, 7], [2, 4], [5, 9])
    intervals2 = [Interval(6, 7), Interval(2, 4), Interval(5, 9)]
    print("Merged intervals: ")
    for i in merge(intervals2):
        i.print_interval()
    print()
    print('--------------')
    
    print([1, 4], [2, 6], [3, 5])
    intervals3 = [Interval(1, 4), Interval(2, 6), Interval(3, 5)]
    print("Merged intervals: ")
    for i in merge(intervals3):
        i.print_interval()
    print()
    print('--------------')
    
main()