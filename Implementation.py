import time
import sys

sys.setrecursionlimit(2000)

def coin_change_naive(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')

    min_coins = float('inf')
    for coin in coins:
        result = coin_change_naive(coins, amount - coin)
        if result != float('inf'):
            min_coins = min(min_coins, 1 + result)
    
    return min_coins

def coin_change_optimized(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], 1 + dp[i - coin])

    return dp[amount] if dp[amount] <= amount else -1

# --- Main Execution Block ---
def main():
    print("=== Algorithm Analysis & Design Project: Coin Change ===")
    try:

        coins_input = input("Enter coin denominations separated by commas (e.g., 1,5,10,25): ")
        coins_list = [int(c.strip()) for c in coins_input.split(',')]
        
        target_amount = int(input("Enter the target amount: "))

        print("\n[Running Optimized Algorithm...]")
        start_opt = time.time()
        opt_res = coin_change_optimized(coins_list, target_amount)
        end_opt = time.time()
        opt_time = end_opt - start_opt

        print(f"[Running Naive Algorithm... (Warning: May be slow for large amounts)]")
        start_naive = time.time()
        naive_res = coin_change_naive(coins_list, target_amount)
        if naive_res == float('inf'): naive_res = -1
        end_naive = time.time()
        naive_time = end_naive - start_naive

        print("\n" + "="*50)
        print(f"{'Algorithm':<20} | {'Result':<10} | {'Execution Time (s)':<20}")
        print("-" * 50)
        print(f"{'Naive (Recursive)':<20} | {naive_res:<10} | {naive_time:.6f}")
        print(f"{'Optimized (DP)':<20} | {opt_res:<10} | {opt_time:.6f}")
        print("="*50)
        
        if opt_time > 0:
            print(f"Efficiency Gain: Optimized is {naive_time/opt_time:.2f}x faster.")

    except ValueError:
        print("Error: Please enter valid integers.")
    except RecursionError:
        print("Error: Amount too large for the Naive algorithm's recursion limit.")

if __name__ == "__main__":
    main()