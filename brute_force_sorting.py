import matplotlib.pyplot as plt
import numpy as np
import random
import time

# Function to update the bar plot visualization
def update_plot(array, colors, title):
    plt.clf()  # Clear the figure
    plt.bar(range(len(array)), array, color=colors)
    plt.title(title)
    plt.pause(0.1)  # Pause for a short interval to create animation effect

# Bubble Sort Visualization
def bubble_sort_visual(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            colors = ['green' if x == j or x == j+1 else 'blue' for x in range(n)]
            update_plot(array, colors, "Bubble Sort")
    return array

# Insertion Sort Visualization
def insertion_sort_visual(array):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            colors = ['green' if x == j+1 or x == i else 'blue' for x in range(n)]
            update_plot(array, colors, "Insertion Sort")
        array[j + 1] = key
    return array

# Merge Sort Visualization
def merge_sort_visual(array):
    def merge(array, left, mid, right):
        L = array[left:mid+1]
        R = array[mid+1:right+1]
        i = j = 0
        k = left

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            colors = ['green' if x >= left and x <= right else 'blue' for x in range(len(array))]
            update_plot(array, colors, "Merge Sort")
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            colors = ['green' if x >= left and x <= right else 'blue' for x in range(len(array))]
            update_plot(array, colors, "Merge Sort")
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            colors = ['green' if x >= left and x <= right else 'blue' for x in range(len(array))]
            update_plot(array, colors, "Merge Sort")
            k += 1

    def merge_sort(array, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort(array, left, mid)
            merge_sort(array, mid + 1, right)
            merge(array, left, mid, right)

    merge_sort(array, 0, len(array) - 1)
    return array

# Quick Sort Visualization
def quick_sort_visual(array):
    def partition(array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
            colors = ['green' if x == i or x == j else 'blue' for x in range(len(array))]
            update_plot(array, colors, "Quick Sort")
        array[i+1], array[high] = array[high], array[i+1]
        update_plot(array, ['green' if x == i+1 or x == high else 'blue' for x in range(len(array))], "Quick Sort")
        return i + 1

    def quick_sort(array, low, high):
        if low < high:
            pi = partition(array, low, high)
            quick_sort(array, low, pi - 1)
            quick_sort(array, pi + 1, high)

    quick_sort(array, 0, len(array) - 1)
    return array

# Main visualization runner
def visualize_sorting_algorithm():
    # Generate a random list of integers
    array = random.sample(range(1, 100), 10)
    print(f"Original array: {array}")

    # Plot setup
    plt.ion()  # Turn on interactive mode
    fig, ax = plt.subplots()

    # Prompt user to select a sorting algorithm
    print("Select Sorting Algorithm:")
    print("1 - Bubble Sort")
    print("2 - Insertion Sort")
    print("3 - Merge Sort")
    print("4 - Quick Sort")
    choice = input("Enter the number corresponding to the algorithm: ")

    # Select and run the chosen algorithm
    if choice == '1':
        plt.title("Bubble Sort Visualization")
        bubble_sort_visual(array)
    elif choice == '2':
        plt.title("Insertion Sort Visualization")
        insertion_sort_visual(array)
    elif choice == '3':
        plt.title("Merge Sort Visualization")
        merge_sort_visual(array)
    elif choice == '4':
        plt.title("Quick Sort Visualization")
        quick_sort_visual(array)
    else:
        print("Invalid choice!")

    # Show the sorted array
    plt.ioff()
    plt.show()

# Run the visualization
visualize_sorting_algorithm()
