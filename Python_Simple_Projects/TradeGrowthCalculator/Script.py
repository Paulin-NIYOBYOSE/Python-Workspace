def calculate_months_to_target(start_balance, target_balance, win_rate, rr_ratio, trades_per_month, risk_on_each_trade):
    balance = start_balance
    months = 0

    while balance < target_balance:
        # Recalculate risk per trade based on 10% of the balance
        risk_per_trade = risk_on_each_trade * balance
        reward_per_trade = risk_per_trade * rr_ratio

        # Calculate monthly outcomes
        wins = trades_per_month * win_rate
        losses = trades_per_month * (1 - win_rate)

        # Monthly profit
        monthly_profit = (wins * reward_per_trade) - (losses * risk_per_trade)

        # Update balance
        balance += monthly_profit
        months += 1

    return months

def main():
    print("Trading Growth Calculator")
    start_balance = float(input("Enter the starting amount (e.g., 100): "))
    win_rate = float(input("Enter the win rate as a decimal (e.g., 0.5 for 50%): "))
    rr_ratio = float(input("Enter the risk-reward ratio (e.g., 2 for 1:2): "))
    trades_per_month = int(input("Enter the number of trades per month: "))
    risk_on_each_trade = float(input("Enter the risk on each trade as percentage:(eg 0.10 for 10%): "))
    target_balance = 1000  # Target balance

    months = calculate_months_to_target(
        start_balance=start_balance,
        target_balance=target_balance,
        win_rate=win_rate,
        rr_ratio=rr_ratio,
        trades_per_month=trades_per_month,
        risk_on_each_trade = risk_on_each_trade
    )

    print(f"\nIt will take {months} months to grow your account from ${start_balance:.2f} to ${target_balance:.2f}. risking 10% of the ending balance per month")

if __name__ == "__main__":
    main()
