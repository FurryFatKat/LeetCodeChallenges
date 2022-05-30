# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
#
# The distance between two adjacent cells is 1.
#
#
#
# Example 1:
#
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
#
# Example 2:
#
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]




'''
1
https://leetcode.com/problems/01-matrix/discuss/363902/BFS-python-explained-and-commneted-(two-approaches)

Approach -1-
Naive BFS invoked multiple times (Slow)

Idea

    Iterate over the matrix with a nested for-loop to find cells conatining 1
    Apply BFS algo on those cells -> pass those cells to a BFS helper to find distance to closest 0
    update the matrix cell with the distance

Visuals
image

Code

def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # BFS helper #
        def bfs(node):
            from collections import deque
            q = deque()
            i, j = node
            q.append(((i,j), 0)) # d (dist to a zero) = 0 initially
            visited = set()
            dirs = [(1,0), (-1,0), (0,1), (0,-1)]
            while q:
                for i in range(len(q)):
                    coor, d = q.popleft()
                    x, y = coor
                    # if a zero nei is found
                    if matrix[x][y] == 0:
                        return d
                    visited.add(coor)
                    # investiagte neighbours
                    for dir in dirs:
                        newX, newY = x+dir[0], y+dir[1]
                        # within bounds:
                        if newX >= 0 and newX <= len(matrix)-1 and \
                            newY >= 0 and newY <= len(matrix[0])-1:
                            # not seen:
                            if (newX, newY) not in visited:
                                q.append(((newX, newY), d+1))
            return -1

        # main logic #

        steps:
            - itertate over matrix to find cells = 1
            - pass cells equaling 1 to a bfs to find the closest 0 to them
            - update matrix

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    d = bfs((i,j)) # d = closest dist to a 0
                    matrix[i][j] = d # update M with d
        return matrix

Approach -2-
Optimized BFS invoked only once (Fast)

Idea

    Instead of invoking BFS for each land cell to see how far we can get away from that source, we flip the problem.
    The flipped problem is to start from target (sea) and to figure our the closest source (land)
    This allows us to run a single BFS search that emerges from different places (all the targets aka all the zero cells) in the grid
    Add all the targets (all zero cells) into the queue. While you're at it, also mark those targets as visited (add to a visited set)
    Run a single BFS on the pre-processed queue and investigate neighbours.
    if neighbiour cell has not been visited --> then it must bea land cell (since all the sea cells have been marked visited):
        append the neighbour cell into the queue and mutate the gird

Code

visited = set()
        from collections import deque
        q = deque()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    visited.add((i,j))
                    q.append((i,j))

        while q:
            x,y = q.popleft()
            for dirr in [(1,0), (-1,0), (0,1), (0,-1)]:
                newX, newY = x+dirr[0], y+dirr[1]
                if newX >= 0 and newX <= len(matrix)-1 and newY >= 0 and newY <= len(matrix[0])-1 and (newX, newY) not in visited:
                        matrix[newX][newY] = matrix[x][y] + 1
                        visited.add((newX, newY))
                        q.append((newX, newY))
        return matrix

Similar problem:
- 1162. As Far from Land as Possible


'''






'''
2
https://leetcode.com/problems/01-matrix/discuss/1369741/C%2B%2BJavaPython-BFS-DP-solutions-with-Picture-Clean-and-Concise-O(1)-Space

 Solution 1: BFS on zero cells first

    For convinience, let's call the cell with value 0 as zero-cell, the cell has with value 1 as one-cell, the distance of the nearest 0 of a cell as distance.
    Firstly, we can see that the distance of all zero-cells are 0.
    Same idea with Topology Sort, we process zero-cells first, then we use queue data structure to keep the order of processing cells, so that cells which have the smaller distance will be processed first. Then we expand the unprocessed neighbors of the current processing cell and push into our queue.
    Afterall, we can achieve the minimum distance of all cells in our matrix.

C++

class Solution {
public:
    vector<int> DIR = {0, 1, 0, -1, 0};
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        queue<pair<int, int>> q;
        for (int r = 0; r < m; ++r)
            for (int c = 0; c < n; ++c)
                if (mat[r][c] == 0) q.emplace(r, c);
                else mat[r][c] = -1; // Marked as not processed yet!

        while (!q.empty()) {
            auto [r, c] = q.front(); q.pop();
            for (int i = 0; i < 4; ++i) {
                int nr = r + DIR[i], nc = c + DIR[i+1];
                if (nr < 0 || nr == m || nc < 0 || nc == n || mat[nr][nc] != -1) continue;
                mat[nr][nc] = mat[r][c] + 1;
                q.emplace(nr, nc);
            }
        }
        return mat;
    }
};


Java

class Solution {
    int[] DIR = new int[]{0, 1, 0, -1, 0};
    public int[][] updateMatrix(int[][] mat) {
        int m = mat.length, n = mat[0].length; // The distance of cells is up to (M+N)
        Queue<int[]> q = new ArrayDeque<>();
        for (int r = 0; r < m; ++r)
            for (int c = 0; c < n; ++c)
                if (mat[r][c] == 0) q.offer(new int[]{r, c});
                else mat[r][c] = -1; // Marked as not processed yet!

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int r = curr[0], c = curr[1];
            for (int i = 0; i < 4; ++i) {
                int nr = r + DIR[i], nc = c + DIR[i+1];
                if (nr < 0 || nr == m || nc < 0 || nc == n || mat[nr][nc] != -1) continue;
                mat[nr][nc] = mat[r][c] + 1;
                q.offer(new int[]{nr, nc});
            }
        }
        return mat;
    }
}


Python3

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        DIR = [0, 1, 0, -1, 0]

        q = deque([])
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1  # Marked as not processed yet!

        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]
                if nr < 0 or nr == m or nc < 0 or nc == n or mat[nr][nc] != -1: continue
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr, nc))
        return mat



 Solution 2: Dynamic Programming

    For convinience, let's call the cell with value 0 as zero-cell, the cell has with value 1 as one-cell, the distance of the nearest 0 of a cell as distance.
    Firstly, we can see that the distance of all zero-cells are 0, so we skip zero-cells, we process one-cells only.
    In DP, we can only use prevous values if they're already computed.
    In this problem, a cell has at most 4 neighbors that are left, top, right, bottom. If we use dynamic programming to compute the distance of the current cell based on 4 neighbors simultaneously, it's impossible because we are not sure if distance of neighboring cells is already computed or not.
    That's why, we need to compute the distance one by one:
        Firstly, for a cell, we restrict it to only 2 directions which are left and top. Then we iterate cells from top to bottom, and from left to right, we calculate the distance of a cell based on its left and top neighbors.
        Secondly, for a cell, we restrict it only have 2 directions which are right and bottom. Then we iterate cells from bottom to top, and from right to left, we update the distance of a cell based on its right and bottom neighbors.


C++

class Solution { // 48 ms, faster than 99.64%
public:
    vector<vector<int>> updateMatrix(vector<vector<int>> &mat) {
        int m = mat.size(), n = mat[0].size(), INF = m + n; // The distance of cells is up to (M+N)
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (mat[r][c] == 0) continue;
                int top = INF, left = INF;
                if (r - 1 >= 0) top = mat[r - 1][c];
                if (c - 1 >= 0) left = mat[r][c - 1];
                mat[r][c] = min(top, left) + 1;
            }
        }
        for (int r = m - 1; r >= 0; r--) {
            for (int c = n - 1; c >= 0; c--) {
                if (mat[r][c] == 0) continue;
                int bottom = INF, right = INF;
                if (r + 1 < m) bottom = mat[r + 1][c];
                if (c + 1 < n) right = mat[r][c + 1];
                mat[r][c] = min(mat[r][c], min(bottom, right) + 1);
            }
        }
        return mat;
    }
};


Java

class Solution { // 5 ms, faster than 99.66%
    public int[][] updateMatrix(int[][] mat) {
        int m = mat.length, n = mat[0].length, INF = m + n; // The distance of cells is up to (M+N)
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (mat[r][c] == 0) continue;
                int top = INF, left = INF;
                if (r - 1 >= 0) top = mat[r - 1][c];
                if (c - 1 >= 0) left = mat[r][c - 1];
                mat[r][c] = Math.min(top, left) + 1;
            }
        }
        for (int r = m - 1; r >= 0; r--) {
            for (int c = n - 1; c >= 0; c--) {
                if (mat[r][c] == 0) continue;
                int bottom = INF, right = INF;
                if (r + 1 < m) bottom = mat[r + 1][c];
                if (c + 1 < n) right = mat[r][c + 1];
                mat[r][c] = Math.min(mat[r][c], Math.min(bottom, right) + 1);
            }
        }
        return mat;
    }
}


Python3

class Solution:  # 520 ms, faster than 96.50%
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        for r in range(m):
            for c in range(n):
                if mat[r][c] > 0:
                    top = mat[r - 1][c] if r > 0 else math.inf
                    left = mat[r][c - 1] if c > 0 else math.inf
                    mat[r][c] = min(top, left) + 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if mat[r][c] > 0:
                    bottom = mat[r + 1][c] if r < m - 1 else math.inf
                    right = mat[r][c + 1] if c < n - 1 else math.inf
                    mat[r][c] = min(mat[r][c], bottom + 1, right + 1)

        return mat




'''
