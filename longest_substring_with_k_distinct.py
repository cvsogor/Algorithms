
def longest_substring_with_k_distinct(str, k):
    chars = {}
    window_start = 0
    max_length = 0
    for window_end in range(len(str)):
        right_c = str[window_end]
        if right_c not in chars:
            chars[right_c] = 0
        chars[right_c] += 1

        while len(chars) > k:
            left_c = str[window_start]
            chars[left_c] -= 1
            if chars[left_c] == 0:
                del chars[left_c] 
            window_start +=1
        max_length = max(max_length, window_end-window_start + 1)    
    return max_length

def main():
    print(longest_substring_with_k_distinct("araaci", 2))
    print(longest_substring_with_k_distinct("araaci", 1))
    print(longest_substring_with_k_distinct("cbbebi", 3))
        
main()
