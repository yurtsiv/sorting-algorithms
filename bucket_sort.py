import math
from bubble_sort import bubble_sort

def bucket_sort(array, bucket_size):
    buckets_num = math.ceil(len(array) / bucket_size);
    buckets = [[] * buckets_num]
    max_elem = max(array)

    for elem in array:
        bucket_index = math.floor(elem / (max_elem * bucket_size))
        buckets[bucket_index].append(elem)

    for i in range(0, len(buckets)):
        buckets[i] = bubble_sort(buckets[i])

    return [bucket for bucket in buckets][0]
