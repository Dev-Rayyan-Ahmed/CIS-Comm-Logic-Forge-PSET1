def calculate_impact(contributions:list):
    n = len(contributions)
    impacts = [1]*n

    #calculating left product:
    left_product = 1
    for i in range(n):
        impacts[i] = left_product
        left_product *= contributions[i]
    
    #calculating right product:
    right_product = 1
    for i in range(-1, -(n+1), -1):
        #using negative indexing here
        impacts[i] *= right_product
        right_product *= contributions[i]
    
    return impacts
        
test_contributions = [1,2,3,4]
# impacts should be = [24,12,8,6]
print(calculate_impact(test_contributions))

# testing
# n = 4
# for i in range(-1,-(n+1),-1):
#     print(test_contributions[i])
    # print(i)