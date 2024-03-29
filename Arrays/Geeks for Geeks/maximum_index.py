"""

Given an array A[] of N positive integers. The task is to find the maximum of j - i subjected to the constraint of A[i] < A[j] and i < j.
 

Example 1:

Input:
N = 2
A[] = {1, 10}
Output:
1
Explanation:
A[0]<A[1] so (j-i) is 1-0 = 1.
Example 2:

Input:
N = 9
A[] = {34, 8, 10, 3, 2, 80, 30, 33, 1}
Output:
6
Explanation:
In the given array A[1] < A[7]
satisfying the required 
condition(A[i] < A[j]) thus giving 
the maximum difference of j - i 
which is 6(7-1).
 

Your Task:
The task is to complete the function maxIndexDiff() which finds and returns maximum index difference. Printing the output will be handled by driver code. Return 0 in case no such index is found.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤ 107
0 ≤ A[i] ≤ 109

"""



def maxIndexDiff(N, A):
    # Create two arrays to store the minimum and maximum values on the left and right of each element
    left_min = [0] * N
    right_max = [0] * N
    print(A)
    # Fill the left_min array
    left_min[0] = A[0]
    for i in range(1, N):
        left_min[i] = min(left_min[i - 1], A[i])
    print(left_min)
    # Fill the right_max array
    right_max[N - 1] = A[N - 1]
    for i in range(N - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], A[i])
    print(right_max)
    # Traverse both arrays to find the maximum index difference
    i, j, max_diff = 0, 0, -1
    while i < N and j < N:
        if left_min[i] < right_max[j]:
            max_diff = max(max_diff, j - i)
            j += 1
        else:
            i += 1

    return max_diff

# Example usage:
# N1, A1 = 2, [1, 10]
N2, A2 = 9, [34, 8, 10, 3, 2, 80, 30, 33, 1]

# print(maxIndexDiff(N1, A1))  # Output: 1
print(maxIndexDiff(N2, A2))  # Output: 6
