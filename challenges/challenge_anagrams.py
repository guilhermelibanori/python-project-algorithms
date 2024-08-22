def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)


def merge(left, right):
    merged = []
    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged.append(left[left_cursor])
            left_cursor += 1
        else:
            merged.append(right[right_cursor])
            right_cursor += 1

    merged.extend(left[left_cursor:])
    merged.extend(right[right_cursor:])

    return merged


def is_anagram(first_string, second_string):
    first_string = first_string.replace(" ", "").lower()
    second_string = second_string.replace(" ", "").lower()

    if not first_string and not second_string:
        return "", "", False

    sorted_first = "".join(merge_sort(first_string))
    sorted_second = "".join(merge_sort(second_string))

    return sorted_first, sorted_second, sorted_first == sorted_second
