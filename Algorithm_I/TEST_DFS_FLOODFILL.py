image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
rows, cols = len(image), len(image[0])
same_color = image[sr][sc]

def traverse(row, col):
    print(row, col)
    if (not (0<=row < rows and 0 <= col < cols)) or image[row][col] != same_color:
        return
    image[row][col] = newColor
    print(image[0])
    print(image[1])
    print(image[2])
    [traverse(row + x, col + y) for (x, y) in ((0, 1), (1, 0), (0, -1), (-1, 0))]

def floodFill(image, sr, sc, newColor):
    rows, cols = len(image), len(image[0])
    same_color = image[sr][sc]
    if same_color != newColor:
        print(image)
        traverse(sr, sc)
    return image

if __name__ == '__main__':
    floodFill(image, sr, sc, newColor)
