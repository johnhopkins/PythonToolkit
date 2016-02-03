# A recursive pythonic binary search procedure
# Needs a sorted in increasing order list to work.

def rBinarySearch(list,element):
    if len(list) == 1:
        return element == list[0]
    midPoint = len(list)/2
    if list[midPoint] > element:
        return rBinarySearch( list[ : midPoint] , element )
    if list[midPoint] < element:
        return rBinarySearch( list[midPoint : ] , element)
    return True


