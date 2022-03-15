"""
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.
"""
def solution(data):
    fL = len(data[0])+1
    sL = len(data[1])+1
    dp = [[0 for _ in range(sL)] for _ in range(fL)]
    for i in range(1, fL):
        for j in range(1, sL):
            if data[0][i-1]==data[1][j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]
if __name__=="__main__":
    data = [input() for _ in range(2)]
    print(solution(data))

"""
string1[n]==string2[k] 라면 dp[n][k] = [n-1][k-1]+1
다르다면 dp[n][k] = max(dp[n-1][k], dp[n][k-1])
"""
