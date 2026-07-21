class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        total = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                total.append(matrix[i][j])
        left = 0
        right = len(total) - 1
        while left <= right:
            mid = (left + right) // 2
            if total[mid] == target:
                return True
            elif total[mid] < target:
                left = mid + 1
            elif total[mid] > target:
                right = mid - 1
        return False