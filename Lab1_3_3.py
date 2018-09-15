def ShiftDown(array, root, bottom):
    finished = False
    maxChild = 0
    
    while ( (root * 2 <= bottom) and (not finished) ):
        if (root * 2 == bottom):
            maxChild = root * 2
        elif (array[root * 2]    > array[root * 2 + 1]):
            maxChild = root * 2
        else:
            maxChild = root * 2 + 1

        if (array[root] < array [maxChild]):
            array[root],array[maxChild] = array[maxChild],array[root]
            root = maxChild
        else:
            finished = True
            
def HeapSort(array, arraySize):
    for i in range(6, 0 , -1):
        ShiftDown(array, i, arraySize)
    for i in range(arraySize - 1, 1, -1):
        array[0],array[i] = array[i],array[0]
        ShiftDown(array, 0, i - 1)

ar = [1,4,2,8,4,7,3,9,4,0,1,6,4,7]
        
