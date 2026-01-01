def get_valid_expressions(exp: str)-> list:
    
    # LB = Left Bracket
    # RB = Right Bracket

    LB_rem = 0
    RB_rem = 0
    
    # How many ( and ) must be remvoed??
    for char in exp:
        if char == "(":
            LB_rem += 1
        elif char == ")":
            if LB_rem > 0:
                LB_rem -= 1
            else:
                RB_rem += 1
    
    results = set()

    def dfs(index: int, exp_string: str, balance: int, LB_rem: int, RB_rem: int):

        
        if index == len(exp):
            if balance == 0 and LB_rem == 0 and RB_rem == 0:
                results.add(exp_string)
            return
        
        ch = exp[index]

        # Remove ( :-
        if ch == "(" and LB_rem > 0:
            dfs(index + 1, exp_string, balance, LB_rem-1, RB_rem)
        
        # Remove ) :-
        if ch == ")" and RB_rem > 0:
            dfs(index+1, exp_string, balance, LB_rem, RB_rem-1)
        
        # Keep
        # characters
        if ch not in "()":
            dfs(index+1, exp_string + ch, balance, LB_rem, RB_rem)
        # Keep (
        if ch == "(":
            dfs(index+1, exp_string + ch, balance+1, LB_rem, RB_rem)
        # Keep )
        if ch == ")" and balance > 0:
            dfs(index+1, exp_string + ch, balance-1, LB_rem, RB_rem)

    dfs(0,"",0,LB_rem, RB_rem)
    return list(results)

print("\nOutput of ()())() is: ",get_valid_expressions("()())()"))
print("Output of )( is: ",get_valid_expressions(")("))
print("Output of (a)())() is: ",get_valid_expressions("(a)())()"))
print("Output of abc is: ",get_valid_expressions("abc"),"\n")


