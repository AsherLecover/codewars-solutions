def find_longest(string):
    spl = string.split(" ")
    max_len = -1
    for i in spl:
        if len(i) > max_len:
            max_len = len(i)
            longest = len(i)
    return longest