
# Buat panduan lengkap untuk error pip not recognized
pip_fix_guide = """# ================================================================
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
C:\\Users\\Daniel\\AppData\\Local\\Python\\pythoncore-3.14-64\\Scripts

**CARA 1: Tambahkan ke PATH secara manual**
1. Tekan Win + R, ketik: sysdm.cpl, Enter
2. Tab Advanced → Environment Variables
3. User variables → Pilih Path → Edit
4. New → Paste: C:\\Users\\Daniel\\AppData\\Local\\Python\\pythoncore-3.14-64\\Scripts
5. OK semua dialog
6. RESTART PowerShell (penting!)

**CARA 2: Tambahkan via PowerShell (Run as Administrator)**
```powershell
$env:Path += ";C:\\Users\\Daniel\\AppData\\Local\\Python\\pythoncore-3.14-64\\Scripts"
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
- Pastikan menjalankan PowerShell di directory aplikasi (D:\\Tradingview Python app)

"""

with open("FIX_PIP_ERROR.md", "w", encoding='utf-8') as f:
    f.write(pip_fix_guide)

print("File FIX_PIP_ERROR.md berhasil dibuat!")
print("\n" + "="*70)
print("SOLUSI UNTUK ERROR: pip is not recognized")
print("="*70)
print("""
ERROR ANDA:
-----------
pip : The term 'pip' is not recognized...

SOLUSI TERCEPAT (Copy-Paste di PowerShell):
============================================

python -m pip install --upgrade pip
python -m pip install pandas numpy pandas-ta lightweight-charts trendln

============================================

PENJELASAN:
-----------
Gunakan 'python -m pip' sebagai pengganti 'pip'
Ini memanggil pip module langsung dari Python, sehingga tidak perlu 
mencari 'pip' di system PATH.

SETELAH INSTALL SELESAI, JALANKAN:
===================================

python tradingview_app_complete.py

===================================

ALTERNATIVE: Install pip ke PATH (Permanent Fix)
=================================================

1. Buka PowerShell sebagai Administrator
2. Jalankan:

$env:Path += ";C:\\Users\\Daniel\\AppData\\Local\\Python\\pythoncore-3.14-64\\Scripts"
[Environment]::SetEnvironmentVariable("Path", $env:Path, [EnvironmentVariableTarget]::User)

3. Restart PowerShell
4. Sekarang 'pip' akan dikenali

===================================

File bantuan: FIX_PIP_ERROR.md (panduan lengkap solusi pip error)
""")
