
# Buat contoh kode Python lengkap untuk aplikasi TradingView
code_example = """
#================================================================
# APLIKASI TRADINGVIEW PYTHON 3.14 - TRENDLINE & SUPPORT/RESISTANCE
# Multi-Timeframe Top-Down Analysis dengan Indikator Kuat
#================================================================

import pandas as pd
import numpy as np
import yfinance as yf
from lightweight_charts import Chart
import pandas_ta as ta
from datetime import datetime, timedelta

#================================================================
# 1. DATA ACQUISITION MODULE
#================================================================
class DataModule:
    def __init__(self, symbol, start_date, end_date):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.data = None
    
    def fetch_data(self):
        \"\"\"Fetch historical OHLCV data from Yahoo Finance\"\"\"
        print(f"Fetching data for {self.symbol}...")
        self.data = yf.download(self.symbol, start=self.start_date, end=self.end_date)
        print(f"Data fetched: {len(self.data)} rows")
        return self.data

#================================================================
# 2. TECHNICAL INDICATORS MODULE
#================================================================
class IndicatorsModule:
    @staticmethod
    def calculate_sma(df, periods=[20, 50, 200]):
        \"\"\"Calculate Simple Moving Averages\"\"\"
        for period in periods:
            df[f'SMA_{period}'] = df['Close'].rolling(window=period).mean()
        return df
    
    @staticmethod
    def calculate_ema(df, periods=[13, 21, 34, 55, 89]):
        \"\"\"Calculate Exponential Moving Averages (Fibonacci)\"\"\"
        for period in periods:
            df[f'EMA_{period}'] = df['Close'].ewm(span=period, adjust=False).mean()
        return df
    
    @staticmethod
    def calculate_rsi(df, period=14):
        \"\"\"Calculate RSI indicator\"\"\"
        df['RSI'] = ta.rsi(df['Close'], length=period)
        return df
    
    @staticmethod
    def calculate_macd(df):
        \"\"\"Calculate MACD indicator\"\"\"
        macd = ta.macd(df['Close'])
        df = pd.concat([df, macd], axis=1)
        return df
    
    @staticmethod
    def calculate_pivot_points(df):
        \"\"\"Calculate Pivot Points for Support/Resistance\"\"\"
        df['Pivot'] = (df['High'] + df['Low'] + df['Close']) / 3
        df['R1'] = 2 * df['Pivot'] - df['Low']
        df['S1'] = 2 * df['Pivot'] - df['High']
        df['R2'] = df['Pivot'] + (df['High'] - df['Low'])
        df['S2'] = df['Pivot'] - (df['High'] - df['Low'])
        return df

#================================================================
# 3. MULTI-TIMEFRAME ANALYSIS ENGINE
#================================================================
class MultiTimeframeEngine:
    def __init__(self, data):
        self.data = data
        self.timeframes = {}
    
    def resample_data(self, timeframes=['1W', '1D', '4H', '1H']):
        \"\"\"Resample data to multiple timeframes\"\"\"
        for tf in timeframes:
            resampled = self.data.resample(tf).agg({
                'Open': 'first',
                'High': 'max',
                'Low': 'min',
                'Close': 'last',
                'Volume': 'sum'
            })
            self.timeframes[tf] = resampled.dropna()
        return self.timeframes
    
    def get_timeframe(self, tf):
        \"\"\"Get specific timeframe data\"\"\"
        return self.timeframes.get(tf, None)

#================================================================
# 4. SUPPORT/RESISTANCE DETECTION MODULE
#================================================================
class SupportResistanceDetector:
    def __init__(self, df, threshold=0.02):
        self.df = df
        self.threshold = threshold
        self.support_levels = []
        self.resistance_levels = []
    
    def detect_wick_levels(self):
        \"\"\"Detect support/resistance based on long wicks\"\"\"
        for i in range(1, len(self.df) - 1):
            # Long lower wick = potential support
            lower_wick = self.df['Low'].iloc[i] - min(self.df['Open'].iloc[i], self.df['Close'].iloc[i])
            body = abs(self.df['Close'].iloc[i] - self.df['Open'].iloc[i])
            
            if lower_wick > 2 * body:
                self.support_levels.append(self.df['Low'].iloc[i])
            
            # Long upper wick = potential resistance
            upper_wick = self.df['High'].iloc[i] - max(self.df['Open'].iloc[i], self.df['Close'].iloc[i])
            
            if upper_wick > 2 * body:
                self.resistance_levels.append(self.df['High'].iloc[i])
        
        return self.cluster_levels()
    
    def cluster_levels(self):
        \"\"\"Cluster nearby levels and calculate strength\"\"\"
        def cluster(levels):
            if not levels:
                return []
            levels = sorted(levels)
            clusters = []
            current_cluster = [levels[0]]
            
            for level in levels[1:]:
                if abs(level - current_cluster[-1]) / current_cluster[-1] < self.threshold:
                    current_cluster.append(level)
                else:
                    clusters.append({
                        'level': np.mean(current_cluster),
                        'strength': len(current_cluster)
                    })
                    current_cluster = [level]
            
            clusters.append({
                'level': np.mean(current_cluster),
                'strength': len(current_cluster)
            })
            return sorted(clusters, key=lambda x: x['strength'], reverse=True)
        
        return {
            'support': cluster(self.support_levels),
            'resistance': cluster(self.resistance_levels)
        }

#================================================================
# 5. SIGNAL GENERATION MODULE
#================================================================
class SignalGenerator:
    def __init__(self, df):
        self.df = df
    
    def generate_signals(self):
        \"\"\"Generate buy/sell signals based on multi-indicator confirmation\"\"\"
        self.df['Signal'] = 0
        
        # Buy Signal: SMA20 > SMA50, RSI < 70, MACD bullish
        buy_condition = (
            (self.df['SMA_20'] > self.df['SMA_50']) &
            (self.df['RSI'] < 70) &
            (self.df['MACD_12_26_9'] > self.df['MACDs_12_26_9'])
        )
        
        # Sell Signal: SMA20 < SMA50, RSI > 30, MACD bearish
        sell_condition = (
            (self.df['SMA_20'] < self.df['SMA_50']) &
            (self.df['RSI'] > 30) &
            (self.df['MACD_12_26_9'] < self.df['MACDs_12_26_9'])
        )
        
        self.df.loc[buy_condition, 'Signal'] = 1
        self.df.loc[sell_condition, 'Signal'] = -1
        
        return self.df

#================================================================
# 6. CHART VISUALIZATION MODULE
#================================================================
class ChartVisualizer:
    def __init__(self, df, title='TradingView Chart'):
        self.df = df
        self.chart = Chart()
        self.title = title
    
    def plot_candlestick(self):
        \"\"\"Plot candlestick chart with TradingView style\"\"\"
        self.chart.set(self.df)
        return self
    
    def add_sma_lines(self):
        \"\"\"Add SMA lines to chart\"\"\"
        if 'SMA_20' in self.df.columns:
            self.chart.lines.SMA20 = self.df['SMA_20']
        if 'SMA_50' in self.df.columns:
            self.chart.lines.SMA50 = self.df['SMA_50']
        return self
    
    def show(self):
        \"\"\"Display the chart\"\"\"
        self.chart.show(block=True)

#================================================================
# 7. MAIN APPLICATION CLASS
#================================================================
class TradingViewApp:
    def __init__(self, symbol='AAPL', days_back=365):
        self.symbol = symbol
        self.end_date = datetime.now()
        self.start_date = self.end_date - timedelta(days=days_back)
        self.data = None
        self.indicators = None
    
    def run(self):
        \"\"\"Run the complete trading application\"\"\"
        print("="*60)
        print("APLIKASI TRADINGVIEW PYTHON - MULTI-TIMEFRAME ANALYSIS")
        print("="*60)
        
        # Step 1: Fetch Data
        data_module = DataModule(self.symbol, self.start_date, self.end_date)
        self.data = data_module.fetch_data()
        
        # Step 2: Calculate Indicators
        print("\\nCalculating indicators...")
        indicator_module = IndicatorsModule()
        self.data = indicator_module.calculate_sma(self.data)
        self.data = indicator_module.calculate_ema(self.data)
        self.data = indicator_module.calculate_rsi(self.data)
        self.data = indicator_module.calculate_macd(self.data)
        self.data = indicator_module.calculate_pivot_points(self.data)
        
        # Step 3: Multi-Timeframe Analysis
        print("\\nPerforming multi-timeframe analysis...")
        mtf_engine = MultiTimeframeEngine(self.data)
        timeframes = mtf_engine.resample_data(['1W', '1D', '4H'])
        
        # Step 4: Detect Support/Resistance
        print("\\nDetecting support/resistance levels...")
        sr_detector = SupportResistanceDetector(self.data)
        sr_levels = sr_detector.detect_wick_levels()
        
        print(f"\\nStrong Support Levels: {sr_levels['support'][:3]}")
        print(f"Strong Resistance Levels: {sr_levels['resistance'][:3]}")
        
        # Step 5: Generate Signals
        print("\\nGenerating trading signals...")
        signal_gen = SignalGenerator(self.data)
        self.data = signal_gen.generate_signals()
        
        # Step 6: Visualize
        print("\\nGenerating TradingView chart...")
        visualizer = ChartVisualizer(self.data, title=f'{self.symbol} - Multi-Timeframe Analysis')
        visualizer.plot_candlestick().add_sma_lines().show()
        
        print("\\n" + "="*60)
        print("Analysis completed!")
        print("="*60)

#================================================================
# 8. RUN THE APPLICATION
#================================================================
if __name__ == "__main__":
    # Initialize and run the app
    app = TradingViewApp(symbol='AAPL', days_back=365)
    app.run()
"""

# Save the code to a file
with open("tradingview_app_complete.py", "w", encoding='utf-8') as f:
    f.write(code_example)

print("File kode Python lengkap berhasil dibuat: tradingview_app_complete.py")
print("\n" + "="*70)
print("STRUKTUR KODE:")
print("="*70)
print("""
1. DataModule - Fetch data dari Yahoo Finance
2. IndicatorsModule - Hitung SMA, EMA, RSI, MACD, Pivot Points
3. MultiTimeframeEngine - Resample ke berbagai timeframe
4. SupportResistanceDetector - Deteksi level S/R dengan wick detection
5. SignalGenerator - Generate sinyal buy/sell
6. ChartVisualizer - Visualisasi TradingView-style
7. TradingViewApp - Main application class
8. Main execution - Run the app

Total: ~250+ lines kode modular dan profesional
""")
