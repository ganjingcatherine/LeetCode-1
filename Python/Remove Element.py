"""
Given an array and a value, remove all instances of that value in place and return the new length.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        start = 0
        end = len(A) -1 
        while start <= end:
            if A[start] == elem:
                A[start],A[end] = A[end],A[start]
                end -= 1
            else:
                start += 1
        return end + 1