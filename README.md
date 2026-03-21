# 📁 Merge Sort Algorithm
> A Python implementation of merge sort, a divide and conquer sorting algorithm that recursively splits, sorts, and merges arrays.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Project](https://img.shields.io/badge/Learning-Journey-orange)
![DSA](https://img.shields.io/badge/Topic-Algorithms-red?logo=python&logoColor=white)

## 📌 About

This project implements merge sort from scratch, one of the most fundamental sorting algorithms in computer science. The function recursively splits an array in half until every piece has one element, then merges the pieces back together in sorted order. Built to understand recursion, divide and conquer thinking, and how O(n log n) sorting works under the hood.

## 🧠 What I Learned

- **Recursion with a base case** — Using `if len(array) <= 1: return` to stop the recursion when a subarray can't be split further, which is the foundation of all divide and conquer algorithms
- **Divide and conquer** — Splitting the problem into smaller subproblems (`left_part` and `right_part`), solving each recursively, and combining the results, a pattern that appears across many important algorithms
- **The merge step** — Using three index trackers (`left_array_index`, `right_array_index`, `sorted_index`) to walk through both halves simultaneously and write the smaller element back into the original array in order
- **Handling leftover elements** — After the main merge loop ends, one side may still have elements remaining. Two additional while loops drain whichever side has leftovers, preventing data loss
- **In-place merging** — Writing sorted values directly back into the original array rather than returning a new one, modifying the list in place the same way Python's built-in `list.sort()` does
- **O(n log n) time complexity** — Understanding that splitting takes `O(log n)` levels of recursion and merging takes `O(n)` work per level, making merge sort significantly faster than `O(n²)` algorithms like bubble sort on large datasets.

## 🛠️ Technologies Used
| Tool/Library | Purpose |
|--------------|---------|
| Python 3.x | Core Language |

## 💡 How It Works

```
Original:  [4, 10, 6, 14, 2, 1, 8, 5]

Split:     [4, 10, 6, 14]    [2, 1, 8, 5]
Split:     [4, 10] [6, 14]   [2, 1] [8, 5]
Split:     [4] [10] [6] [14] [2] [1] [8] [5]

Merge:     [4, 10] [6, 14]   [1, 2] [5, 8]
Merge:     [4, 6, 10, 14]    [1, 2, 5, 8]
Merge:     [1, 2, 4, 5, 6, 8, 10, 14] ✅
```

**Example output:**
```
Unsorted array:
[4, 10, 6, 14, 2, 1, 8, 5]
Sorted array:
[1, 2, 4, 5, 6, 8, 10, 14]
```

## 🚀 Future Improvements

- [ ] Add a step counter to show how many comparisons were made during sorting
- [ ] Compare performance against Python's built-in `sorted()` on large arrays
- [ ] Implement quicksort and benchmark both side by side
- [ ] Visualize the recursive split and merge process using `matplotlib`

## 📂 Project Structure

```
merge-sort/
│
├── MergeSortAlgorithm.py    # merge_sort function with example usage
└── README.md
```

*Part of my Python learning journey 🐍 — implementing divide and conquer sorting algorithms from scratch*
