def find_longest(string):
    spl = string.split(" ")
    max_len = -1
    for i in spl:
        if len(i) > max_len:
            max_len = len(i)
            longest = len(i)
    return longest
print(find_longest("Arsene Ishikawa Mine Fujiko Nix Goemon Fujiko Daisuke Koichi III Da Da Lupin Vinci Da"))