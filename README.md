# SYS-TOOLKIT v3.1
🇺🇿 O‘zbekcha hujjat

[📄 Hujjat](#hujjat) · [🛠️ Asboblar](#asboblar) · [⬇️ O‘rnatish](#ornatish)

---

## Hujjat
- **Nima?** Windows va Linux uchun 38 ta buyruq-qator asboblar to‘plami (tarmoq, tizim, xavfsizlik, Windows, Linux). Rangli menyu, yozuv animatsiyasi, birinchi ishga tushishda OS tanlovi saqlanadi.
- **Nega kerak?** Tarmoq diagnostikasi (ping, port skan, traceroute, nmap), tizim holati (CPU/RAM/disk), xavfsizlik (hash, parol generatori, aircrack-ng, nmap vuln), tez sozlash (Windows optimallashtirish, Linux UFW/service/cron).
- **Offline?** Python standart kutubxonasi bilan ishlaydi. Agar `vendor/` ichiga portable `nmap` / `aircrack-ng` qo‘ysangiz, to‘liq oflayn. Linuxda internet bo‘lsa, birinchi setup payti apt/yum orqali kerakli paketlarni o‘rnatishga urinadi.
- **OS tanlash**: faqat birinchi setupda so‘raladi, `.os_choice` ga yoziladi. Keyin avtomatik shu OS bilan ochiladi; `os` komandasida yoki `toolkit --setup` bilan o‘zgartiriladi.
- **Ishga tushirish**: `./toolkit` (Linux/macOS) yoki `toolkit.bat` (Windows). PATH ga qo‘shsangiz, shunchaki `toolkit`.

---

## Asboblar

**Tarmoq (NET)**  
1 Ping · 2 Port Scan · 3 Traceroute · 4 DNS Lookup · 5 WHOIS · 6 Net Interfaces · 7 Bandwidth (speedtest-cli) · 8 ARP Scan 🔴 · 9 HTTP Check · 31 Nmap Quick · 32 Nmap Full 🔴 · 33 Nmap Ping · 34 Nmap Top20

**Tizim (SYS)**  
10 System Info · 11 Process List · 12 Disk Usage · 13 RAM Usage · 14 CPU Monitor · 15 Kill Process 🔴 · 16 Startup List

**Windows (WIN)**  
17 Win Optimizer · 18 Clear Cache · 19 Win Activate 🔴 · 20 Speed Up · 21 Win Update · 22 Firewall

**Linux (LNX)**  
23 UFW Firewall · 24 Package Manager · 25 Services · 26 Cron · 27 Log Viewer

**Xavfsizlik (SEC)**  
28 Hash File · 29 Password Generator · 30 Vulnerability Scan 🔴 · 35 Airmon 🔴 · 36 Airodump 🔴 · 37 Aircrack 🔴 · 38 Aireplay 🔴

🔴 — odatda Admin/Root talab qiladi.

---

## O‘rnatish

### 1) Tayyorlash
- **Talab**: Python 3.11+.  
- **Majburiy pip paketlar**: yo‘q.  
- **Tashqi binarlar**: `nmap`, `aircrack-ng`, `speedtest-cli` (bandwidth uchun). Windows versiyalari `vendor/windows/` ichida allaqachon bor; Linux uchun ikki yo‘l:  
  - Portable binarlarni `vendor/linux/nmap/bin/` va `vendor/linux/aircrack-ng/bin/` ga qo‘ying; yoki  
  - Internet bo‘lsa, setup ularni apt/yum orqali o‘zi o‘rnatishga harakat qiladi.

### 2) Klonlash
```bash
git clone https://github.com/AxmatovB/Toolkit.git
cd Toolkit   # odatda: ~/Toolkit yoki %USERPROFILE%\Toolkit
chmod +x toolkit   # Linux/macOS
```

### 3) Birinchi ishga tushirish (setup animatsiyasi bilan)
```bash
./toolkit        # Linux/macOS
toolkit.bat      # Windows
```
- OS tanlovi saqlanadi.  
- Linuxda kerakli paketlar topilmasa, apt/yum orqali avtomatik o‘rnatishga urinadi (sudo ruxsat so‘ralishi mumkin).  
- Vendor papkalari PATH ga qo‘shiladi. `.setup_done` yaratiladi.

### 4) Keyingi ishga tushirish
Shunchaki `toolkit` (yoki `toolkit.bat`). OS so‘ralmaydi. OSni almashtirish uchun menyuda `os` yozing yoki `toolkit --setup`.

### 5) PATH ga qo‘shish (ixtiyoriy, lekin qulay)
- Linux/macOS:  
  ```bash
  echo 'export PATH="$HOME/Toolkit:$PATH"' >> ~/.bashrc
  source ~/.bashrc
  # yoki: sudo ln -s "$HOME/Toolkit/toolkit" /usr/local/bin/toolkit
  ```
- Windows (PowerShell):  
  ```powershell
  setx PATH "$env:PATH;${env:USERPROFILE}\\Toolkit"
  ```

### 6) Vendor tuzilmasi (agar portable qo‘ysangiz)
```
vendor/
  windows/
    nmap/          nmap.exe, nping.exe, ncat.exe, ndiff.exe + dll
    aircrack-ng/   aircrack-ng.exe, airodump-ng.exe, aireplay-ng.exe, airmon-ng.exe + dll
  linux/
    nmap/bin/          nmap (nping, ncat ixtiyoriy)
    aircrack-ng/bin/   aircrack-ng, airodump-ng, aireplay-ng, airmon-ng
```
`.keep` fayllar — shunchaki placeholder, haqiqiy binarlar bilan almashtiring.

### 7) Muammolar
- `nmap` yoki `aircrack-ng` topilmasa: Linuxda `sudo apt install nmap aircrack-ng` yoki `sudo yum install ...`; Windowsda binoarlarni `vendor/windows/...` ga qo‘ying.  
- Bandwidth testi uchun `speedtest-cli` yo‘q bo‘lsa, uni o‘rnating yoki bu asbobni o‘tkazib yuboring.  
- Setupni qayta ishlatish: `toolkit --setup`.

---

*Muallif: Axmatov · SYS-TOOLKIT v3.1*
