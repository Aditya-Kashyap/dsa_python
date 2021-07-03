def bubble_sort(array_to_sort):
    """
    Simple Sorting Algorithm which Worst Case of O(n2) and Best Case od O(n) if array is already sorted
    :param array_to_sort: The Array to be sorted
    :return: Sorted Array
    """
    n = len(array_to_sort)
    for i in range(n-1):
        swap = False

        for j in range(n-i-1):
            if array_to_sort[j] > array_to_sort[j + 1]:
                array_to_sort[j], array_to_sort[j + 1] = array_to_sort[j + 1], array_to_sort[j]
                swap = True

        if swap is False:
            return array_to_sort

    return array_to_sort


if __name__ == '__main__':
    sample = [[1, 2, 34, 45, 12, 42, 44, 53, 5],
              [1, 0],
              [0, 9, 8, 6, 5, 4, 3, 2, 1],
              [],
              [1, 2, 3, 4, 5, 6, 7]]

    for arr in range(len(sample)):
        print(bubble_sort(sample[arr]))
