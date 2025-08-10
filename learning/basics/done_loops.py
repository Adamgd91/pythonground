my_family = ["Adam", "Sarah", "Harper", "Preston"]
men = []
women = []
for i in my_family:
    print(i)
    
for m in my_family:
    if m == "Adam" or m == "Preston":
        men.append(m)
    else:
        women.append(m)

print(men)
print(women)