#!/usr/bin/env python3
import numpy as np

def resolve(N, K, A):
    """
    問題固有のメソッド。引数や戻り値は問題によって変える。
    """

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
    """
    pytestでの呼び出しを想定したメソッドである。
    """

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
        # launch.jsonで第1引数にDEBUGを渡すように設定している
        # ローカル実行環境の場合のみここを通る
        import os
        from pathlib import Path
        import utils
        data_dir = Path(__file__).parent.parent
        fpath = os.path.join(data_dir, "handinput.txt")
        utils.replace_stdin(fpath)

    execute()