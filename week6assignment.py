students = [
    ["Alice", [85, 90, 92]],
    ["Bob", [78, 80, 75]],
    ["Charlie", [92, 85, 88]],
    ["Diana", [70, 75, 72]],
    ["Ethan", [95, 88, 91]]
]

search_name = "Charlie"

index = -1
for i in range(len(students)):
    if students[i][0] == search_name:
        index = i
        break

if index != -1:
    result = (students[index][0], students[index][1], index)
    print(result)
else:
    print("Not found")

