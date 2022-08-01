def merge(array_1, array_2):
    merged_array = []
    pivot_1 = 0
    pivot_2 = 0
    while True:
        if array_1[pivot_1] < array_2[pivot_2]:
            merged_array.append(array_1[pivot_1])
            if pivot_1 < len(array_1) - 1:
                pivot_1 += 1
            else:
                for i in range(pivot_2, len(array_2)):
                    merged_array.append(array_2[i])
                break
        else:
            merged_array.append(array_2[pivot_2])
            if pivot_2 < len(array_2) - 1:
                pivot_2 += 1
            else:
                for i in range(pivot_1, len(array_1)):
                    merged_array.append(array_1[i])
                break
    return merged_array


def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        middle = len(array) // 2
        array_1 = array[:middle]
        array_2 = array[middle:]
        sorted_array_1 = merge_sort(array_1)
        sorted_array_2 = merge_sort(array_2)
        sorted_array = merge(sorted_array_1, sorted_array_2)
        return sorted_array


array = [1, 9, -2, 3, 5, 1, 3, 3, 2, 9, 8]

sorted_array = merge_sort(array)
print(sorted_array)