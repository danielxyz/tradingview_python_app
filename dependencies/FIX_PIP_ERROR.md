# ================================================================
# SOLUSI: pip is not recognized
# ================================================================

## PENYEBAB:
PowerShell tidak mengenali command 'pip' karena:
1. pip belum terinstall, ATAU
2. pip tidak ada di system PATH

## SOLUSI LENGKAP:

---

### SOLUSI 1: Gunakan 'python -m pip' (PALING AMAN)

Gunakan prefix 'python -m' sebelum pip:

```powershell
python -m pip install pandas numpy pandas-ta lightweight-charts trendln
```

Ini bekerja karena memanggil pip module langsung dari Python.

---

### SOLUSI 2: Install pip jika belum ada

```powershell
python -m ensurepip --upgrade
python -m pip install --upgrade pip
```

Kemudian install dependencies:

```powershell
python -m pip install pandas numpy pandas-ta lightweight-charts trendln
```

---

### SOLUSI 3: Tambahkan pip ke PATH (Permanent Fix)

Berdasarkan warning sebelumnya, pip terinstall di:
C:\Users\Daniel\AppData\Local\Python\pythoncore-3.14-64\Scripts

**CARA 1: Tambahkan ke PATH secara manual**
1. Tekan Win + R, ketik: sysdm.cpl, Enter
2. Tab Advanced → Environment Variables
3. User variables → Pilih Path → Edit
4. New → Paste: C:\Users\Daniel\AppData\Local\Python\pythoncore-3.14-64\Scripts
5. OK semua dialog
6. RESTART PowerShell (penting!)

**CARA 2: Tambahkan via PowerShell (Run as Administrator)**
```powershell
$env:Path += ";C:\Users\Daniel\AppData\Local\Python\pythoncore-3.14-64\Scripts"
[Environment]::SetEnvironmentVariable("Path", $env:Path, [EnvironmentVariableTarget]::User)
```

---

### SOLUSI 4: Install menggunakan Python langsung (QUICK FIX)

Satu command untuk install semua:

```powershell
python -m pip install --upgrade pip
python -m pip install pandas numpy pandas-ta lightweight-charts trendln requests websocket-client python-dateutil pytz loguru
```

---

## VERIFICATION:

Setelah install, verifikasi:

```powershell
python -m pip --version
python -c "import pandas; import numpy; import yfinance; print('SUCCESS!')"
```

---

## JALANKAN APLIKASI:

```powershell
python tradingview_app_complete.py
```

---

## CATATAN PENTING:

- SELALU gunakan 'python -m pip' jika 'pip' tidak dikenali
- Restart PowerShell setelah menambahkan PATH
- Gunakan 'py' jika 'python' juga tidak dikenali
- Pastikan menjalankan PowerShell di directory aplikasi (D:\Tradingview Python app)

