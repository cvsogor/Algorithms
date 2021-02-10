start, end = 0, 1
def first(elem):
    return elem[start]

def merge(intervals):
    merged = []
    intervals.sort(key=first)
    l = len(intervals)
    i = 0

    while i < l-1:
        if intervals[i][end] < intervals[i+1][start]:
            merged.append(intervals[i])
            i += 1
        else:
            intervals[i+1][start] = intervals[i][start]
            intervals[i+1][end] = max(intervals[i][end], intervals[i+1][end])
            i += 1
    
    merged.append(intervals[l-1])
    
    return merged
 
    
    
def main():
    intervals = [[1, 4], [2, 5], [1, 2], [7, 9]]
    print(intervals)
    print("Merged intervals: ")
    print(merge(intervals))
    print('--------------')
    
    intervals2 = [[6, 7], [2, 4], [5, 9]]
    print(intervals2)
    print("Merged intervals: ")
    print(merge(intervals2))
    print('--------------')
    
    intervals3 = [[1, 4], [2, 6], [3, 5]]
    print(intervals3)
    print("Merged intervals: ")
    print(merge(intervals3))
    print('--------------')
    
main()