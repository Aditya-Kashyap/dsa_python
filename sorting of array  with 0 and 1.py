def sort_array(array):
    zero = []
    one = []
    for i in array:
        if i == 0:
            zero.append(i)

        else:
            one.append(i)

    zero.extend(one)
    return zero


if __name__ == '__main__':
    a = [0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1]
    b = sort_array(a)
    print(b)
