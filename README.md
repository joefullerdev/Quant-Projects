# Quant Projects Repository

## **Project 1)** SMA Crossover Strategy with Backtest (SMA-Model)

This is my first quant related project, so I'd thought I would start off with something simple.

This model firstly calculates the 10 day and 20 day moving averages for a 10 year history of the Microsoft Stock (MSFT).
If the 10 day moving average crosses above the 20 day moving average, then we buy MSFT and go long. If the 20 day moving average crosses
above the 10 day moving average then we sell MSFT and go short.

The data for MSFT has come from the **yfinance** library.
For the backtesting, we are using the **backtesting** library.

To see the interactive chart, simply download **SMACross.html** and open it from your file explorer.
