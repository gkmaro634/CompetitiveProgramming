#!/usr/bin/env python3
import numpy as np

def resolve(N, K, A):
    MOD = 10 ** 9+7

    dp = [[0] * (K+1) for i in range(N+1)]
    sum_dp = [[0] * (K+2) for i in range(N+1)]

    dp[0][0] = 1

    for i in range(0, N):
        for j in range(0, K+1):
            sum_dp[i][j+1] = (sum_dp[i][j] + dp[i][j]) % MOD

        for j in range(0, K+1):
            dp[i+1][j] = (sum_dp[i][j+1] - sum_dp[i][max(j - A[i], 0)]) % MOD

    return dp[N][K]

def execute():
    # read single value
    # N = int(input())

    # read splitted two values
    # H, W = list(map(int, input().split()))

    # read values
    # A = list(map(int, input().split()))

    # read 2d values
    # M = [list(map(int, input().split())) for i in range(N)]

    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    ret = resolve(N, K, A)
    print(ret)
        
    return f"{ret}"

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "DEBUG":
        import os
        from pathlib import Path
        import utils
        data_dir = Path(__file__).parent
        fpath = os.path.join(data_dir, "handinput.txt")
        utils.replace_stdin(fpath)

    execute()