import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import ta

# --- PARAMETER ---
symbol = "AAPL"
period = "6mo"                   # data 6 bulan
interval = "1d"                  # daily

# --- FETCH DATA ---
print(f"Fetching data for {symbol}...")
df = yf.download(symbol, period=period, interval=interval)

# FIX: Flatten MultiIndex columns jika ada
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)

df = df.dropna()
print(f"Data loaded: {len(df)} rows")

# --- INDIKATOR (ta) ---
print("Calculating indicators...")
# Extract close price sebagai Series 1D
close_price = df['Close'].squeeze()

df['SMA20'] = ta.trend.sma_indicator(close_price, window=20)
df['SMA50'] = ta.trend.sma_indicator(close_price, window=50)
df['RSI'] = ta.momentum.RSIIndicator(close_price, window=14).rsi()

# --- SUPPORT/RESISTANCE (Simple Wick Clustering) ---
print("Detecting support/resistance levels...")
def find_levels(df, col, n=10, percentage=0.02):
    levels = []
    values = df[col].values
    for i in range(n, len(values) - n):
        slice_ = values[i-n:i+n+1]
        value = values[i]
        # Tertinggi/terendah lokal
        if value == slice_.max() or value == slice_.min():
            # Cluster: hanya simpan level unik
            if not any(abs(value-lvl)<percentage*value for lvl in levels):
                levels.append(value)
    return levels

support = find_levels(df, col='Low', n=5, percentage=0.01)
resistance = find_levels(df, col='High', n=5, percentage=0.01)

print(f"Found {len(support)} support levels and {len(resistance)} resistance levels")

# --- PLOT CHART CANDLESTICK ---
print("Generating chart...")
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14,9), gridspec_kw={'height_ratios': [3, 1]})

# Candlestick manual
up = df[df['Close'] >= df['Open']]
down = df[df['Close'] < df['Open']]

# Plot candlestick - Bullish (green)
ax1.bar(up.index, up['Close']-up['Open'], bottom=up['Open'], color='green', width=0.8)
ax1.bar(up.index, up['High']-up['Close'], bottom=up['Close'], color='green', width=0.15)
ax1.bar(up.index, up['Open']-up['Low'], bottom=up['Low'], color='green', width=0.15)

# Plot candlestick - Bearish (red)
ax1.bar(down.index, down['Close']-down['Open'], bottom=down['Open'], color='red', width=0.8)
ax1.bar(down.index, down['High']-down['Open'], bottom=down['Open'], color='red', width=0.15)
ax1.bar(down.index, down['Close']-down['Low'], bottom=down['Low'], color='red', width=0.15)

# SMA
ax1.plot(df.index, df['SMA20'], color='blue', linewidth=2, label='SMA 20')
ax1.plot(df.index, df['SMA50'], color='orange', linewidth=2, label='SMA 50')

# Support/Resistance Lines
for idx, s in enumerate(support[:5]):  # Max 5 levels untuk clarity
    ax1.axhline(s, color='cyan', linestyle='--', linewidth=1, alpha=0.6, 
                label='Support' if idx == 0 else '')
for idx, r in enumerate(resistance[:5]):  # Max 5 levels
    ax1.axhline(r, color='magenta', linestyle='--', linewidth=1, alpha=0.6, 
                label='Resistance' if idx == 0 else '')

# Tampilan Chart
ax1.set_title(f"{symbol} - TradingView Style Analysis (Multi-Timeframe)", fontsize=16, fontweight='bold')
ax1.set_ylabel('Price (USD)', fontsize=12)
ax1.legend(loc='upper left')
ax1.grid(True, alpha=0.3)

# RSI Subplot
ax2.plot(df.index, df['RSI'], color='purple', linewidth=1.5, label='RSI(14)')
ax2.axhline(70, color='red', linestyle='--', linewidth=1, alpha=0.5)
ax2.axhline(30, color='green', linestyle='--', linewidth=1, alpha=0.5)
ax2.fill_between(df.index, 30, 70, alpha=0.1, color='gray')
ax2.set_ylabel('RSI', fontsize=12)
ax2.set_xlabel('Date', fontsize=12)
ax2.legend(loc='upper left')
ax2.grid(True, alpha=0.3)
ax2.set_ylim(0, 100)

plt.tight_layout()
print("Chart ready! Close the window to exit.")
plt.show()

print(f"\n{'='*60}")
print(f"ANALYSIS SUMMARY - {symbol}")
print(f"{'='*60}")
print(f"Period: {period} | Interval: {interval}")
print(f"Current Price: ${df['Close'].iloc[-1]:.2f}")
print(f"SMA20: ${df['SMA20'].iloc[-1]:.2f}")
print(f"SMA50: ${df['SMA50'].iloc[-1]:.2f}")
print(f"RSI: {df['RSI'].iloc[-1]:.2f}")
print(f"\nSupport Levels (Top 3): {[f'${s:.2f}' for s in support[:3]]}")
print(f"Resistance Levels (Top 3): {[f'${r:.2f}' for r in resistance[:3]]}")
print(f"{'='*60}")
