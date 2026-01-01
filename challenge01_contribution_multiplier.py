def calculate_impact(contributions: list)-> list:

    n = len(contributions)
    if n <= 0:
        return []

    impacts = [1] * n

    # calculating left product:
    left_product = 1
    for i in range(n):
        impacts[i] = left_product
        left_product *= contributions[i]

    # calculating right product:
    right_product = 1
    for i in range(n - 1, -1, -1):
        impacts[i] *= right_product
        right_product *= contributions[i]

    return impacts

test_contributions = [1, 2, 3, 4]
# impacts should be = [24,12,8,6]
print("Input: [1, 2, 3, 4], and Output: ", calculate_impact(test_contributions))
