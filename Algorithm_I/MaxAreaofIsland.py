# ou are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
# The area of an island is the number of cells with a value 1 in the island.
#
# Return the maximum area of an island in grid. If there is no island, return 0.
#
#
#
# Example 1:
#
# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
#
# Example 2:
#
# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0


# Time Limit Exceeded
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_traverse = 0
        used_pair = []
        rows, cols = len(grid), len(grid[0])
        def bfs(q, counter=1):
            while q:
                i, j = q.popleft()
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                        q.append((x,y))
                        used_pair.append([x, y])
                        counter += 1
            return counter


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and ([i, j] not in used_pair):
                    count = bfs(q=collections.deque([(i,j)]))
                    max_traverse = max(max_traverse, count)

        return max_traverse


# 209 ms and 16.5 MB
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_traverse = 0
        rows, cols = len(grid), len(grid[0])
        def dfs(i, j):
            if 0 <= i < rows and 0 <= j < cols and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
            return 0


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    max_traverse = max(dfs(i,j), max_traverse)

        return max_traverse


'''

https://leetcode.com/problems/max-area-of-island/discuss/1244552/JS-Python-Java-C%2B%2B-or-Simple-DFS-Recursion-Solution-w-Explanation

Idea:

So we can just use a simple iteration through the grid and look for islands. When we find an island, we can use a recursive helper function (trav) to sum up all the connected pieces of land and return the total land mass of the island.

As we traverse over the island, we can replace the 1s with 0s to prevent "finding" the same land twice. We can also keep track of the largest island found so far (ans), and after the grid has been fully traversed, we can return ans.

    Time Complexity: O(N * M) where N and M are the lengths of the sides of the grid
    Space Complexity: O(L) where L is the size of the largest island, representing the maximum recursion stack
        or O(N * M + L) if we create an N * M matrix in order to not modify the input

Javascript Code:

The best result for the code below is 92ms / 39.7MB (beats 95% / 100%).

var maxAreaOfIsland = function(grid) {
    let ans = 0, n = grid.length, m = grid[0].length
    const trav = (i, j) => {
        if (i < 0 || j < 0 || i >= n || j >= m || !grid[i][j]) return 0
        grid[i][j] = 0
        return 1 + trav(i-1, j) + trav(i, j-1) + trav(i+1, j) + trav(i, j+1)
    }
    for (let i = 0; i < n; i++)
        for (let j = 0; j < m; j++)
            if (grid[i][j]) ans = Math.max(ans, trav(i, j))
    return ans
};

Python Code:

The best result for the code below is 124ms / 16.7MB (beats 95% / 48%).

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans, n, m = 0, len(grid), len(grid[0])
        def trav(i: int, j: int) -> int:
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0: return 0
            grid[i][j] = 0
            return 1 + trav(i-1, j) + trav(i, j-1) + trav(i+1, j) + trav(i, j+1)
        for i, j in product(range(n), range(m)):
            if grid[i][j]: ans = max(ans, trav(i, j))
        return ans

Java Code:

The best result for the code below is 2ms / 39.2MB (beats 99% / 83%).

class Solution {
    private int n, m;
    public int maxAreaOfIsland(int[][] grid) {
        int ans = 0;
        n = grid.length;
        m = grid[0].length;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (grid[i][j] > 0) ans = Math.max(ans, trav(i, j, grid));
        return ans;
    }
    private int trav(int i, int j, int[][] grid) {
        if (i < 0 || j < 0 || i >= n || j >= m || grid[i][j] < 1) return 0;
        grid[i][j] = 0;
        return 1 + trav(i-1, j, grid) + trav(i, j-1, grid) + trav(i+1, j, grid) + trav(i, j+1, grid);
    }
}

C++ Code:

The best result for the code below is 8ms / 23.0MB (beats 100% / 95%).

class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int ans = 0;
        n = grid.size(), m = grid[0].size();
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (grid[i][j]) ans = max(ans, trav(i, j, grid));
        return ans;
    }
private:
    int n, m;
    int trav(int i, int j, vector<vector<int>>& grid) {
        if (i < 0 || j < 0 || i >= n || j >= m || !grid[i][j]) return 0;
        grid[i][j] = 0;
        return 1 + trav(i-1, j, grid) + trav(i, j-1, grid) + trav(i+1, j, grid) + trav(i, j+1, grid);
    }
};





'''
