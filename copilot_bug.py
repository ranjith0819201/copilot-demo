# Copilot: Write a function to check if a list is sorted
def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True
# Copilot: Implement a function to check if a list is sorted in ascending order
def is_sorted(lst):
    for i in range(len(lst)):
        if lst[i] > lst[i+1]:
            return False
    return True
# Corrected version
def is_sorted_fixed(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True
