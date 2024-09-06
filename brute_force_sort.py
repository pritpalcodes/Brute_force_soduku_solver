import curses
import time
import random

# Function to visualize the list as bars
def print_list_curses(stdscr, lst, highlight_indices=[], sorted_indices=[]):
    stdscr.clear()  # Clear the screen for fresh display
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Sorted items in green
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # Highlighted items (for comparison/swaps) in red
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)   # Default items in cyan

    max_y, max_x = stdscr.getmaxyx()  # Get terminal screen size
    max_value = max(lst)
    bar_width = max_x // len(lst)  # Width per bar

    for i, val in enumerate(lst):
        color = curses.color_pair(3)  # Default color for the bars
        if i in highlight_indices:
            color = curses.color_pair(2)  # Highlight bars being compared or swapped
        elif i in sorted_indices:
            color = curses.color_pair(1)  # Bars that are sorted

        # Draw the vertical bar proportional to the value
        bar_height = int((val / max_value) * (max_y - 1))
        for y in range(max_y - 1, max_y - 1 - bar_height, -1):
            stdscr.addstr(y, i * bar_width, ' ' * (bar_width - 1), color)

    stdscr.refresh()  # Refresh the screen to update the display
    time.sleep(0.1)  # Small delay for visualization effect

# Bubble Sort Visualization
def bubble_sort_curses(stdscr, lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            print_list_curses(stdscr, lst, highlight_indices=[j, j + 1])
    return lst

# Insertion Sort Visualization
def insertion_sort_curses(stdscr, lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
            print_list_curses(stdscr, lst, highlight_indices=[j + 1, i])
        lst[j + 1] = key
        print_list_curses(stdscr, lst, highlight_indices=[j + 1])
    return lst

# Merge Sort Visualization
def merge_sort_curses(stdscr, lst):
    def merge(lst, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid

        # Temporary arrays
        L = lst[left:mid + 1]
        R = lst[mid + 1:right + 1]

        i = 0  # Initial index of first subarray
        j = 0  # Initial index of second subarray
        k = left  # Initial index of merged subarray

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = R[j]
                j += 1
            print_list_curses(stdscr, lst, highlight_indices=[k])
            k += 1

        while i < n1:
            lst[k] = L[i]
            i += 1
            print_list_curses(stdscr, lst, highlight_indices=[k])
            k += 1

        while j < n2:
            lst[k] = R[j]
            j += 1
            print_list_curses(stdscr, lst, highlight_indices=[k])
            k += 1

    def merge_sort(lst, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort(lst, left, mid)
            merge_sort(lst, mid + 1, right)
            merge(lst, left, mid, right)

    merge_sort(lst, 0, len(lst) - 1)
    return lst

# Quick Sort Visualization
def quick_sort_curses(stdscr, lst):
    def partition(lst, low, high):
        pivot = lst[high]
        i = low - 1
        for j in range(low, high):
            if lst[j] < pivot:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
            print_list_curses(stdscr, lst, highlight_indices=[i, j])
        lst[i + 1], lst[high] = lst[high], lst[i + 1]
        print_list_curses(stdscr, lst, highlight_indices=[i + 1, high])
        return i + 1

    def quick_sort(lst, low, high):
        if low < high:
            pi = partition(lst, low, high)
            quick_sort(lst, low, pi - 1)
            quick_sort(lst, pi + 1, high)

    quick_sort(lst, 0, len(lst) - 1)
    return lst

# Wrapper function to run the curses-based sorting visualizer
def start_sorting_visualizer(stdscr):
    # List of 10 random numbers
    lst = random.sample(range(1, 100), 10)

    # Debugging: Output the list to ensure it's working
    stdscr.addstr(0, 0, f"Initial list: {lst}")
    stdscr.refresh()
    time.sleep(1)  # Short pause to view the initial list

    # Prompt user to select a sorting algorithm
    stdscr.clear()
    stdscr.addstr(0, 0, "Select Sorting Algorithm:")
    stdscr.addstr(2, 0, "1 - Bubble Sort")
    stdscr.addstr(3, 0, "2 - Insertion Sort")
    stdscr.addstr(4, 0, "3 - Merge Sort")
    stdscr.addstr(5, 0, "4 - Quick Sort")
    stdscr.refresh()

    key = stdscr.getch()
    if key == ord('1'):
        stdscr.addstr(7, 0, "Running Bubble Sort...")
        stdscr.refresh()
        bubble_sort_curses(stdscr, lst)
    elif key == ord('2'):
        stdscr.addstr(7, 0, "Running Insertion Sort...")
        stdscr.refresh()
        insertion_sort_curses(stdscr, lst)
    elif key == ord('3'):
        stdscr.addstr(7, 0, "Running Merge Sort...")
        stdscr.refresh()
        merge_sort_curses(stdscr, lst)
    elif key == ord('4'):
        stdscr.addstr(7, 0, "Running Quick Sort...")
        stdscr.refresh()
        quick_sort_curses(stdscr, lst)

    # Display sorted list
    stdscr.addstr(9, 0, f"Sorting Complete! Final list: {lst}")
    stdscr.addstr(10, 0, "Press any key to exit.")
    stdscr.refresh()
    stdscr.getch()

# Run the visualizer using curses wrapper
curses.wrapper(start_sorting_visualizer)
