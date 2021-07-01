def maxSlidingWindow(nums, k):
    i = 0
    j = 0
    maximum = []
    final = []

    while j < len(nums):
        maximum.append(nums[j])
        print(maximum)

        if j - i + 1 < k:
            j += 1

        elif j - i + 1 == k:
            final.append(max(maximum))
            print('final', final)

            maximum.pop(0)
            print('max', maximum)
            
            i += 1
            j += 1

    return final


li = [7, 2, -1]
key = 2
print(maxSlidingWindow(li, key))

