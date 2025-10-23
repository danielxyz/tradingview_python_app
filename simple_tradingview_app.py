import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import ta

# --- PARAMETER ---
symbol = "AAPL"
period = "6mo"                   # data 6 bulan
interval = "1d"                  # daily

# --- FETCH DATA ---
df = yf.download(symbol, period=period, interval=interval)
df = df.dropna()

# --- INDIKATOR (ta) ---
df['SMA20'] = ta.trend.sma_indicator(df['Close'], window=20)
df['SMA50'] = ta.trend.sma_indicator(df['Close'], window=50)
df['RSI'] = ta.momentum.RSIIndicator(df['Close'], window=14).rsi()

# --- SUPPORT/RESISTANCE (Simple Wick Clustering) ---
def find_levels(df, col, n=10, percentage=0.02):
    levels = []
    for i in range(n, len(df) - n):
        slice_ = df[col].iloc[i-n:i+n+1]
        value = slice_[n]
        # Tertinggi/terendah lokal
        if value == slice_.max() or value == slice_.min():
            # Cluster: hanya simpan level unik
            if not any(abs(value-lvl)<percentage*value for lvl in levels):
                levels.append(value)
    return levels

support = find_levels(df, col='Low', n=5, percentage=0.01)
resistance = find_levels(df, col='High', n=5, percentage=0.01)

# --- PLOT CHART CANDLESTICK ---
fig, ax = plt.subplots(figsize=(14,7))
# Candlestick manual (karena mplfinance kadang bermasalah dependencies)
up = df[df.Close >= df.Open]
down = df[df.Close < df.Open]
ax.bar(up.index, up.Close-up.Open, bottom=up.Open, color='green', width=0.8)
ax.bar(up.index, up.High-up.Close, bottom=up.Close, color='green', width=0.15)
ax.bar(up.index, up.Open-up.Low, bottom=up.Low, color='green', width=0.15)
ax.bar(down.index, down.Close-down.Open, bottom=down.Open, color='red', width=0.8)
ax.bar(down.index, down.High-down.Open, bottom=down.Open, color='red', width=0.15)
ax.bar(down.index, down.Close-down.Low, bottom=down.Low, color='red', width=0.15)

# SMA
df['SMA20'].plot(ax=ax, color='blue', linewidth=2, label='SMA 20')
df['SMA50'].plot(ax=ax, color='orange', linewidth=2, label='SMA 50')

# Support/Resistance Line
for s in support:
    ax.axhline(s, color='cyan', linestyle='--', linewidth=1, alpha=0.6, label='Support')
for r in resistance:
    ax.axhline(r, color='magenta', linestyle='--', linewidth=1, alpha=0.6, label='Resistance')

# Tampilan
ax.set_title(f"{symbol} TradingView-style Chart")
ax.legend()
plt.tight_layout()
plt.show()
