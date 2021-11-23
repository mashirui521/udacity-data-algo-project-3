# Problem 1: Finding the Square Root of an Integer
## Problem Statement
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.
The expected time complexity is O(log(n))
## Choice of Data Structure
The searched data to find the square root would be an integer array between 0 and the given integer. For each searching step, the middle value is calculated, which square is compared with the given integer. The binary search approach is used here to divide the data into two parts, depending on the comparison, it is decided which part will be searched in the next step.

## Time and Space Complexity
**Time complexity**

For worst case scenario, the time complexity of Binary Search is **O(log(n))**, as expected in the Problem Statement

**Space complexity**

Since only a variable for saving middle value is created, the space complexity is constant **O(1)**

# Problem 2: Search in a Rotated Sorted Array
## Problem Statement
Given a sorted array which is rotated at some random pivot point and a target value to search. If found in the array return its index, otherwise return -1.

There are no duplicates in the array and the algorithm's runtime complexity must be in the order of O(log n).

## Choice of Data Structure
This problem is about searching an element in the given array and returning the index. It would be a variance of Binary Search. The array is divided into two parts, the searching is performed on each part. Two indices found from each parts or -1(if not found) are taken and the maximum one is returned, e.g. if the value is found in the left part, while the searching on right part will return -1.

## Time and Space Complexity
**Time complexity**

For worst case scenario, the time complexity of Binary Search is **O(log(n))**, as expected in the Problem Statement

**Space complexity**

Since only a variable for saving middle value is created, the space complexity is constant **O(1)**


# Problem 3: Rearrange Array Elements
## Problem Statement
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

## Choice of Data Structure
The idea is to firstly sort the given array from maximum to the minimum value and take digits on the even index into the first number, and one on the odd index into the second number. It is guaranteed to get a maximum sum. For sorting, the merged sorting approach is chosen to get the required efficiency.

## Time and Space Complexity
**Time complexity**

The time complexity for merged sorting is **O(n log(n))**, as expected in the Problem Statement.

**Space complexity**

The memory space for the sorted array is needed. The space complexity is **O(n)** depending on the length of input array.


# Problem 4: Dutch National Flag Problem
## Problem Statement
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

## Choice of Data Structure
Since the result array will be in form of [0, 0, 0, 1, 1, 2, 2, 2], it is necessary to get two indices indicating the next position of "0" and "2", the next position of "0" (`next_0_idx`) is initialized by 0, while the "initial next position" of "2" (`next_2_idx`) is len(array)-1. An additional index (`front`) is needed for walking through the given array. When `front` is indicating the digit `0`, it is swapped with the value on `next_0_idx`, for `2` as well.

## Time and Space Complexity
**Time complexity**

The approach is performing a single traversal through the given array, which time complexity is **O(n)**


**Space complexity**

Since the approach is using a in-place sorting algorithm, the space complexity is constant **O(1)**


# Problem 5: Autocomplete with Tries
## Problem Statement
Building a Trie to realize the autocomplete and give suggestions for the given input suffix. 

## Choice of Data Structure
Trie is a tree, each path from root node to lief node is indicating a word. For each `TrieNode`, the flag `is_word` is indicating whether it can build a complete word. The flag in lief nodes are `True`, while in other nodes are `False`.

## Time and Space Complexity
**Time complexity**

Inserting (method `insert`) and finding (method `find`) a word by looping over the characters given in the input word. The time complexity is O(n), depending on the number of characters in the word.

**Space complexity**

The space complexity of `insert` and `find` is O(n * m) depending on the number of words (`n`) saving in the `Trie` and the number of characters `m`. In the worst case, all words saved in the `Trie` don't have any common characters.


# Problem 6: Max and Min in a Unsorted Array
## Problem Statement
In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time.

## Choice of Data Structure
To reach the expected time complexity O(n), the approach should perform a single traversal through the unsorted input array. We need two variable to save the maximum `max_value` and minimum value `min_value`. During the traversal, it is firstly to compare the element on `idx` with the next element on `next_idx`, the greater one will be used to update `max_value` and the smaller one to update `min_value`

## Time and Space Complexity
**Time complexity**

O(n) as expected

**Space complexity**

O(1), only two variables saving max and min values are needed, the complexity is constant


# Problem 7: HTTPRouter using a Trie
## Problem Statement
For this exercise we are going to implement an HTTPRouter using the Trie data structure. The purpose is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and return a handler (a string in this exercise) for that path. A Trie with a single path entry of "/about/me" would look like:

(root, None) -> ("about", None) -> ("me", "About Me handler")


## Choice of Data Structure
Similar as Problem 5, instead of create `TrieNode`s for saving characters in a string, the `TriesNode`s used for this problem is going to save the path parts from a given path, separated by `/`. On lief nodes in the `Trie`, the handler will be returned, for other nodes `non_found_handler`.

## Time and Space Complexity
**Time complexity**

The `insert` and `find` methods in the `RouteTrie` are using a loop over the path parts. The time complexity is O(n), depending on the number of parts.

**Space complexity**

The space complexity of inserting and finding path in `RouteTrie`is O(n * m) depending on the number of paths (`n`) and the number of parts `m` from the given path. The worst case would be having `n` paths in the `RouteTrie`, but they don't have any common parts.
