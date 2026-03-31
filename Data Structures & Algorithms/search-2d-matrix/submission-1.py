class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            if target <= matrix[i][n -1]:
                l, r = 0, n - 1
                while l <= r:
                    mid = (l + r) // 2
                    if matrix[i][mid] > target:
                        r = mid - 1
                    elif matrix[i][mid] < target:
                        l = mid + 1
                    else:
                        return True
        
        return False
        
        