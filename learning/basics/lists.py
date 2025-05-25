hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50
# Create list areas
areas = [hall, kit, liv, bed, bath]
# Print areas
print(areas)
print(areas[2])
# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
        ["bedroom", bed],
        ["bathroom", bath]]
# Print out house
print(house)
bathroom_length = house[-1][1]
print(bathroom_length)
################################################
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Change this command
areas_copy = list(areas)
# Change areas_copy
areas_copy[0] = 5.0
# Print areas
print(areas)
##############################################
scores = [99, 15, 65, 43, 22, 28, 100, 98, 64, 66, 54, 76, 87, 88, 34, 56, 65, 46, 76, 65]
reversed_scores = sorted(scores, reverse = True)
print(reversed_scores)
max_score = max(scores)
print(max_score)
avg_score = sum(scores) / len(scores)
print(avg_score)
print(scores)