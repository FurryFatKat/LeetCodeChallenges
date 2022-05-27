# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
#
# You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].
#
# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.
#
# Return the modified image after performing the flood fill.
#
#
#
# Example 1:
#
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
#
# Example 2:
#
# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
# Output: [[2,2,2],[2,2,2]]



# https://leetcode.com/problems/flood-fill/discuss/109604/Easy-Python-DFS-(no-need-for-visited)!!!
# The idea is simple. Simply perform a DFS on the source cell. Continue the DFS if:
#
#     Next cell is within bounds.
#     Next cell is the same color as source cell.
#
# There is a tricky case where the new color is the same as the original color and if the DFS is done on it, there will be an infinite loop. If new color is same as original color, there is nothing to be done and we can simply return the image.
#
# 💯 Check out https://www.techinterviewhandbook.org for more tips and tricks by me to ace your coding interview 💯
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows, cols, same_color = len(image), len(image[0]), image[sr][sc]
        def traverse(row, col):
            if (not (0 <= row < rows and 0 <= col < cols)) or image[row][col] != same_color:
                return
            image[row][col] = newColor
            [traverse(row + x, col + y) for (x, y) in ((0, 1), (1, 0), (0, -1), (-1, 0))]
        if same_color != newColor:
            traverse(sr, sc)
        return image



# https://leetcode.com/problems/flood-fill/discuss/187701/Python-nice-and-clean-DFS-and-BFS-solutions
#    BFS

class Solution2:
    def floodFill(self, image, sr, sc, newColor):
        old, m, n = image[sr][sc], len(image), len(image[0])
        if old != newColor:
            q = collections.deque([(sr, sc)])
            while q:
                i, j = q.popleft()
                image[i][j] = newColor
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and image[x][y] == old:
                        q.append((x, y))
        return image

#    DFS

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        def dfs(i, j):
            image[i][j] = newColor
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and image[x][y] == old:
                    dfs(x, y)
        old, m, n = image[sr][sc], len(image), len(image[0])
        if old != newColor:
            dfs(sr, sc)
        return image

'''
C++ solution
https://leetcode.com/problems/flood-fill/discuss/1590584/C%2B%2B-oror-Simple-DFS-oror-97.6-faster-oror-91.6-better-memory-Use

class Solution {
public:

    void dfs(vector<vector<int>>& image, int i, int j,int val, int newColor)
    {
        if(i<0 || i>=image.size() || j<0 || j>= image[0].size() || image[i][j] == newColor || image[i][j] != val)
        {
            return;
        }
        image[i][j] = newColor;
        dfs(image,i-1,j,val,newColor);
        dfs(image,i+1,j,val,newColor);
        dfs(image,i,j-1,val,newColor);
        dfs(image,i,j+1,val,newColor);
    }

    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor)
    {
        int val = image[sr][sc];
        dfs(image,sr,sc,val,newColor);
        return image;
    }
};
# IF THIS CODE  IS HELPFUL TO YOU THEN  PLEASE UPVOTE!!!


'''
