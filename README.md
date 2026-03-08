# ⚡ SYS-TOOLKIT v3.0

```
                    ::::::::::::::::::
              ::::::::::::::::::::::::::::::
          ::::::::::::::::::::::::::::::::::::::
       ::::::::::::::::::::     :::::::::::::::::::
     :::::::::::::                      :::::::::::::
  ::::::::::::                              ::::::::::::
 ::::::::::       ::::::::::::::::::::::       ::::::::::
 ::::::::      :::::::::::::::::::::::::::::      :::::::
   ::::     ::::::::::::::::::::::::::::::::::     ::::
          ::::::::::::::           :::::::::::::
        :::::::::::                    :::::::::::
        ::::::::       ::::::::::::       ::::::::
          ::::     ::::::::::::::::::::     ::::
                 ::::::::::::::::::::::::
               ::::::::::::::::::::::::::::
               :::::::::          :::::::::
                 ::::     ::::::     :::::
                        ::::::::::
                       :::::::::::::
                      ::::::::::::::
                      ::::::::::::::
                       ::::::::::::
                         ::::::::
```

**Created by Axmatov** | Cross-platform · Windows & Linux · 30 Tools

---

## 🌐 Language / Язык / Til

<details>
<summary>🇬🇧 English</summary>

## Documentation

### What is SYS-TOOLKIT?

A cross-platform, all-in-one command-line utility with **30 tools** in 5 categories.  
On launch it detects your OS and shows only tools available for your system.  
All output is printed with a **typewriter animation** effect.

---

### ⚙️ Requirements

| Component | Minimum | ✅ Recommended |
|-----------|---------|----------------|
| **Python** | 3.9 | **3.11 or higher ← required** |
| OS | Windows 7 / Linux kernel 4+ | Windows 10/11 / Ubuntu 20.04+ |
| RAM | 64 MB | 128 MB |
| Disk | 5 MB | 20 MB |
| Rights | User | 🔴 Admin/Root (some tools) |

> ⚠️ Python **3.11+** is required for full compatibility.

**Optional Python packages** (auto-installed by tool 7):
```
psutil          — live CPU / RAM monitor
speedtest-cli   — bandwidth speed test
```

**Optional system binaries:**

| Binary | Linux | Windows |
|--------|-------|---------|
| `nmap` | `sudo apt install nmap` | `choco install nmap` |
| `whois` | `sudo apt install whois` | `choco install whois` |
| `arp-scan` | `sudo apt install arp-scan` | — |
| `traceroute` | `sudo apt install traceroute` | built-in `tracert` |

---

### 📦 Install & Run

```bash
git clone https://github.com/YOUR_USERNAME/sys-toolkit.git
cd sys-toolkit
pip install -r requirements.txt

python toolkit.py          # Windows
python3 toolkit.py         # Linux
sudo python3 toolkit.py    # Linux (full features)
```

---

### 🚀 Usage

1. Run → **OS selection screen** appears
2. Press `A` (auto) or `1` Windows / `2` Linux
3. **3-column menu** shows tools for your OS
4. Type a number → Enter → follow prompts → Enter to return
5. Type `os` anytime to switch OS without restarting
6. Type `0` to exit

---

### 🛠️ Tools

**🌐 NETWORK** — both OS

| ID | Tool | Description | Diff |
|----|------|-------------|------|
| 1 | Ping | Custom count & interval | 🟢 |
| 2 | Port Scan | Multi-threaded TCP | 🟡 |
| 3 | Traceroute | Hop-by-hop path | 🟡 |
| 4 | DNS Lookup | Domain → IP | 🟢 |
| 5 | WHOIS | Registration info | 🟢 |
| 6 | Net Interfaces | All adapters & IPs | 🟢 |
| 7 | Bandwidth | DL / UL speed test | 🟡 |
| 8 | ARP Scan | Discover LAN devices | 🔴 |
| 9 | HTTP Check | Status, server, time | 🟢 |

**💻 SYSTEM** — both OS

| ID | Tool | Description | Diff |
|----|------|-------------|------|
| 10 | System Info | OS / CPU / IP | 🟢 |
| 11 | Process List | Sorted by CPU | 🟢 |
| 12 | Disk Usage | Partitions & free space | 🟢 |
| 13 | RAM Usage | Total / used / free | 🟢 |
| 14 | CPU Monitor | Live 8-sample bar | 🟢 |
| 15 | Kill Process | By PID or name | 🔴 |
| 16 | Startup List | Boot programs | 🟡 |

**🪟 WINDOWS** — Windows only

| ID | Tool | Description | Diff |
|----|------|-------------|------|
| 17 | Win Optimizer | Effects, SysMain, index off | 🟡 |
| 18 | Clear Cache | Temp files, free space | 🟡 |
| 19 | Win Activate | KMS: Win 10/11 + Office | 🔴 |
| 20 | Speed Up | Registry tweaks | 🟡 |
| 21 | Win Update | PowerShell updates | 🟡 |
| 22 | Firewall | Rules & port management | 🟡 |

**🐧 LINUX** — Linux only

| ID | Tool | Description | Diff |
|----|------|-------------|------|
| 23 | UFW Firewall | Allow / deny / status | 🟡 |
| 24 | Pkg Manager | APT/YUM install, remove | 🟢 |
| 25 | Services | Systemd control | 🟡 |
| 26 | Cron Jobs | View, add, edit | 🟡 |
| 27 | Log Viewer | syslog, auth, dmesg | 🟢 |

**🔒 SECURITY** — both OS

| ID | Tool | Description | Diff |
|----|------|-------------|------|
| 28 | Hash File | MD5 / SHA1 / SHA256 | 🟢 |
| 29 | Pass Gen | Cryptographic passwords | 🟢 |
| 30 | Vuln Scan | nmap CVE scan | 🔴 |

🟢 Easy · 🟡 Medium · 🔴 Hard (Admin/Root)

</details>

---

<details>
<summary>🇷🇺 Русский</summary>

## Документация

### Что такое SYS-TOOLKIT?

Кросс-платформенная утилита «всё в одном» с **30 инструментами** в 5 категориях.  
При запуске автоматически определяет ОС и показывает только доступные инструменты.  
Весь вывод печатается с **эффектом печатной машинки**.

---

### ⚙️ Системные требования

| Компонент | Минимум | ✅ Рекомендуется |
|-----------|---------|-----------------|
| **Python** | 3.9 | **3.11 и выше ← обязательно** |
| ОС | Windows 7 / Linux ядро 4+ | Windows 10/11 / Ubuntu 20.04+ |
| ОЗУ | 64 МБ | 128 МБ |
| Диск | 5 МБ | 20 МБ |
| Права | Пользователь | 🔴 Admin/Root (часть инструментов) |

> ⚠️ Python **3.11+** обязателен для полной совместимости.

**Опциональные пакеты:**
```
psutil          — мониторинг CPU / RAM
speedtest-cli   — тест скорости интернета
```

**Опциональные системные утилиты:**

| Утилита | Linux | Windows |
|---------|-------|---------|
| `nmap` | `sudo apt install nmap` | `choco install nmap` |
| `whois` | `sudo apt install whois` | `choco install whois` |
| `arp-scan` | `sudo apt install arp-scan` | — |
| `traceroute` | `sudo apt install traceroute` | встроен `tracert` |

---

### 📦 Установка и запуск

```bash
git clone https://github.com/YOUR_USERNAME/sys-toolkit.git
cd sys-toolkit
pip install -r requirements.txt

python toolkit.py          # Windows
python3 toolkit.py         # Linux
sudo python3 toolkit.py    # Linux полный
```

---

### 🚀 Использование

1. Запустить → **экран выбора ОС**
2. `A` (авто) или `1` Windows / `2` Linux
3. **Меню в 3 колонки** для вашей ОС
4. Номер → Enter → подсказки → Enter для возврата
5. `os` — сменить ОС без перезапуска
6. `0` — выход

---

### 🛠️ Инструменты

**🌐 СЕТЬ** — обе ОС

| ID | Инструмент | Описание | Сложность |
|----|-----------|----------|----------|
| 1 | Ping | Пакеты с интервалом | 🟢 |
| 2 | Сканер портов | Многопоточный TCP | 🟡 |
| 3 | Traceroute | Путь по хопам | 🟡 |
| 4 | DNS Lookup | Домен → IP | 🟢 |
| 5 | WHOIS | Данные регистрации | 🟢 |
| 6 | Интерфейсы | Адаптеры и IP | 🟢 |
| 7 | Скорость | Тест загрузки/отдачи | 🟡 |
| 8 | ARP Скан | Устройства в LAN | 🔴 |
| 9 | HTTP Проверка | Статус, сервер, время | 🟢 |

**💻 СИСТЕМА** — обе ОС

| ID | Инструмент | Описание | Сложность |
|----|-----------|----------|----------|
| 10 | Инфо о системе | ОС / CPU / IP | 🟢 |
| 11 | Процессы | По CPU | 🟢 |
| 12 | Диск | Разделы и место | 🟢 |
| 13 | ОЗУ | Общее / занято / свободно | 🟢 |
| 14 | CPU Монитор | Живой бар 8 сэмплов | 🟢 |
| 15 | Завершить процесс | По PID или имени | 🔴 |
| 16 | Автозагрузка | Программы при старте | 🟡 |

**🪟 WINDOWS** — только Windows

| ID | Инструмент | Описание | Сложность |
|----|-----------|----------|----------|
| 17 | Оптимизатор | Эффекты, SysMain, индекс | 🟡 |
| 18 | Очистка кэша | Temp-файлы | 🟡 |
| 19 | Активация | KMS Win 10/11 + Office | 🔴 |
| 20 | Ускорение | Твики реестра | 🟡 |
| 21 | Обновления | PowerShell | 🟡 |
| 22 | Брандмауэр | Правила и порты | 🟡 |

**🐧 LINUX** — только Linux

| ID | Инструмент | Описание | Сложность |
|----|-----------|----------|----------|
| 23 | UFW | Allow / deny / статус | 🟡 |
| 24 | Пакеты | APT/YUM | 🟢 |
| 25 | Службы | Systemd | 🟡 |
| 26 | Cron | Просмотр и добавление | 🟡 |
| 27 | Логи | syslog, auth, dmesg | 🟢 |

**🔒 БЕЗОПАСНОСТЬ** — обе ОС

| ID | Инструмент | Описание | Сложность |
|----|-----------|----------|----------|
| 28 | Хэш файла | MD5 / SHA1 / SHA256 | 🟢 |
| 29 | Генератор паролей | Криптостойкие | 🟢 |
| 30 | Сканер уязвимостей | nmap CVE | 🔴 |

🟢 Лёгко · 🟡 Средне · 🔴 Сложно (Admin/Root)

</details>

---

<details>
<summary>🇺🇿 O'zbekcha</summary>

## Hujjat

### SYS-TOOLKIT nima?

5 kategoriyada **30 ta vosita** bilan ishlaydigon cross-platform buyruq qatori dasturi.  
Ishga tushganda OS ni avtomatik aniqlab, faqat mavjud vositalarni ko'rsatadi.  
Barcha chiqish **yozuv mashinasi animatsiyasi** bilan chiqadi.

---

### ⚙️ Talablar

| Komponent | Minimal | ✅ Tavsiya |
|-----------|---------|-----------|
| **Python** | 3.9 | **3.11 va undan yuqori ← zaruriy** |
| OT | Windows 7 / Linux kernel 4+ | Windows 10/11 / Ubuntu 20.04+ |
| RAM | 64 MB | 128 MB |
| Disk | 5 MB | 20 MB |
| Huquqlar | Foydalanuvchi | 🔴 Admin/Root (ba'zi vositalar) |

> ⚠️ To'liq ishlashi uchun Python **3.11+** talab qilinadi.

**Ixtiyoriy Python paketlari:**
```
psutil          — jonli CPU / RAM monitoring
speedtest-cli   — internet tezlik testi
```

**Ixtiyoriy tizim vositalari:**

| Vosita | Linux | Windows |
|--------|-------|---------|
| `nmap` | `sudo apt install nmap` | `choco install nmap` |
| `whois` | `sudo apt install whois` | `choco install whois` |
| `arp-scan` | `sudo apt install arp-scan` | — |
| `traceroute` | `sudo apt install traceroute` | o'rnatilgan `tracert` |

---

### 📦 O'rnatish va ishga tushirish

```bash
git clone https://github.com/YOUR_USERNAME/sys-toolkit.git
cd sys-toolkit
pip install -r requirements.txt

python toolkit.py          # Windows
python3 toolkit.py         # Linux
sudo python3 toolkit.py    # Linux to'liq
```

---

### 🚀 Qanday ishlatish

1. Ishga tushirish → **OS tanlash ekrani**
2. `A` (avto) yoki `1` Windows / `2` Linux
3. **3 ustunli menyu** OS uchun vositalar
4. Raqam → Enter → ko'rsatmalar → Enter menyuga qaytadi
5. `os` — qayta ishga tushirmasdan OS almashtirish
6. `0` — chiqish

---

### 🛠️ Vositalar

**🌐 TARMOQ** — ikkala OS

| ID | Vosita | Tavsif | Qiyinlik |
|----|--------|--------|---------|
| 1 | Ping | Interval bilan ping | 🟢 |
| 2 | Port skaneri | Ko'p tarmoqli TCP | 🟡 |
| 3 | Traceroute | Tarmoq yo'li | 🟡 |
| 4 | DNS Lookup | Domen → IP | 🟢 |
| 5 | WHOIS | Ro'yxatga olish | 🟢 |
| 6 | Interfeyslari | Adapterlar va IP | 🟢 |
| 7 | Tezlik testi | DL / UL | 🟡 |
| 8 | ARP Skan | LAN qurilmalar | 🔴 |
| 9 | HTTP tekshirish | Holat, server, vaqt | 🟢 |

**💻 TIZIM** — ikkala OS

| ID | Vosita | Tavsif | Qiyinlik |
|----|--------|--------|---------|
| 10 | Tizim ma'lumoti | OS / CPU / IP | 🟢 |
| 11 | Jarayonlar | CPU bo'yicha | 🟢 |
| 12 | Disk | Bo'limlar va joy | 🟢 |
| 13 | RAM | Jami / band / bo'sh | 🟢 |
| 14 | CPU monitor | Jonli bar | 🟢 |
| 15 | Jarayonni o'ldirish | PID yoki nom | 🔴 |
| 16 | Ishga tushirish | Boot dasturlar | 🟡 |

**🪟 WINDOWS** — faqat Windows

| ID | Vosita | Tavsif | Qiyinlik |
|----|--------|--------|---------|
| 17 | Optimallashtiruvchi | Effektlar, SysMain | 🟡 |
| 18 | Keshni tozalash | Temp fayllar | 🟡 |
| 19 | Faollashtirish | KMS Win 10/11 + Office | 🔴 |
| 20 | Tezlashtirish | Registry tweaklar | 🟡 |
| 21 | Win yangilash | PowerShell | 🟡 |
| 22 | Xavfsizlik devori | Qoidalar va portlar | 🟡 |

**🐧 LINUX** — faqat Linux

| ID | Vosita | Tavsif | Qiyinlik |
|----|--------|--------|---------|
| 23 | UFW devori | Allow / deny | 🟡 |
| 24 | Paket menejeri | APT/YUM | 🟢 |
| 25 | Servislar | Systemd | 🟡 |
| 26 | Cron | Ko'rish, qo'shish | 🟡 |
| 27 | Loglar | syslog, auth, dmesg | 🟢 |

**🔒 XAVFSIZLIK** — ikkala OS

| ID | Vosita | Tavsif | Qiyinlik |
|----|--------|--------|---------|
| 28 | Fayl xeshi | MD5 / SHA1 / SHA256 | 🟢 |
| 29 | Parol generatori | Kriptografik | 🟢 |
| 30 | Zaiflik skaneri | nmap CVE | 🔴 |

🟢 Oson · 🟡 O'rta · 🔴 Qiyin (Admin/Root)

</details>

---

## 📁 Structure

```
sys-toolkit/
├── toolkit.py       ← main script (only file you need to run)
├── requirements.txt ← optional pip packages
└── README.md        ← docs (EN / RU / UZ)
```

## ⚡ Quick start

```bash
git clone https://github.com/YOUR_USERNAME/sys-toolkit.git
cd sys-toolkit
pip install -r requirements.txt
python3 toolkit.py
```

---
*⚡ Created by Axmatov*
