def draw():
    from collections import deque

    arr = list(range(80))

    def swapSort_one_way(arr1):
        A = sorted(arr1)

        H = {val: index for index, val in enumerate(arr1)}
        swaps = 0
        for i in range(len(arr1)):
            if arr1[i] != A[i]:
                swaps += 1
                j = H[A[i]]
                H[arr1[i]] = H[A[i]]
                arr1[i], arr1[j] = A[i], arr1[i]

        return swaps

    ## create hashmap value -> index
    def swapSort(arr1):
        A = deque(sorted(arr1))
        H = {val: index for index, val in enumerate(arr1)}

        #H1 = {}
        #for index, val in enumerate(arr1):
        #    if val in H1:
        #        H1[val].append(index)
        #        print("Arr has a reapeat: {}".format(val))
        #    else:
        #
        #        H1[val] = [
        #            index,
        #        ]
        #print(len(H))
        #print(len(H1))

        start = 0
        end = len(arr) - 1
        swaps = 0
        #print(arr1)
        while start < end:
            maxNum = A.pop()
            minNum = A.popleft()
            if end != H[maxNum]:
                #Perform Max Swap
                a = arr1[end]
                arr1[end] = maxNum
                arr1[H[maxNum]] = a
                H[a] = H[maxNum]
                H[maxNum] = end
                swaps += 1
            if start != H[minNum]:
                #Perform Min Swap
                a = arr[start]
                arr1[start] = minNum
                arr1[H[minNum]] = a
                H[a] = H[minNum]
                H[minNum] = start
                swaps += 1

            start += 1
            end -= 1