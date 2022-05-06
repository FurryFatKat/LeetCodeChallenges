# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.
#
# A row i is weaker than a row j if one of the following is true:
#
#     The number of soldiers in row i is less than the number of soldiers in row j.
#     Both rows have the same number of soldiers and i < j.
#
# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        order_sum = []
        counter = 0
        index = []
        for row in mat:
            order_sum.append([sum(row), counter])
            counter += 1
        order_sum.sort()

        print(order_sum)
        for val in order_sum:
            index.append(val[1])

        print(index)
        return index[:k]

# this solution takes advantage of list object sort function to sort the first
# value of list in list elements
