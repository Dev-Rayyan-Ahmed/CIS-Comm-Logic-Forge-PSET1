def recover_password(log: str, pattern: str)-> str:

    pattern_len = len(pattern)
    log_len = len(log)

    if not log or not pattern or pattern_len > log_len:
        return ""
    
    dict_p = {}
    for char in pattern:
        dict_p[char] = dict_p.get(char,0) + 1 
    
    left_ptr = 0
    right_ptr = 0
    required_unique = len(dict_p)
    formed = 0
    window_counts = {}

    result = (float('inf'), None, None) 
    # Tuple to be returned by func (len, left, right ptrs)

    while (right_ptr < log_len):
        char = log[right_ptr]
        window_counts[char] = window_counts.get(char, 0) + 1

        if char in dict_p and window_counts[char] == dict_p[char]:
            # here we are checking whether char is in list 
            # and only increment when our count is satisfied (2nd condition)
            formed += 1
        
        while formed == required_unique:
            
            current_window_len = right_ptr - left_ptr +1
            if current_window_len < result[0]:
                # updating result if new one smaller than previous one
                result = (current_window_len, left_ptr, right_ptr)
            
            # minimizing Length of substring to get minimum substring
            left_most_char = log[left_ptr]
            window_counts[left_most_char] -= 1

            # if minimizng removed required character then we update value and exit loop
            if left_most_char in dict_p and window_counts[left_most_char] < dict_p[left_most_char]:
                formed -= 1

            left_ptr  += 1
        right_ptr += 1
    
    return log[result[1] : result[2] + 1] if result[0] != float('inf') else ""

log = "ADOBECODEBANC"
pattern = "ABC"
print("\nInput is 'ADOBECODEBANC'\nPattern: 'ABC'\nOutput:",recover_password(log, pattern))
                