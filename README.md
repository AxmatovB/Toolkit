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
- **Admin/Root**: 🔴 asbob tanlansa va huquq yetarli bo‘lmasa, dastur ruxsat so‘raydi; rozilik bersangiz sudo/runas bilan qayta ishga tushadi.

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

### Asboblar qo‘llanmasi (ID — ishlatish)
- 1 Ping: host/IP kiriting → paket soni va intervalni tanlang → natijalar.  
- 2 Port Scan: host/IP, start/end port (default 1–1024) → ochiq portlarni ko‘rsatadi.  
- 3 Traceroute: manzil kiriting → hoplar ketma-ketligi.  
- 4 DNS Lookup: domen kiriting → hostname, alias, IP lar.  
- 5 WHOIS: domen/IP kiriting → birinchi 50 qator WHOIS ma’lumoti.  
- 6 Net Interfaces: IP/adapterni ro‘yxati (ip/ifconfig yoki ipconfig).  
- 7 Bandwidth: `speedtest`/`speedtest-cli` bo‘lsa tezlik testini ishga tushiradi.  
- 8 ARP Scan 🔴: subnet kiriting → arp-scan yoki nmap -sn bilan LAN qurilmalar; root talab.  
- 9 HTTP Check: URL kiriting → status, server, content-type, javob vaqti.  
- 10 System Info: OS, versiya, CPU, Python, hostname, IP, admin holati.  
- 11 Process List: ps/tasklist chiqishini CPU bo‘yicha ko‘rsatadi (birinchi ~45 qator).  
- 12 Disk Usage: df -h yoki WMIC disklar.  
- 13 RAM Usage: free -h yoki WMIC RAM.  
- 14 CPU Monitor: psutil bo‘lsa 8 soniyali bar; aks holda top/WMIC.  
- 15 Kill Process 🔴: nom yoki PID kiriting → tasdiqlash → pkill/taskkill.  
- 16 Startup List: Windows startup (WMIC) yoki Linux init.d/systemd ro‘yxati.  
- 17 Win Optimizer: effektlar/SysMain/indeks/trim/power plan sozlaydi (admin).  
- 18 Clear Cache: Temp va Prefetch fayllarni tozalaydi (admin tavsiya).  
- 19 Win Activate 🔴: KMS orqali Windows/Office aktivatsiyasi (admin).  
- 20 Speed Up: registry tweaks, DNS flush, hibernation off (admin tavsiya).  
- 21 Win Update: PowerShell orqali yangilanishlarni o‘rnatish (admin).  
- 22 Firewall: netsh bilan yoqish/o‘chirish, portni block/allow, rules ro‘yxati.  
- 23 UFW Firewall: status/enable/disable/allow/deny/delete (sudo).  
- 24 Package Manager: apt/yum update/upgrade/install/remove/search/list (sudo).  
- 25 Services: systemctl status/start/stop/restart/enable/disable (sudo).  
- 26 Cron Jobs: crontab ko‘rish/qo‘shish/edit/nuklash.  
- 27 Log Viewer: syslog, auth.log, dmesg, journalctl, kern.log tail.  
- 28 Hash File: tanlangan faylning MD5/SHA1/SHA256 xeshi.  
- 29 Password Generator: uzunlik va sonini tanlab, tasodifiy parollar yaratadi.  
- 30 Vulnerability Scan 🔴: `nmap -sV --script=vuln` (root tavsiya); vaqt oladi.  
- 31 Nmap Quick: `nmap -T4 -F` tez top-port skan.  
- 32 Nmap Full 🔴: `nmap -sC -sV -O -p- -T4` to‘liq skan (admin tavsiya).  
- 33 Nmap Ping: `nmap -sn <subnet>` ping sweep.  
- 34 Nmap Top20: `nmap --top-ports 20 -sV -T4`.  
- 35 Airmon 🔴: airmon-ng start/stop monitor rejimi (root).  
- 36 Airodump 🔴: monitor interfeysda handshake yozish; BSSID/channel/outputni kiriting.  
- 37 Aircrack 🔴: .cap/.pcap faylni wordlist bilan buzish.  
- 38 Aireplay 🔴: deauth jo‘natib handshake olish; BSSID va ixtiyoriy client MAC.

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
cd Toolkit   # odatda: ~/Toolkit yoki %USERPROFILE%\\Toolkit
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
