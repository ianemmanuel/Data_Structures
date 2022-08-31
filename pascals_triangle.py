class Solution:
    def pascals_triangle(self,num_rows):
        res = [[1]]

        for i in range(num_rows-1):
            temp = [0] + res[-1]+[0]
            row = []

            for j in range(len(res[-1])+1):
                row.append(temp[j] + temp[j+1])
            res.append(row)
        return res

if __name__ == '__main__':
    pascals = Solution()
    print(pascals.pascals_triangle(num_rows=5))






