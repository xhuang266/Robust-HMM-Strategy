import warnings
from src.data_loader import DataLoader
from src.model_engine import HMMModelEngine
from src.strategy_logic import StrategyLogic
from src.analytics import Analytics

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

def main():
    print("=== Robust HMM Strategy (Walk-Forward Validation) ===")
    
    # === Asset Universe Configuration ===
    # 1. Risk-On Assets:
    #    QQQ: Nasdaq 100 (High Beta, Tech Growth)
    #    SPY: S&P 500 (Core Asset, Defensive Growth)
    
    # 2. Risk-Off Assets:
    #    TLT: 20Y+ Treasury (Deflationary Hedge)
    #    GLD: Gold (Inflationary/Fiat Hedge)
    #    BIL: T-Bills/Cash (Ultimate Safety)
    
    # 3. Macro Signals (Feature Calculation Only):
    #    LQD: Investment Grade Corp Bonds (Smart Money)
    #    HYG: High Yield Bonds (Risk Sentiment)
    #    ^VIX: Volatility Index
    
    tickers = ['QQQ', 'SPY', 'TLT', 'GLD', 'BIL', 'LQD', 'HYG', '^VIX']
    
    # 1. Initialize Modules
    # Note: min_train_years=5 means we need 5 years of data before making the first prediction
    data_loader = DataLoader(tickers, start_date='2007-01-01')
    hmm_engine = HMMModelEngine(min_train_years=5)
    strat_logic = StrategyLogic()
    analytics = Analytics()
    
    # 2. Data Pipeline
    # Download raw data
    data_raw = data_loader.get_data()
    
    # Calculate economic features (Credit Spread Mom, VIX Mom, Tech Mom)
    data_feat = data_loader.engineer_features(data_raw)
    
    # 3. Model Training
    # Apply Walk-Forward Validation (Expanding Window) to prevent look-ahead bias
    data_wf = hmm_engine.walk_forward_training(data_feat)
    
    # 4. Strategy Execution
    # Apply Logic: State Smoothing -> Trend Filter -> Correlation Filter -> Vol Control
    res = strat_logic.execute_strategy(data_wf)
    
    # 5. Visualization & Reporting
    analytics.plot_results(res)

if __name__ == "__main__":
    main()