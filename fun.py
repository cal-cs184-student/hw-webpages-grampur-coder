import sys
from bisect import bisect_left
# 1. Fast Input definition
def input(): return sys.stdin.readline().rstrip()

def solve():
    # Read number of test cases
    try:
        t_str = input()
        if not t_str: return
        t = int(t_str)
    except ValueError: return

    for _ in range(t):
        try:
            # Read n (robots), m (spikes), k (instructions)
            n, m, k = map(int, input().split())
            
            # Read Robot positions
            robots = list(map(int, input().split()))
            
            # Read Spike positions
            spikes = list(map(int, input().split()))
            
            # Read Instructions string (L/R)
            instructions = input()

            # --- YOUR LOGIC STARTS HERE ---
            spikes.sort()
            close = {}
            for robot in robots:
                left = bisect_left(spikes, robot)
                left_index = robot - left
                if left_index > 0:
                    close[robot]
            # --- YOUR LOGIC ENDS HERE ---

            print(*results)

        except ValueError: break

if __name__ == "__main__":
    solve()