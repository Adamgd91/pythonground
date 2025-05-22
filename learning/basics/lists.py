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