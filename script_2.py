
# Buat diagram arsitektur sistem dengan komponen utama
architecture_data = {
    "Layer": [
        "Presentation Layer",
        "Presentation Layer", 
        "Presentation Layer",
        "Business Logic Layer",
        "Business Logic Layer",
        "Business Logic Layer",
        "Business Logic Layer",
        "Business Logic Layer",
        "Data Layer",
        "Data Layer",
        "Data Layer",
        "Infrastructure Layer",
        "Infrastructure Layer",
        "Infrastructure Layer"
    ],
    "Component": [
        "Chart Visualization (lightweight-charts-python)",
        "User Interface / Dashboard",
        "Event Markers & Alerts",
        "Multi-Timeframe Analysis Engine",
        "Technical Indicators Calculator",
        "Support/Resistance Detector",
        "Signal Generation Module",
        "Risk Management Module",
        "Data Acquisition Module (yfinance/API)",
        "Data Storage (pandas DataFrame)",
        "Real-time Data Handler (WebSocket)",
        "Event-Driven Architecture",
        "Logging & Monitoring",
        "Deployment (Docker/Cloud)"
    ],
    "Technology": [
        "lightweight-charts, HTML/JavaScript",
        "Flask/FastAPI/Streamlit",
        "Custom Event System",
        "pandas resample, custom logic",
        "pandas_ta, TA-Lib, numpy",
        "trendln, pytrendline, custom algo",
        "Rule-based / ML model",
        "Position tracking, stop-loss logic",
        "yfinance, ccxt, requests",
        "pandas, numpy, sqlite3",
        "websocket-client, asyncio",
        "Python Queue, threading",
        "loguru, prometheus",
        "Docker, AWS/GCP, systemd"
    ],
    "Responsibility": [
        "Display candlestick, indicators, S/R levels",
        "User interaction, parameter input",
        "Show buy/sell signals, price alerts",
        "Analyze across weekly/daily/hourly timeframes",
        "Calculate SMA/EMA/RSI/MACD/Pivots",
        "Find strong support/resistance levels",
        "Generate buy/sell/hold signals",
        "Manage position size, risk limits",
        "Fetch historical OHLCV data from sources",
        "Store and process market data",
        "Stream live price updates",
        "Trigger actions on events (new data/signal)",
        "Track performance, errors, system health",
        "Host and run application 24/7"
    ]
}

df_architecture = pd.DataFrame(architecture_data)

# Save to CSV
df_architecture.to_csv("arsitektur_sistem_tradingview.csv", index=False, encoding='utf-8-sig')
print("Arsitektur sistem berhasil dibuat!")
print("\nPreview Arsitektur:")
print(df_architecture.to_string(index=False))
