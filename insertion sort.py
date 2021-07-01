# This Program is to Implement Insertion sort

def insertion_sort(array):
    """
    For Shorting the Array, this would take an Average time complexity of O(n2)
    And space complexity of O(1)
    :param array: Array to be Shorted
    :return: Shorted Array
    """
    # Running a loop from the 1st pos to the length of the array
    for i in range(1, len(array)):
        key = array[i]
        j = i-1

        '''
        Now Running the Loop for Comparing jth element starting from 0 to the ith position
        This would compare the keys from jth and till the key is less than element of array -
        - At that specific jth position in the array
        And if this is True: Then we just swap the elements
        Now, decrement j as the jth position element is swapped and we would shorten the shorting array
        '''
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return array


if __name__ == '__main__':
    sample = [[1, 2, 34, 45, 12, 42, 44, 53, 5],
              [1, 0],
              [0, 9, 8, 6, 5, 4, 3, 2, 1],
              [],
              [1, 2, 3, 4, 5, 6, 7]]

    for arr in range(len(sample)):
        print(insertion_sort(sample[arr]))
