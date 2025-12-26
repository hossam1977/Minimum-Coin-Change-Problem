import time, sys
sys.setrecursionlimit(2000)

INF = float("inf")

def Naive_Coin_Change(coins, amount):
    if amount == 0: return 0
    if amount < 0:  return INF
    min_coins = INF
    for coin in coins:
        result = Naive_Coin_Change(coins, amount - coin)
        if result != INF:
            min_coins = min(min_coins, result + 1)
    return min_coins

coins = [int(x) for x in input("Coins (e.g., 1,2,5): ").split(",")]
amount = int(input("Amount: "))

t0 = time.time()
ans = Naive_Coin_Change(coins, amount)
t1 = time.time()

ans = -1 if ans == INF else ans
print(f"Result: {ans} | Time(s): {t1 - t0:.6f}")
