# SYS-TOOLKIT v3.1
Created by Axmatov · Windows & Linux · 38 CLI tools · typewriter UI

---

## 🇬🇧 English
### What it is
Cross‑platform, menu‑driven toolbox (network, system, Windows, Linux, security) with color + typing animation. Works fully offline after clone; no pip installs at runtime.

### Requirements
- Python **3.11+**  
- External binaries (not bundled): `nmap`, `aircrack-ng` suite, `speedtest-cli` (optional for bandwidth test).

### Install (offline-ready)
1. `git clone https://github.com/YOUR_USERNAME/sys-toolkit.git`
2. `cd sys-toolkit` (default path: `~/sys-toolkit` on Linux/macOS, `%USERPROFILE%\\sys-toolkit` on Windows)
3. `chmod +x toolkit` (Linux)
4. Run: `./toolkit` (Linux/macOS) or `toolkit.bat` (Windows). First run shows a short animated setup; it auto-installs missing tools on Linux (apt/yum) if you confirm.  
   - First-run OS choice is saved; use `toolkit --setup` or `os` command in menu to change later.
5. (Optional, recommended) Add the repo to PATH so you can just type `toolkit` anywhere:
   - Linux/macOS: `echo 'export PATH=\"$HOME/sys-toolkit:$PATH\"' >> ~/.bashrc && source ~/.bashrc`
     or `sudo ln -s \"$HOME/sys-toolkit/toolkit\" /usr/local/bin/toolkit`
   - Windows (PowerShell): `setx PATH \"$env:PATH;${env:USERPROFILE}\\sys-toolkit\"`

### Use
- Startup prompt: `1` Windows, `2` Linux, `A` auto, `0` exit.  
- Type tool number → Enter. `os` switches OS without restart.  
- 🔴 items usually need Admin/Root.

### Tool map
- **Network:** 1 Ping, 2 Port Scan, 3 Traceroute, 4 DNS, 5 WHOIS, 6 Interfaces, 7 Bandwidth (needs speedtest-cli), 8 ARP Scan 🔴, 9 HTTP Check, 31 Nmap Quick, 32 Nmap Full 🔴, 33 Nmap Ping, 34 Nmap Top20.  
- **System:** 10 System Info, 11 Process List, 12 Disk, 13 RAM, 14 CPU Monitor, 15 Kill 🔴, 16 Startup.  
- **Windows:** 17 Optimizer, 18 Clear Cache, 19 Activate 🔴, 20 Speed Up, 21 Update, 22 Firewall.  
- **Linux:** 23 UFW, 24 Package Manager, 25 Services, 26 Cron, 27 Logs.  
- **Security:** 28 Hash File, 29 Passwords, 30 Vulnerability scan (nmap) 🔴, 35 Airmon 🔴, 36 Airodump 🔴, 37 Aircrack 🔴, 38 Aireplay 🔴.

### Notes
- `nmap` / `aircrack-ng` are invoked if present; otherwise you’ll get a clear hint to install (apt/yum/choco).  
- No Python packages shipped/needed; everything is standard library.  
- Some commands may be intrusive (port scans, deauth); use only where permitted.

### Offline vendor option
Place portable binaries inside the repo to skip system installs:
```
vendor/
  windows/
    nmap/          nmap.exe + dlls
    aircrack-ng/   aircrack-ng.exe, airmon-ng.exe, airodump-ng.exe, aireplay-ng.exe, etc.
  linux/
    nmap/bin/          nmap
    aircrack-ng/bin/   aircrack-ng, airmon-ng, airodump-ng, aireplay-ng, etc.
```
On launch, toolkit prepends these folders to PATH automatically.

---

## 🇷🇺 Русский
### Что это
Кроссплатформенный набор CLI-инструментов с меню и анимацией. Работает офлайн после клона; pip не требуется.

### Требования
- Python **3.11+**  
- Внешние бинарники (не входят в репо): `nmap`, комплект `aircrack-ng`, `speedtest-cli` (по желанию для теста скорости).

### Установка
1. `git clone https://github.com/YOUR_USERNAME/sys-toolkit.git`  
2. `cd sys-toolkit`  (обычно `~/sys-toolkit` или `%USERPROFILE%\\sys-toolkit`)  
3. `chmod +x toolkit` (Linux)  
4. Запуск: `./toolkit` (Linux/macOS) или `toolkit.bat` (Windows). При первом запуске есть короткий анимированный setup; на Linux при согласии попытается установить недостающие пакеты (apt/yum).  
   - Выбор ОС сохраняется; поменять можно командой `os` в меню или `toolkit --setup`.
5. (Опционально) Добавьте каталог в PATH, чтобы вызывать `toolkit` откуда угодно:  
   - Linux/macOS: `echo 'export PATH=\"$HOME/sys-toolkit:$PATH\"' >> ~/.bashrc && source ~/.bashrc`  
     или `sudo ln -s \"$HOME/sys-toolkit/toolkit\" /usr/local/bin/toolkit`  
   - Windows (PowerShell): `setx PATH \"$env:PATH;${env:USERPROFILE}\\sys-toolkit\"`

### Использование
- На старте: `1` Windows, `2` Linux, `A` авто, `0` выход.  
- Введите номер инструмента → Enter. `os` — сменить ОС без перезапуска.  
- 🔴 обычно требуют права администратора/рута.

### Карта инструментов
- **Сеть:** 1 Ping, 2 Port Scan, 3 Traceroute, 4 DNS, 5 WHOIS, 6 Интерфейсы, 7 Скорость (speedtest-cli), 8 ARP 🔴, 9 HTTP, 31 Nmap Quick, 32 Nmap Full 🔴, 33 Nmap Ping, 34 Nmap Top20.  
- **Система:** 10 Инфо, 11 Процессы, 12 Диск, 13 ОЗУ, 14 CPU, 15 Kill 🔴, 16 Автозапуск.  
- **Windows:** 17 Оптимизация, 18 Очистка кэша, 19 Активация 🔴, 20 Ускорение, 21 Обновления, 22 Брандмауэр.  
- **Linux:** 23 UFW, 24 Пакеты, 25 Службы, 26 Cron, 27 Логи.  
- **Безопасность:** 28 Хэш, 29 Пароли, 30 Скан уязвимостей 🔴, 35 Airmon 🔴, 36 Airodump 🔴, 37 Aircrack 🔴, 38 Aireplay 🔴.

### Заметки
- `nmap` / `aircrack-ng` должны быть установлены в системе; при отсутствии выводится подсказка.  
- Python-зависимостей нет.  
- Будьте внимательны: сканирование и deauth легальны не везде.

### Офлайн-вариант (vendor)
Поместите портативные бинарники в репозиторий, чтобы не ставить системно:
```
vendor/
  windows/
    nmap/          nmap.exe + dll
    aircrack-ng/   aircrack-ng.exe, airmon-ng.exe, airodump-ng.exe, aireplay-ng.exe, ...
  linux/
    nmap/bin/          nmap
    aircrack-ng/bin/   aircrack-ng, airmon-ng, airodump-ng, aireplay-ng, ...
```
При запуске toolkit сам добавит эти пути в PATH.

---

## 🇺🇿 O‘zbekcha
### Bu nima
Menyu orqali boshqariladigan, rangli va yozuv animatsiyali kross‑platform CLI to‘plam. Klondan so‘ng oflayn ishlaydi; pip shart emas.

### Talablar
- Python **3.11+**  
- Tashqi binarlar (repo ichida yo‘q): `nmap`, `aircrack-ng` to‘plami, `speedtest-cli` (ixtiyoriy).

### O‘rnatish
1. `git clone https://github.com/YOUR_USERNAME/sys-toolkit.git`
2. `cd sys-toolkit`  (odatda `~/sys-toolkit` yoki `%USERPROFILE%\\sys-toolkit`)
3. `chmod +x toolkit` (Linux)
4. Ishga tushirish: `./toolkit` (Linux/macOS) yoki `toolkit.bat` (Windows). Birinchi safar qisqa animatsiyali setup chiqadi; Linuxda rozilik bersangiz kerakli paketlarni (apt/yum) o‘rnatishga urinadi.
   - OS tanlovi saqlanadi; keyinroq `os` (menyuda) yoki `toolkit --setup` bilan o‘zgartirishingiz mumkin.
5. (Ixtiyoriy) PATH ga qo‘shish, shunda hamma joyda `toolkit` deb chaqiriladi:  
   - Linux/macOS: `echo 'export PATH=\"$HOME/sys-toolkit:$PATH\"' >> ~/.bashrc && source ~/.bashrc`  
     yoki `sudo ln -s \"$HOME/sys-toolkit/toolkit\" /usr/local/bin/toolkit`  
   - Windows (PowerShell): `setx PATH \"$env:PATH;${env:USERPROFILE}\\sys-toolkit\"`

### Foydalanish
- Boshlanishida: `1` Windows, `2` Linux, `A` auto, `0` chiqish.  
- Raqam kiriting → Enter. `os` — OS ni almashtirish.  
- 🔴 vositalar ko‘pincha admin/root talab qiladi.

### Asboblar xaritasi
- **Tarmoq:** 1 Ping, 2 Port skaneri, 3 Traceroute, 4 DNS, 5 WHOIS, 6 Interfeyslar, 7 Tezlik (speedtest-cli), 8 ARP 🔴, 9 HTTP, 31 Nmap Quick, 32 Nmap Full 🔴, 33 Nmap Ping, 34 Nmap Top20.  
- **Tizim:** 10 Tizim ma’lumoti, 11 Jarayonlar, 12 Disk, 13 RAM, 14 CPU monitor, 15 Jarayonni o‘ldirish 🔴, 16 Avto-ishga tushish.  
- **Windows:** 17 Optimallashtirish, 18 Kesh tozalash, 19 Aktivatsiya 🔴, 20 Tezlashtirish, 21 Yangilash, 22 Xavfsizlik devori.  
- **Linux:** 23 UFW, 24 Paket menejeri, 25 Servislar, 26 Cron, 27 Loglar.  
- **Xavfsizlik:** 28 Fayl xeshi, 29 Parol generatori, 30 Zaiflik skaneri 🔴, 35 Airmon 🔴, 36 Airodump 🔴, 37 Aircrack 🔴, 38 Aireplay 🔴.

### Esda tuting
- `nmap` va `aircrack-ng` tizimda o‘rnatilgan bo‘lishi kerak; yo‘q bo‘lsa dastur ko‘rsatma beradi.  
- Python kutubxonalari kerak emas.  
- Port skan/deauth faqat ruxsat etilgan tarmoqlarda ishlating.

### Oflayn (vendor) varianti
Portable binarlarni loyiha ichiga qo‘ying — o‘rnatish shart emas:
```
vendor/
  windows/
    nmap/          nmap.exe + dll
    aircrack-ng/   aircrack-ng.exe, airmon-ng.exe, airodump-ng.exe, aireplay-ng.exe, ...
  linux/
    nmap/bin/          nmap
    aircrack-ng/bin/   aircrack-ng, airmon-ng, airodump-ng, aireplay-ng, ...
```
Ishga tushganda toolkit bu papkalarni PATH ga qo‘shadi.
