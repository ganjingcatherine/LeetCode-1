"""
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""

class Solution:
    # @return a string
    def getPermutation(self, n, k):
        used = [i for i in xrange(1,n+1)]
        fact = math.factorial(n-1)
        result = ""
        for i in reversed(xrange(n)):
            sequence = math.ceil(float(k)/fact)
            result += str(used[int(sequence)-1])
            used.remove(used[int(sequence)-1])
            if i > 0:
                k %= fact
                fact/=i
        return result

class Solution:
    """
    @param n: n
    @param k: the k-th permutation
    @return: a string, the k-th permutation
    """
    def getPermutation(self, n, k):
        factorial = [1 for i in range(n + 1)]
        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i
        array = range(1, n + 1)
        k = (k % factorial[n]) - 1
        permutation = []
        for i in xrange(n - 1, -1, -1):
            idx, k = divmod(k, factorial[i])
            permutation.append(array.pop(idx))
        return "".join(map(str, permutation))
