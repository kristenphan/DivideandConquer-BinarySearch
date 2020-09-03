# python3
def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query, high, low):
    if high <= low:
        if keys[low] == query:
            return low
        return -1

    mid = (high + low) // 2

    if keys[mid] == query:
        return mid
    elif keys[mid] > query:
        return binary_search(keys, query, mid - 1, low)
    else:
        return binary_search(keys, query, high, mid + 1)


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]
    high, low = len(input_keys)-1, 0

    for q in input_queries:
        print(binary_search(input_keys, q, high, low), end=' ')
