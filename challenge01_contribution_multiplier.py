def calculate_impact(contributions:list):
    impacts = []
    for contribute in contributions:
        impact = 1
        for score in contributions:
            if score == contribute:
                continue
            impact = impact*score
        impacts.append(impact)
    return impacts
        
test_contributions = [1,2,3,4]
# impacts = [24,12,8,6]
print(calculate_impact(test_contributions))