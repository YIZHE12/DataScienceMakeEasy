'''On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
Note:

N will be an integer in the range [1, 30].
K will be an integer in the range [1, 2^(N-1)].'''


# solution 1: Brute force
# Time: O(2^n)
# Space: O(2^n) (length of the array)
class Solution(object):
	def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        array = ["0"]
        for i in range(N):   
            new_array = []
            for j in range(len(array[i])):
                if array[i][j]=="0":
                    new_array.extend("0")
                    new_array.extend("1")
                elif array[i][j]=="1":
                    new_array.append("1")
                    new_array.append("0")

            array.append(new_array)
        
        return (array[N-1][K-1])

# solution 2: recursion based on parent
# Time O(N)
# Space (1)

class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1:
            return 0
        
        if K%2 == 1:
            return self.kthGrammar(N-1, int((K+1)/2))
        else:
            return (1+self.kthGrammar(N-1, int((K+1)/2)))%2