def recover_password(log, pattern):
    log_len = len(log)
    best_sub = ""
    min_len = float('inf')

    dict_p = {}
    for char in pattern:
        dict_p[char] = dict_p.get(char, 0) + 1

    for i in range(log_len):
        for j in range(i, log_len):
            substring = log[i : j+1]
            
            if is_valid(substring, dict_p):
                if len(substring) < min_len:
                    min_len = len(substring)
                    best_sub = substring
                    
    return best_sub

def is_valid(substring, dict_p):
    sub_count = {}
    for char in substring:
        sub_count[char] = sub_count.get(char, 0) + 1
        
    for char, count in dict_p.items():
        if sub_count.get(char, 0) < count:
            return False
            
    return True

## Brute Force Attempt
log = "ADOBECODEBANC"
pattern = "ABC"
print(recover_password(log, pattern))