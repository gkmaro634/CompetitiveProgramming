#!/usr/bin/env python3
import numpy as np
import bisect
import heapq
import sys
from collections import deque

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(120000)

# def dfs(G, pos, visited):
#     visited[pos] = True
#     for node in G[pos]:
#         if visited[node] == False:
#             dfs(G, node, visited)

def resolve(N, M, edges):
    """
    問題固有のメソッド。引数や戻り値は問題によって変える。
    """
    G = [[] for i in range(N+1)]
    for a, b in edges:
        G[a].append(b)
        G[b].append(a)

    # 幅優先
    # visited = [False] * (N+1)
    path_l = [-1] * (N+1)
    to_visit = deque()
    to_visit.append(1)
    while len(to_visit) > 0:
        pos = to_visit.popleft()
        # visited[pos] = True
        path_l[pos] += 1
        for node in G[pos]:
            if path_l[node] == -1:
                path_l[node] = path_l[pos]
                to_visit.append(node)
    return path_l

def execute():
    """
    pytestでの呼び出しを想定したメソッドである。
    """

    # read single value
    # N = int(input())

    # read splitted two values
    # H, W = list(map(int, input().split()))
    # M, N = list(map(int, input().split()))

    # read values
    # A = list(map(int, input().split()))

    # read 2d values
    # M = [list(map(int, input().split())) for i in range(N)]

    N, M = list(map(int, input().split()))
    edges = [list(map(int, input().split())) for i in range(M)]
    ret = resolve(N, M, edges)
    for i in range(1, N+1):
        print(ret[i])
    # print(ret)
        
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