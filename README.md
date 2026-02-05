# Robust HMM Systematic Macro Strategy with Walk-Forward Validation

## Overview
This project implements a **Regime-Switching Multi-Asset Strategy** utilizing **Gaussian Hidden Markov Models (HMM)**. 

Unlike standard "fit-and-predict" models, this engine enforces strict **Walk-Forward Validation** (Expanding Window) to eliminate look-ahead bias. It dynamically adapts to changing market conditions by identifying **Bull**, **Bear**, and **Sideways** regimes using macroeconomic leading indicators.

## Key Features

### 1. Zero Look-Ahead Bias (Walk-Forward)
The model retrains annually using an **expanding window**. 
* *Example:* To predict the regime for 2015, the model is trained *only* on data from 2007-2014. Future data is never leaked into the standardization (Scaler) or training process.

### 2. Macro-Economic Feature Engineering
Instead of relying solely on technical indicators (like RSI), the HMM clusters regimes based on structural market drivers:
* **Credit Spread Momentum (LQD/HYG):** Measures "Smart Money" risk appetite.
* **VIX Momentum:** Captures the acceleration of panic.
* **Tech Momentum (QQQ):** Gauges the strength of the growth factor.

### 3. Robust Filtering Layers
Raw HMM outputs are noisy. This engine applies three engineering layers to stabilize signals:
* **State Smoothing:** Uses a 3-day rolling median to prevent "state flickering."
* **Trend Confirmation:** Downgrades exposure from QQQ to SPY if prices break below the 100-day Moving Average.
* **The "2022 Inflation Filter":** Monitors the **Stock-Bond Correlation**. 
    * If Correlation > 0 (Inflationary Crisis), it abandons Treasuries (TLT) in favor of Gold (GLD) and Cash (BIL).

### 4. Risk Control
* **Volatility Targeting:** Dynamically adjusts leverage to target 25% annualized volatility.
* **Financing Cost:** Accounts for the cost of leverage (Risk-Free Rate) and transaction slippage.

## Project Structure

```text
Robust-HMM-Strategy/
├── src/                     # Core Source Code
│   ├── data_loader.py       # Data download & Feature Engineering
│   ├── model_engine.py      # HMM Training & Walk-Forward Logic
│   ├── strategy_logic.py    # Signal Generation & Position Management
│   └── analytics.py         # Performance Reporting & Plotting
├── main.py                  # Execution Entry Point
├── requirements.txt         # Dependencies
└── README.md                # Documentation