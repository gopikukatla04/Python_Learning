# Define the bubble_sort function that takes a list as input
# Find the length of the list
# Repeat the process for each element in the list (outer loop)
# For each element, compare it with the next one in the list (inner loop)
# If the current element is greater than the next, swap them
# Continue this until the largest elements bubble to the end
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Create the unsorted list
# Print the original_list
# Call the bubble_sort function
# Print the sorted list
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original Array:", arr)
bubble_sort(arr)
print("Sorted Array  :", arr)