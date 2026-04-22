# Step 1: Sample data (each item represents a class with features)

classes = {
    "Class1": [1, 0, 1, 0, 1],
    "Class2": [1, 1, 0, 0, 1],
    "Class3": [0, 0, 1, 1, 0],
    "Class4": [0, 1, 1, 1, 0]
}

# Step 2: Function to calculate similarity

def calculate_similarity(a, b):
    same = 0
    total = 0

    for x, y in zip(a, b):
        if x == 1 or y == 1:
            total += 1
            if x == 1 and y == 1:
                same += 1

    if total == 0:
        return 0

    return same / total


# Step 3: Display similarity values

print("Similarity between classes:\n")

names = list(classes.keys())

for i in range(len(names)):
    for j in range(i + 1, len(names)):
        value = calculate_similarity(classes[names[i]], classes[names[j]])
        print(names[i], "-", names[j], ":", round(value, 2))


# Step 4: Simple grouping logic

groups = []
checked = []

for i in range(len(names)):
    if names[i] in checked:
        continue

    current_group = [names[i]]
    checked.append(names[i])

    for j in range(len(names)):
        if names[j] not in checked:
            value = calculate_similarity(classes[names[i]], classes[names[j]])
            if value >= 0.4:
                current_group.append(names[j])
                checked.append(names[j])

    groups.append(current_group)


# Step 5: Print final groups

print("\nFinal Clusters:\n")

for index, g in enumerate(groups):
    print("Group", index + 1, ":", g)
