# Grade Labels: Using the gradebook example, write a function that returns a list of (name, label) pairs.

gradebook = {
    "Ana":   [14, 16, 18],
    "João":  [12, 10, 15],
    "Maria": [19, 18, 17],
    "Rui":   [8,  11, 12],
}

def average(nums):
    return sum(nums) / len(nums) if nums else 0.0

# Compute averages
averages = {name: average(grades) for name, grades in gradebook.items()}
print("Averages:", averages)

# Classify each student (simple rules)
for name, avg in averages.items():
    if avg >= 17:
        label = "Excellent"
    elif avg >= 14:
        label = "Good"
    elif avg >= 10:
        label = "Pass"
    else:
        label = "Fail"
    print(f"{name}: {avg:.1f} → {label}")

listaNova = [(name, label) for name, avg in averages.items() if (label := "Excellent" if avg >= 17 else "Good" if avg >= 14 else "Pass" if avg >= 10 else "Fail")]

print (listaNova)


# solução alternativa

gradebook = {
    "Ana":   [14, 16, 18],
    "João":  [12, 10, 15],
    "Maria": [19, 18, 17],
    "Rui":   [8,  11, 12],
}

def average(nums):
    return sum(nums) / len(nums) if nums else 0.0

def classify_grades(book):
    results = []
    for name, grades in book.items():
        avg = average(grades)
        if avg >= 17:
            label = "Excellent"
        elif avg >= 14:
            label = "Good"
        elif avg >= 10:
            label = "Pass"
        else:
            label = "Fail"
        results.append((name, label))
    return results

print(classify_grades(gradebook))