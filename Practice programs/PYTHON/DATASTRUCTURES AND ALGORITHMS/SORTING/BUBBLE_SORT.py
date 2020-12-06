def bubble_sort(collects_list):
    """
    :param collects_list: mutable list type with homogeneous mutable
                            items which are not sorted
    :return:Items which are sorted
    >>> bubble_sort([0, 5, 2, 3, 2])
    [0, 2, 2, 3, 5]
    >>> bubble_sort([0, 5, 2, 3, 2]) == sorted([0, 5, 2, 3, 2])
    True
    >>> bubble_sort([]) == sorted([])
    True
    >>> bubble_sort([-2, -45, -5]) == sorted([-2, -45, -5])
    True
    >>> bubble_sort([-23, 0, 6, -4, 34]) == sorted([-23, 0, 6, -4, 34])
    True
    >>> bubble_sort(['d', 'a', 'b', 'e', 'c']) == sorted(['d', 'a', 'b', 'e', 'c'])
    True
    >>> import random
    >>> collection= random.sample(range(-50, 50), 100)
    >>> bubble_sort(collection) == sorted(collection)
    True
    >>> import string
    >>> collection = random.choices(string.ascii_letters + string.digits, k=100)
    >>> bubble_sort(collection) == sorted(collection)
    True
    >>> bubble_sort([1,2,3,4,5,5,6,6,7,78,8,8,8,89,9,89])
    [1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 8, 8, 9, 78, 89, 89]
    >>> 6+6
    12
    """
    length = len(collects_list)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if collects_list[j] > collects_list[j + 1]:
                swapped = True
                collects_list[j], collects_list[j + 1] = collects_list[j + 1], collects_list[j]
        if not swapped:
            break
    return collects_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    m = 0
    while m < 3:
        try:
            user_input = input("Enter numbers separated by coma : ")
            unsorted = [int(item) for item in user_input.split(",")]
            m = 6
            print(bubble_sort(unsorted))

        except:
            print("please check the input and re-type ")
            m += 1

    if m == 3:
        print("you tried more than 3 times please run the source code again ")
