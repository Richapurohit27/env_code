import os
from collections import deque

def get_min_time(cache_size, cache_time, server_time, urls):
    dns_cache = set()
    cache_queue = deque()
    result = []

    for url in urls:
        if url in dns_cache:
            # If URL is in the cache, fetch from cache
            result.append(cache_time)
            # Move the URL to the front of the queue to represent it as the most recently used
            cache_queue.remove(url)
            cache_queue.appendleft(url)
        else:
            # If URL is not in the cache, fetch from server
            result.append(server_time)

            # Add the URL to the cache and the queue (remove the oldest entry if cache is full)
            dns_cache.add(url)
            cache_queue.appendleft(url)

            if len(cache_queue) > cache_size:
                oldest_url = cache_queue.pop()
                dns_cache.remove(oldest_url)

    return result

if __name__ == '__main__':
    # Read input values from the user
    cache_size = int(input("Enter cache size: ").strip())
    cache_time = int(input("Enter cache fetch time: ").strip())
    server_time = int(input("Enter server fetch time: ").strip())
    urls_count = int(input("Enter number of URLs: ").strip())

    urls = []
    for _ in range(urls_count):
        urls_item = input("Enter URL: ").strip()
        urls.append(urls_item)

    # Call the function to get the result
    result = get_min_time(cache_size, cache_time, server_time, urls)

    # Write the result to an output file
    with open('output.txt', 'w') as fptr:
        for time in result:
            fptr.write(str(time) + '\n')
