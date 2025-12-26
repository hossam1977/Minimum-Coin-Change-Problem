import time
import math

def Optimized_Coin_Change(coins, amount):
    DP = [math.inf] * (amount + 1)
    DP[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                DP[i] = min(DP[i], DP[i - coin] + 1)

    if DP[amount] == math.inf:
        return -1
    else:
        return DP[amount]

coins = [int(x) for x in input("Coins (e.g., 1,2,5): ").split(",")]
amount = int(input("Amount: "))

t0 = time.time()
ans = Optimized_Coin_Change(coins, amount)
t1 = time.time()

print(f"Result: {ans} | Time(s): {t1 - t0:.6f}")

