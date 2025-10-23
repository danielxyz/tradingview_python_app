
# Buat file requirements.txt lengkap untuk instalasi semua dependencies
requirements = """# ================================================================
# REQUIREMENTS.TXT - Aplikasi TradingView Python 3.14
# ================================================================
# Install dengan: pip install -r requirements.txt
# ================================================================

# Data Acquisition
yfinance>=0.2.49
requests>=2.32.0
ccxt>=4.4.0

# Data Processing
pandas>=2.2.0
numpy>=1.26.0

# Technical Analysis
pandas-ta>=0.3.14b
TA-Lib>=0.4.32

# Chart Visualization
lightweight-charts>=2.0.0

# Support/Resistance Detection
trendln>=0.4.0

# Async & Real-time
websocket-client>=1.8.0
aiohttp>=3.10.0

# Utility
python-dateutil>=2.9.0
pytz>=2024.1

# Logging
loguru>=0.7.0

# Testing (Optional)
pytest>=8.3.0
backtesting>=0.3.3

# Web Framework (Optional - untuk dashboard)
flask>=3.0.0
streamlit>=1.39.0
"""

with open("requirements.txt", "w", encoding='utf-8') as f:
    f.write(requirements)

print("File requirements.txt berhasil dibuat!")
print("\n" + "="*70)
print("LANGKAH-LANGKAH INSTALASI:")
print("="*70)
print("""
STEP 1: Install semua dependencies
---------------------------------------
pip install -r requirements.txt

ATAU install satu per satu:
---------------------------------------
pip install yfinance pandas numpy pandas-ta lightweight-charts trendln

STEP 2: Jika TA-Lib gagal install (sering terjadi di Windows)
---------------------------------------
- Download wheel file dari: https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib
- Pilih file sesuai Python version & OS (contoh: TA_Lib‑0.4.32‑cp314‑cp314‑win_amd64.whl)
- Install: pip install TA_Lib‑0.4.32‑cp314‑cp314‑win_amd64.whl

ATAU skip TA-Lib dan gunakan pandas-ta saja (sudah cukup untuk kebanyakan indikator)

STEP 3: Verifikasi instalasi
---------------------------------------
python -c "import yfinance; import pandas; import lightweight_charts; print('OK!')"

STEP 4: Run aplikasi
---------------------------------------
python tradingview_app_complete.py

""")
print("="*70)
print("\nCATATAN PENTING:")
print("="*70)
print("""
1. Pastikan Python 3.14 sudah terinstall: python --version
2. Gunakan virtual environment untuk menghindari konflik:
   python -m venv venv
   venv\\Scripts\\activate  (Windows)
   source venv/bin/activate  (Linux/Mac)
3. Jika ada error lightweight-charts, install versi legacy:
   pip install lightweight-charts-python
4. Untuk development, install juga:
   pip install jupyter notebook ipython
""")
