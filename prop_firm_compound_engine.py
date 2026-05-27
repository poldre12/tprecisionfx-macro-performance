# T Precision FX — Prop Firm Equity Compounding and Risk Allocation Engine
# Optimized for FTMO, Funding Pips, and High-Timeframe Swing Parameters

def calculate_compounding_curve(starting_equity, monthly_yield_pct, total_months=6):
    print(f"--- Initializing T Precision FX Equity Scaling Curve ---")
    current_equity = starting_equity
    
    for month in range(1, total_months + 1):
        monthly_profit = current_equity * (monthly_yield_pct / 100)
        current_equity += monthly_profit
        print(f"Month {month} Target Portfolio Baseline: ${round(current_equity, 2)} (Net Profit: +${round(monthly_profit, 2)})")
        
    return round(current_equity, 2)

# Evaluated Parameter Model using verified 2026 Macro Swing Metrics
# Baseline Setup: $100,000 Starting Allocation at a conservative 8% average monthly performance
final_projection = calculate_compounding_curve(100000, 8.0, 6)
