withdraw, balance = input().split()

withdraw = int(withdraw)
balance = float(balance)

if withdraw % 5 == 0 and withdraw + 0.50 <= balance:
    balance -= (withdraw + 0.50)

print(f"{balance:.2f}")
