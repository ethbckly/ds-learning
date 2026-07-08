s = "abdcabcbb"


def longest_unique_substring(s):
    seen = {}
    start = 0
    max_length = 0

    for end in range(len(s)):
        char = s[end]
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        
        seen[char] = end
        current_length = end - start + 1
        max_length = max(max_length, current_length)

    return max_length


print(longest_unique_substring(s))