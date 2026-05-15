class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        # 1d arr
        l, r = 0, rows*cols-1

        while l <= r:
            mid = (l+r)//2
            row,col = mid//cols, mid%cols
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                l = mid+1
            else:
                r = mid-1
        return False