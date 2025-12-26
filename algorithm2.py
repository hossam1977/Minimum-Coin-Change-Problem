import time

def dp_min(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if c <= i:
                dp[i] = min(dp[i], dp[i - c] + 1)
    return -1 if dp[amount] > amount else dp[amount]

coins = [int(x) for x in input("Coins (e.g., 1,2,5): ").split(",")]
amount = int(input("Amount: "))

t0 = time.time()
ans = dp_min(coins, amount)
t1 = time.time()

print(f"Result: {ans} | Time(s): {t1 - t0:.6f}")
