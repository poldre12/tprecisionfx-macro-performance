# T Precision FX - Institutional Position Size & Risk Calculator
def calculate_position_size(account_balance, risk_percentage, stop_loss_pips, pip_value=10):
    amount_to_risk = account_balance * (risk_percentage / 100)
    lot_size = amount_to_risk / (stop_loss_pips * pip_value)
    return round(lot_size, 2)

# Example parameters for a standard 100k Prop Firm Challenge
print("Recommended Lot Size:", calculate_position_size(100000, 1.0, 30))
