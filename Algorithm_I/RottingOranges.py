# You are given an m x n grid where each cell can have one of three values:
#
#     0 representing an empty cell,
#     1 representing a fresh orange, or
#     2 representing a rotten orange.
#
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
#
#
#
# Example 1:
#
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
#
# Example 2:
#
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
#
# Example 3:
#
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

'''
https://leetcode.com/problems/rotting-oranges/discuss/563686/Python-Clean-and-Well-Explained-(faster-than-greater-90)


Python

from collections import deque

# Time complexity: O(rows * cols) -> each cell is visited at least once
# Space complexity: O(rows * cols) -> in the worst case if all the oranges are rotten they will be added to the queue

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # number of rows
        rows = len(grid)
        if rows == 0:  # check if grid is empty
            return -1

        # number of columns
        cols = len(grid[0])

        # keep track of fresh oranges
        fresh_cnt = 0

        # queue with rotten oranges (for BFS)
        rotten = deque()

        # visit each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    # add the rotten orange coordinates to the queue
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    # update fresh oranges count
                    fresh_cnt += 1

        # keep track of minutes passed.
        minutes_passed = 0

        # If there are rotten oranges in the queue and there are still fresh oranges in the grid keep looping
        while rotten and fresh_cnt > 0:

            # update the number of minutes passed
            # it is safe to update the minutes by 1, since we visit oranges level by level in BFS traversal.
            minutes_passed += 1

            # process rotten oranges on the current level
            for _ in range(len(rotten)):
                x, y = rotten.popleft()

                # visit all the adjacent cells
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    # calculate the coordinates of the adjacent cell
                    xx, yy = x + dx, y + dy
                    # ignore the cell if it is out of the grid boundary
                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue
                    # ignore the cell if it is empty '0' or visited before '2'
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue

                    # update the fresh oranges count
                    fresh_cnt -= 1

                    # mark the current fresh orange as rotten
                    grid[xx][yy] = 2

                    # add the current rotten to the queue
                    rotten.append((xx, yy))


        # return the number of minutes taken to make all the fresh oranges to be rotten
        # return -1 if there are fresh oranges left in the grid (there were no adjacent rotten oranges to make them rotten)
        return minutes_passed if fresh_cnt == 0 else -1
from collections import deque

# Time complexity: O(rows * cols) -> each cell is visited at least once
# Space complexity: O(rows * cols) -> in the worst case if all the oranges are rotten they will be added to the queue

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # number of rows
        rows = len(grid)
        if rows == 0:  # check if grid is empty
            return -1

        # number of columns
        cols = len(grid[0])

        # keep track of fresh oranges
        fresh_cnt = 0

        # queue with rotten oranges (for BFS)
        rotten = deque()

        # visit each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    # add the rotten orange coordinates to the queue
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    # update fresh oranges count
                    fresh_cnt += 1

        # keep track of minutes passed.
        minutes_passed = 0

        # If there are rotten oranges in the queue and there are still fresh oranges in the grid keep looping
        while rotten and fresh_cnt > 0:

            # update the number of minutes passed
            # it is safe to update the minutes by 1, since we visit oranges level by level in BFS traversal.
            minutes_passed += 1

            # process rotten oranges on the current level
            for _ in range(len(rotten)):
                x, y = rotten.popleft()

                # visit all the adjacent cells
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    # calculate the coordinates of the adjacent cell
                    xx, yy = x + dx, y + dy
                    # ignore the cell if it is out of the grid boundary
                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue
                    # ignore the cell if it is empty '0' or visited before '2'
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue

                    # update the fresh oranges count
                    fresh_cnt -= 1

                    # mark the current fresh orange as rotten
                    grid[xx][yy] = 2

                    # add the current rotten to the queue
                    rotten.append((xx, yy))


        # return the number of minutes taken to make all the fresh oranges to be rotten
        # return -1 if there are fresh oranges left in the grid (there were no adjacent rotten oranges to make them rotten)
        return minutes_passed if fresh_cnt == 0 else -1


'''


'''
https://leetcode.com/problems/rotting-oranges/discuss/588024/C%2B%2B-or-BFS-or-100-Space-95-time-or-explanation-of-logic

C++


class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid)
    {

        vector<int> dir={-1,0,1,0,-1}; //used for finding all 4 adjacent coordinates

        int m=grid.size();
        int n=grid[0].size();

        queue<pair<int,int>> q;
        int fresh=0; //To keep track of all fresh oranges left
        for(int i=0;i<m;i++)
            for(int j=0;j<n;j++)
            {
                if(grid[i][j]==2)
                    q.push({i,j});
                if(grid[i][j]==1)
                    fresh++;
            }
        int ans=-1; //initialised to -1 since after each step we increment the time by 1 and initially all rotten oranges started at 0.
        while(!q.empty())
        {
            int sz=q.size();
            while(sz--)
            {
                pair<int,int> p=q.front();
                q.pop();
                for(int i=0;i<4;i++)
                {
                    int r=p.first+dir[i];
                    int c=p.second+dir[i+1];
                    if(r>=0 && r<m && c>=0 && c<n &&grid[r][c]==1)
                    {
                        grid[r][c]=2;
                        q.push({r,c});
                        fresh--; // decrement by 1 foreach fresh orange that now is rotten
                    }

                }
            }
            ans++; //incremented after each minute passes
        }
        if(fresh>0) return -1; //if fresh>0 that means there are fresh oranges left
        if(ans==-1) return 0; //we initialised with -1, so if there were no oranges it'd take 0 mins.
        return ans;

    }
};


'''
