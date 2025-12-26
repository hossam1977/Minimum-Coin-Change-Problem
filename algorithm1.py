import time, sys
sys.setrecursionlimit(2000)

INF = float("inf")

def naive(coins, amount):
    if amount == 0: return 0
    if amount < 0:  return INF
    best = INF
    for c in coins:
        res = naive(coins, amount - c)
        if res != INF:
            best = min(best, res + 1)
    return best

coins = [int(x) for x in input("Coins (e.g., 1,2,5): ").split(",")]
amount = int(input("Amount: "))

t0 = time.time()
ans = naive(coins, amount)
t1 = time.time()

ans = -1 if ans == INF else ans
print(f"Result: {ans} | Time(s): {t1 - t0:.6f}")

    main()
