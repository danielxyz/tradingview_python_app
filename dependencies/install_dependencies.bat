
# Update install_dependencies.bat dengan fix untuk pip error
install_script_fixed = """@echo off
REM ================================================================
REM INSTALL SCRIPT - Aplikasi TradingView Python 3.14 (FIXED)
REM ================================================================
echo ================================================================
echo INSTALASI DEPENDENCIES APLIKASI TRADINGVIEW PYTHON
echo ================================================================
echo.

REM Check Python version
echo [1/8] Checking Python version...
python --version
if errorlevel 1 (
    echo ERROR: Python tidak ditemukan!
    echo Pastikan Python 3.14 sudah terinstall dan ada di PATH.
    pause
    exit /b 1
)
echo.

REM Upgrade pip menggunakan python -m pip (fix untuk pip not recognized)
echo [2/8] Upgrading pip...
python -m pip install --upgrade pip
echo.

REM Install dependencies satu per satu menggunakan python -m pip
echo [3/8] Installing pandas...
python -m pip install pandas
echo.

echo [4/8] Installing numpy...
python -m pip install numpy
echo.

echo [5/8] Installing pandas-ta...
python -m pip install pandas-ta
echo.

echo [6/8] Installing lightweight-charts...
python -m pip install lightweight-charts
echo.

echo [7/8] Installing trendln...
python -m pip install trendln
echo.

echo [8/8] Installing additional libraries...
python -m pip install requests websocket-client python-dateutil pytz loguru
echo.

echo ================================================================
echo INSTALASI SELESAI!
echo ================================================================
echo.

REM Verify installation
echo Verifying installation...
python -c "import yfinance; import pandas; import numpy; print('✓ All core libraries installed successfully!')"
if errorlevel 1 (
    echo WARNING: Beberapa library mungkin belum terinstall dengan benar.
    echo Coba jalankan manual: python -m pip install yfinance pandas numpy
) else (
    echo.
    echo ================================================================
    echo APLIKASI SIAP DIJALANKAN!
    echo ================================================================
    echo.
    echo Jalankan aplikasi dengan command:
    echo python tradingview_app_complete.py
)
echo.
pause
"""

with open("install_dependencies_fixed.bat", "w", encoding='utf-8') as f:
    f.write(install_script_fixed)

# Buat juga PowerShell script yang lebih robust
ps_script = """# ================================================================
# INSTALL SCRIPT - Aplikasi TradingView Python 3.14 (PowerShell)
# ================================================================

Write-Host "================================================================" -ForegroundColor Cyan
Write-Host "INSTALASI DEPENDENCIES APLIKASI TRADINGVIEW PYTHON" -ForegroundColor Cyan
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host ""

# Check Python
Write-Host "[1/8] Checking Python version..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version
    Write-Host $pythonVersion -ForegroundColor Green
} catch {
    Write-Host "ERROR: Python tidak ditemukan!" -ForegroundColor Red
    Write-Host "Pastikan Python 3.14 sudah terinstall dan ada di PATH." -ForegroundColor Red
    pause
    exit 1
}
Write-Host ""

# Upgrade pip
Write-Host "[2/8] Upgrading pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip
Write-Host ""

# Install dependencies
$packages = @(
    "pandas",
    "numpy", 
    "pandas-ta",
    "lightweight-charts",
    "trendln",
    "requests",
    "websocket-client",
    "python-dateutil",
    "pytz",
    "loguru"
)

$step = 3
foreach ($package in $packages) {
    Write-Host "[$step/8] Installing $package..." -ForegroundColor Yellow
    python -m pip install $package
    Write-Host ""
    $step++
}

Write-Host "================================================================" -ForegroundColor Cyan
Write-Host "INSTALASI SELESAI!" -ForegroundColor Cyan
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host ""

# Verify
Write-Host "Verifying installation..." -ForegroundColor Yellow
try {
    python -c "import yfinance; import pandas; import numpy; print('✓ All core libraries installed successfully!')"
    Write-Host ""
    Write-Host "================================================================" -ForegroundColor Green
    Write-Host "APLIKASI SIAP DIJALANKAN!" -ForegroundColor Green
    Write-Host "================================================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Jalankan aplikasi dengan command:" -ForegroundColor Cyan
    Write-Host "python tradingview_app_complete.py" -ForegroundColor White
} catch {
    Write-Host "WARNING: Beberapa library mungkin belum terinstall dengan benar." -ForegroundColor Red
}
Write-Host ""
pause
"""

with open("install_dependencies.ps1", "w", encoding='utf-8') as f:
    f.write(ps_script)

print("Script instalasi yang sudah diperbaiki berhasil dibuat!")
print("\n" + "="*70)
print("FILES YANG DIBUAT:")
print("="*70)
print("""
1. install_dependencies_fixed.bat (Batch script - updated)
2. install_dependencies.ps1 (PowerShell script - new)
3. FIX_PIP_ERROR.md (Panduan solusi pip error)

CARA MENGGUNAKAN:
==================

OPSI 1: Manual via PowerShell (RECOMMENDED)
--------------------------------------------
Copy-paste command berikut di PowerShell Anda:

python -m pip install --upgrade pip
python -m pip install pandas numpy pandas-ta lightweight-charts trendln

OPSI 2: Jalankan Batch Script
------------------------------
Double-click: install_dependencies_fixed.bat

OPSI 3: Jalankan PowerShell Script
-----------------------------------
Di PowerShell, jalankan:
.\\install_dependencies.ps1

Jika ada error ExecutionPolicy:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

==================

SETELAH INSTALL SELESAI:
========================
python tradingview_app_complete.py

""")
