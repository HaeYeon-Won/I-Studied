def solution(n,limit, data):
     dp = [[0 for _ in range(n+1)] for _ in range(limit+1)]
     for col in range(1,n+1):
          weigh = data[col-1][0]
          val = data[col-1][1]
          for row in range(1,limit+1):
               if row<weigh:
                    dp[row][col] = dp[row][col-1]
               else:
                    dp[row][col] = max(dp[row][col-1], val+dp[row-weigh][col-1])
     print(dp[l][n])

n, l = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
solution(n,l, data)
