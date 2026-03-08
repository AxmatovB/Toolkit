#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SYS-TOOLKIT v3.0
Created by Axmatov
Cross-platform: Windows & Linux
"""

import os, sys, time, platform, subprocess, socket
import threading, hashlib, secrets, string

# ══════════════════════════════════════════════════════════════════
#  COLORS
# ══════════════════════════════════════════════════════════════════
class C:
    RED     = '\033[91m'
    GREEN   = '\033[92m'
    YELLOW  = '\033[93m'
    CYAN    = '\033[96m'
    WHITE   = '\033[97m'
    MAGENTA = '\033[95m'
    BLUE    = '\033[94m'
    BOLD    = '\033[1m'
    DIM     = '\033[2m'
    RESET   = '\033[0m'

def enable_ansi():
    if platform.system() == "Windows":
        try:
            import ctypes
            ctypes.windll.kernel32.SetConsoleMode(
                ctypes.windll.kernel32.GetStdHandle(-11), 7)
        except Exception:
            pass

def clr():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def is_admin():
    try:
        if platform.system() == 'Windows':
            import ctypes
            return bool(ctypes.windll.shell32.IsUserAnAdmin())
        return os.geteuid() == 0
    except Exception:
        return False

def pause():
    input(f"\n{C.DIM}  ↩  Enter — menu ...{C.RESET}")

# ══════════════════════════════════════════════════════════════════
#  TYPEWRITER
# ══════════════════════════════════════════════════════════════════
def tw(text, delay=0.016, color=C.WHITE, nl=True):
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(C.RESET)
    if nl:
        sys.stdout.write('\n')

def twl(text, delay=0.013, color=C.CYAN):
    tw("  " + text, delay=delay, color=color)

# ══════════════════════════════════════════════════════════════════
#  ASCII ART
# ══════════════════════════════════════════════════════════════════
ART = [
    '                    ::::::::::::::::::                    ',
    '              ::::::::::::::::::::::::::::::              ',
    '          ::::::::::::::::::::::::::::::::::::::          ',
    '       ::::::::::::::::::::     :::::::::::::::::::       ',
    '     :::::::::::::                      :::::::::::::     ',
    '  ::::::::::::                              ::::::::::::  ',
    ' ::::::::::       ::::::::::::::::::::::       :::::::::: ',
    ' ::::::::      :::::::::::::::::::::::::::::      ::::::: ',
    '   ::::     ::::::::::::::::::::::::::::::::::     ::::   ',
    '          ::::::::::::::           :::::::::::::          ',
    '        :::::::::::                    :::::::::::        ',
    '        ::::::::       ::::::::::::       ::::::::        ',
    '          ::::     ::::::::::::::::::::     ::::          ',
    '                 ::::::::::::::::::::::::                 ',
    '               ::::::::::::::::::::::::::::               ',
    '               :::::::::          :::::::::               ',
    '                 ::::     ::::::     :::::                ',
    '                        ::::::::::                        ',
    '                       :::::::::::::                      ',
    '                      ::::::::::::::                      ',
    '                      ::::::::::::::                      ',
    '                       ::::::::::::                       ',
    '                         ::::::::                         ',
]

TITLE = [
    '═' * 62,
    '  ███████╗██╗   ██╗███████╗    ████████╗ ██████╗  ██████╗ ██╗',
    '  ██╔════╝╚██╗ ██╔╝██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║',
    '  ███████╗ ╚████╔╝ ███████╗       ██║   ██║   ██║██║   ██║██║',
    '  ╚════██║  ╚██╔╝  ╚════██║       ██║   ██║   ██║██║   ██║██║',
    '  ███████║   ██║   ███████║       ██║   ╚██████╔╝╚██████╔╝███████╗',
    '  ╚══════╝   ╚═╝   ╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝',
    '═' * 62,
    '                    ⚡  Created by Axmatov  ⚡',
    '═' * 62,
]

def print_banner():
    for i, line in enumerate(ART):
        col = C.CYAN if i < 9 else C.CYAN
        print(col + line + C.RESET)
        time.sleep(0.025)
    print()
    for line in TITLE:
        print(f"{C.CYAN}{C.BOLD}{line}{C.RESET}")
        time.sleep(0.03)
    print()

def print_mini_banner(cur_os):
    for line in ART[10:]:
        print(C.CYAN + line + C.RESET)
    os_col  = C.MAGENTA if cur_os == "windows" else C.GREEN
    os_name = "Windows"  if cur_os == "windows" else "Linux"
    print(f"{C.CYAN}{'─' * 62}{C.RESET}")
    print(f"  {C.BOLD}{C.WHITE}SYS-TOOLKIT v3.0{C.RESET}  "
          f"{C.DIM}|{C.RESET}  OS: {os_col}{os_name}{C.RESET}  "
          f"{C.DIM}| Created by Axmatov{C.RESET}")
    print(f"{C.CYAN}{'─' * 62}{C.RESET}")

# ══════════════════════════════════════════════════════════════════
#  OS SELECTION
# ══════════════════════════════════════════════════════════════════
def select_os():
    detected = "windows" if platform.system() == "Windows" else "linux"
    label    = "Windows"  if detected == "windows" else "Linux"
    clr()
    print_banner()
    time.sleep(0.1)
    print()
    twl(f"Detected OS : {C.YELLOW}{label}{C.RESET}", color=C.DIM)
    print()
    twl("[1]  Windows", color=C.MAGENTA)
    twl("[2]  Linux",   color=C.GREEN)
    twl(f"[A]  Auto-detect  ({label})", color=C.DIM)
    print()
    ch = input(f"  {C.WHITE}Choose OS [{C.CYAN}A{C.WHITE}]: {C.CYAN}").strip().lower()
    print(C.RESET, end="")
    if ch == "1":   return "windows"
    elif ch == "2": return "linux"
    else:           return detected

# ══════════════════════════════════════════════════════════════════
#  TOOL REGISTRY
# ══════════════════════════════════════════════════════════════════
TOOLS = {
    # NETWORK — both
    "1" : ("Ping",           "NET","🟢","Ping host — custom count & interval",   "easy",   "both"),
    "2" : ("Port Scan",      "NET","🟡","Multi-threaded open TCP port scanner",  "medium", "both"),
    "3" : ("Traceroute",     "NET","🟡","Trace network hops to destination",     "medium", "both"),
    "4" : ("DNS Lookup",     "NET","🟢","Resolve domain name → IP addresses",    "easy",   "both"),
    "5" : ("WHOIS",          "NET","🟢","Domain/IP registration information",    "easy",   "both"),
    "6" : ("Net Interfaces", "NET","🟢","Show all network adapters & IPs",       "easy",   "both"),
    "7" : ("Bandwidth",      "NET","🟡","Internet speed test (DL / UL)",         "medium", "both"),
    "8" : ("ARP Scan",       "NET","🔴","Discover all devices on local LAN",     "hard",   "both"),
    "9" : ("HTTP Check",     "NET","🟢","URL status, server, response time",     "easy",   "both"),
    # SYSTEM — both
    "10": ("System Info",    "SYS","🟢","OS, CPU, hostname, local IP details",  "easy",   "both"),
    "11": ("Process List",   "SYS","🟢","All running processes sorted by CPU",  "easy",   "both"),
    "12": ("Disk Usage",     "SYS","🟢","Partitions, sizes, free space",        "easy",   "both"),
    "13": ("RAM Usage",      "SYS","🟢","Memory — total / used / free",         "easy",   "both"),
    "14": ("CPU Monitor",    "SYS","🟢","Live CPU usage bar — 8 samples",       "easy",   "both"),
    "15": ("Kill Process",   "SYS","🔴","Terminate process by PID or name",     "hard",   "both"),
    "16": ("Startup List",   "SYS","🟡","Programs that execute at boot",        "medium", "both"),
    # WINDOWS only
    "17": ("Win Optimizer",  "WIN","🟡","Disable effects, SysMain, indexing",   "medium", "windows"),
    "18": ("Clear Cache",    "WIN","🟡","Delete temp & cache files",            "medium", "windows"),
    "19": ("Win Activate",   "WIN","🔴","KMS activate Windows 10/11 & Office",  "hard",   "windows"),
    "20": ("Speed Up",       "WIN","🟡","Registry tweaks for faster Windows",   "medium", "windows"),
    "21": ("Win Update",     "WIN","🟡","Check & install Windows updates",      "medium", "windows"),
    "22": ("Firewall",       "WIN","🟡","Manage Windows Firewall rules",        "medium", "windows"),
    # LINUX only
    "23": ("UFW Firewall",   "LNX","🟡","Manage UFW rules — allow/deny ports",  "medium", "linux"),
    "24": ("Pkg Manager",    "LNX","🟢","APT/YUM install, update, remove",      "easy",   "linux"),
    "25": ("Services",       "LNX","🟡","Systemd start/stop/enable/disable",    "medium", "linux"),
    "26": ("Cron Jobs",      "LNX","🟡","View, add, edit scheduled cron tasks", "medium", "linux"),
    "27": ("Log Viewer",     "LNX","🟢","syslog, auth.log, dmesg, journalctl",  "easy",   "linux"),
    # SECURITY — both
    "28": ("Hash File",      "SEC","🟢","MD5 / SHA1 / SHA256 file checksum",    "easy",   "both"),
    "29": ("Pass Gen",       "SEC","🟢","Generate cryptographically safe pwds", "easy",   "both"),
    "30": ("Vuln Scan",      "SEC","🔴","nmap-based CVE vulnerability scan",    "hard",   "both"),
    "0" : ("Exit",           "---","⬜","Exit toolkit",                         "easy",   "both"),
}

DC = {"easy": C.GREEN, "medium": C.YELLOW, "hard": C.RED}
CAT_META = {
    "NET": (C.CYAN,    "⚡ NETWORK"),
    "SYS": (C.BLUE,    "⚡ SYSTEM"),
    "WIN": (C.MAGENTA, "⚡ WINDOWS"),
    "LNX": (C.GREEN,   "⚡ LINUX"),
    "SEC": (C.YELLOW,  "⚡ SECURITY"),
}

def visible_tools(cur_os):
    return {tid: d for tid, d in TOOLS.items()
            if d[5] in ("both", cur_os) or tid == "0"}

# ══════════════════════════════════════════════════════════════════
#  MENU — 3 COLUMNS
# ══════════════════════════════════════════════════════════════════
def print_menu(cur_os):
    vt = visible_tools(cur_os)
    col_order = (["NET","SYS","WIN","SEC"]
                 if cur_os == "windows"
                 else ["NET","SYS","LNX","SEC"])
    groups = {}
    for tid, d in vt.items():
        if tid == "0": continue
        groups.setdefault(d[1], []).append(tid)

    W   = 57
    SEP = f"  {C.DIM}│{C.RESET}  "

    def render_block(cats):
        while len(cats) < 3:
            cats = cats + ["---"]
        print(f"  {C.DIM}{'─'*W}  {'─'*W}  {'─'*W}{C.RESET}")
        hdrs = []
        for cat in cats:
            cc, lbl = CAT_META.get(cat, (C.DIM, ""))
            hdrs.append(f"{cc}{C.BOLD}  {lbl:^{W-2}}  {C.RESET}")
        print(SEP.join(hdrs))
        print(f"  {C.DIM}{'─'*W}  {'─'*W}  {'─'*W}{C.RESET}")
        cols_data = [groups.get(c, []) for c in cats]
        for i in range(max((len(c) for c in cols_data), default=0)):
            parts = []
            for col in cols_data:
                if i < len(col):
                    tid = col[i]
                    _, cat, icon, desc, diff, _ = TOOLS[tid]
                    dc = DC.get(diff, C.WHITE)
                    parts.append(
                        f"  {C.WHITE}[{C.CYAN}{tid:>2}{C.WHITE}]"
                        f" {icon} {dc}{desc:<40}{C.RESET}"
                    )
                else:
                    parts.append(" " * (W + 5))
            print(SEP.join(parts))

    print()
    render_block(col_order[:3])
    print()
    render_block(col_order[3:])

    print(f"\n  {C.DIM}{'─'*185}{C.RESET}")
    print(f"  {C.WHITE}[{C.RED} 0{C.WHITE}] ⬜ {C.DIM}Exit{C.RESET}"
          f"          {C.DIM}│  type {C.CYAN}os{C.DIM} to switch OS{C.RESET}")
    print(f"  {C.DIM}{'─'*185}{C.RESET}")
    print(f"\n  {C.DIM}Difficulty:  "
          f"{C.GREEN}● Easy   {C.YELLOW}● Medium   {C.RED}● Hard (Admin/Root){C.RESET}\n")

# ══════════════════════════════════════════════════════════════════
#  NETWORK TOOLS
# ══════════════════════════════════════════════════════════════════
def t_ping():
    clr(); twl("⚡  PING", color=f"{C.CYAN}{C.BOLD}"); print()
    host = input(f"  {C.WHITE}Target IP/Host : {C.CYAN}").strip(); print(C.RESET,end="")
    try:
        count    = int(input(f"  {C.WHITE}Packet count  [4] : {C.CYAN}").strip() or "4")
        interval = float(input(f"  {C.WHITE}Interval sec  [1] : {C.CYAN}").strip() or "1")
    except ValueError:
        count, interval = 4, 1.0
    print(C.RESET, end="")
    print(f"\n{C.DIM}  {'─'*50}{C.RESET}")
    cmd = (["ping","-n",str(count),host] if platform.system()=="Windows"
           else ["ping","-c",str(count),"-i",str(interval),host])
    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, text=True)
        for line in proc.stdout:
            tw("  "+line.rstrip(), delay=0.004, color=C.GREEN)
        proc.wait()
    except FileNotFoundError:
        twl("ping not found.", color=C.RED)
    pause()

def t_port_scan():
    clr(); twl("⚡  PORT SCANNER", color=f"{C.CYAN}{C.BOLD}"); print()
    host = input(f"  {C.WHITE}Target host/IP : {C.CYAN}").strip(); print(C.RESET,end="")
    try:
        sp = int(input(f"  {C.WHITE}Start port [1]    : {C.CYAN}").strip() or "1")
        ep = int(input(f"  {C.WHITE}End port   [1024] : {C.CYAN}").strip() or "1024")
    except ValueError:
        sp, ep = 1, 1024
    print(C.RESET, end="")
    twl(f"Scanning {host}  ports {sp}–{ep} ...", color=C.DIM)
    open_ports = []; lock = threading.Lock()
    def scan(p):
        try:
            s = socket.socket(); s.settimeout(0.35)
            if s.connect_ex((host,p)) == 0:
                with lock: open_ports.append(p)
            s.close()
        except Exception: pass
    threads = []
    for p in range(sp, ep+1):
        t = threading.Thread(target=scan, args=(p,)); t.start(); threads.append(t)
        if len(threads) >= 300:
            for th in threads: th.join(); threads = []
    for th in threads: th.join()
    print()
    if open_ports:
        twl(f"Open ports : {len(open_ports)}", color=C.GREEN)
        for p in sorted(open_ports):
            try: svc = socket.getservbyport(p)
            except Exception: svc = "unknown"
            tw(f"    :{p:<6}  {svc}", delay=0.006, color=C.CYAN)
    else:
        twl("No open ports found.", color=C.YELLOW)
    pause()

def t_traceroute():
    clr(); twl("⚡  TRACEROUTE", color=f"{C.CYAN}{C.BOLD}"); print()
    host = input(f"  {C.WHITE}Target : {C.CYAN}").strip(); print(C.RESET,end=""); print()
    cmd = ["tracert",host] if platform.system()=="Windows" else ["traceroute",host]
    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, text=True)
        for line in proc.stdout:
            tw("  "+line.rstrip(), delay=0.005, color=C.CYAN)
        proc.wait()
    except FileNotFoundError:
        twl("traceroute not found.  Linux: sudo apt install traceroute", color=C.RED)
    pause()

def t_dns():
    clr(); twl("⚡  DNS LOOKUP", color=f"{C.CYAN}{C.BOLD}"); print()
    domain = input(f"  {C.WHITE}Domain : {C.CYAN}").strip(); print(C.RESET,end=""); print()
    try:
        h, aliases, ips = socket.gethostbyname_ex(domain)
        twl(f"Hostname : {h}",       color=C.GREEN)
        twl(f"Aliases  : {aliases}", color=C.CYAN)
        twl(f"IPs      : {ips}",     color=C.YELLOW)
    except Exception as e:
        twl(f"Error: {e}", color=C.RED)
    pause()

def t_whois():
    clr(); twl("⚡  WHOIS", color=f"{C.CYAN}{C.BOLD}"); print()
    target = input(f"  {C.WHITE}Domain/IP : {C.CYAN}").strip(); print(C.RESET,end=""); print()
    try:
        r = subprocess.run(["whois",target], capture_output=True, text=True, timeout=15)
        for line in r.stdout.split('\n')[:50]:
            if line.strip(): tw("  "+line, delay=0.003, color=C.DIM)
    except FileNotFoundError:
        twl("whois not found.  Install: sudo apt install whois", color=C.RED)
    pause()

def t_netinfo():
    clr(); twl("⚡  NETWORK INTERFACES", color=f"{C.CYAN}{C.BOLD}"); print()
    if platform.system() == "Windows":
        r = subprocess.run(["ipconfig","/all"], capture_output=True, text=True)
    else:
        try:    r = subprocess.run(["ip","addr"], capture_output=True, text=True)
        except Exception: r = subprocess.run(["ifconfig"], capture_output=True, text=True)
    for line in r.stdout.split('\n'):
        tw("  "+line, delay=0.003, color=C.CYAN)
    pause()

def t_bandwidth():
    clr(); twl("⚡  BANDWIDTH TEST", color=f"{C.CYAN}{C.BOLD}"); print()
    twl("Installing speedtest-cli if needed ...", color=C.DIM)
    subprocess.run([sys.executable,"-m","pip","install","speedtest-cli","-q"])
    try:
        import speedtest
        twl("Finding best server ...", color=C.DIM)
        st = speedtest.Speedtest(); st.get_best_server()
        twl("Testing download ...", color=C.DIM)
        dl = st.download()/1_000_000
        twl("Testing upload ...", color=C.DIM)
        ul = st.upload()/1_000_000
        print()
        twl(f"Download : {dl:.2f} Mbps", color=C.GREEN)
        twl(f"Upload   : {ul:.2f} Mbps", color=C.CYAN)
        twl(f"Ping     : {st.results.ping:.1f} ms", color=C.YELLOW)
    except Exception as e:
        twl(f"Error: {e}", color=C.RED)
    pause()

def t_arp():
    clr(); twl("⚡  ARP SCAN", color=f"{C.CYAN}{C.BOLD}")
    if not is_admin():
        twl("⚠  Admin/Root required!", color=C.RED); pause(); return
    subnet = input(f"  {C.WHITE}Subnet (e.g. 192.168.1.0/24) : {C.CYAN}").strip()
    print(C.RESET,end=""); print()
    for tool, cmd in [("arp-scan",["arp-scan","--localnet"]),
                      ("nmap",    ["nmap","-sn",subnet])]:
        try:
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT, text=True)
            for line in proc.stdout:
                tw("  "+line.rstrip(), delay=0.007, color=C.GREEN)
            proc.wait(); break
        except FileNotFoundError: continue
    else:
        twl("Neither arp-scan nor nmap found.", color=C.RED)
    pause()

def t_http():
    clr(); twl("⚡  HTTP CHECK", color=f"{C.CYAN}{C.BOLD}"); print()
    url = input(f"  {C.WHITE}URL : {C.CYAN}").strip(); print(C.RESET,end=""); print()
    try:
        import urllib.request
        req = urllib.request.Request(url, headers={"User-Agent":"SysToolkit/3.0"})
        t0  = time.time()
        res = urllib.request.urlopen(req, timeout=10)
        ms  = (time.time()-t0)*1000
        twl(f"Status  : {res.status} {res.reason}", color=C.GREEN)
        twl(f"Server  : {res.headers.get('Server','N/A')}", color=C.CYAN)
        twl(f"Content : {res.headers.get('Content-Type','N/A')}", color=C.CYAN)
        twl(f"Time    : {ms:.0f} ms", color=C.YELLOW)
    except Exception as e:
        twl(f"Error: {e}", color=C.RED)
    pause()

# ══════════════════════════════════════════════════════════════════
#  SYSTEM TOOLS
# ══════════════════════════════════════════════════════════════════
def t_sysinfo():
    clr(); twl("⚡  SYSTEM INFO", color=f"{C.CYAN}{C.BOLD}"); print()
    info = {
        "OS"       : platform.system()+" "+platform.release(),
        "Version"  : platform.version(),
        "Machine"  : platform.machine(),
        "CPU"      : platform.processor() or "N/A",
        "Python"   : platform.python_version(),
        "Hostname" : socket.gethostname(),
        "Local IP" : socket.gethostbyname(socket.gethostname()),
        "Admin"    : "Yes" if is_admin() else "No",
    }
    for k, v in info.items():
        tw(f"  {C.CYAN}{k:<12}{C.WHITE}{v}{C.RESET}", delay=0.006)
    pause()

def t_procs():
    clr(); twl("⚡  PROCESS LIST", color=f"{C.CYAN}{C.BOLD}"); print()
    if platform.system()=="Windows":
        r = subprocess.run(["tasklist"], capture_output=True, text=True)
    else:
        r = subprocess.run(["ps","aux","--sort=-%cpu"], capture_output=True, text=True)
    for line in r.stdout.split('\n')[:45]:
        tw("  "+line, delay=0.002, color=C.DIM)
    pause()

def t_disk():
    clr(); twl("⚡  DISK USAGE", color=f"{C.CYAN}{C.BOLD}"); print()
    if platform.system()=="Windows":
        r = subprocess.run(["wmic","logicaldisk","get","size,freespace,caption"],
                           capture_output=True, text=True)
    else:
        r = subprocess.run(["df","-h"], capture_output=True, text=True)
    for line in r.stdout.split('\n'):
        tw("  "+line, delay=0.005, color=C.CYAN)
    pause()

def t_ram():
    clr(); twl("⚡  RAM USAGE", color=f"{C.CYAN}{C.BOLD}"); print()
    if platform.system()=="Windows":
        r = subprocess.run(["wmic","OS","get","FreePhysicalMemory,TotalVisibleMemorySize"],
                           capture_output=True, text=True)
    else:
        r = subprocess.run(["free","-h"], capture_output=True, text=True)
    for line in r.stdout.split('\n'):
        tw("  "+line, delay=0.005, color=C.CYAN)
    pause()

def t_cpu():
    clr(); twl("⚡  CPU MONITOR  (live 8s)", color=f"{C.CYAN}{C.BOLD}"); print()
    try:
        import psutil
        for _ in range(8):
            pct    = psutil.cpu_percent(interval=1)
            filled = int(pct/5)
            bar    = "█"*filled + "░"*(20-filled)
            col    = C.GREEN if pct<50 else C.YELLOW if pct<80 else C.RED
            print(f"\r  CPU [{col}{bar}{C.RESET}] {col}{pct:5.1f}%{C.RESET}  ",
                  end="", flush=True)
        print()
    except ImportError:
        if platform.system()=="Windows":
            subprocess.run(["wmic","cpu","get","loadpercentage"])
        else:
            subprocess.run(["top","-bn1"])
    pause()

def t_kill():
    clr(); twl("⚡  KILL PROCESS", color=f"{C.RED}{C.BOLD}"); print()
    name = input(f"  {C.WHITE}Name or PID : {C.CYAN}").strip(); print(C.RESET,end="")
    ok   = input(f"  {C.RED}Kill '{name}'? [y/N] : {C.CYAN}").strip().lower()
    print(C.RESET,end="")
    if ok == "y":
        if platform.system()=="Windows":
            if name.isdigit(): subprocess.run(["taskkill","/PID",name,"/F"])
            else:              subprocess.run(["taskkill","/IM",name,"/F"])
        else:
            subprocess.run(["pkill","-f",name])
        twl("Done.", color=C.GREEN)
    pause()

def t_startup():
    clr(); twl("⚡  STARTUP LIST", color=f"{C.CYAN}{C.BOLD}"); print()
    if platform.system()=="Windows":
        r = subprocess.run(["wmic","startup","get","caption,command"],
                           capture_output=True, text=True)
        for line in r.stdout.split('\n'):
            if line.strip(): tw("  "+line, delay=0.005, color=C.CYAN)
    else:
        for path in ["/etc/init.d/","/etc/systemd/system/"]:
            if os.path.exists(path):
                twl(f"Path: {path}", color=C.CYAN)
                r = subprocess.run(["ls","-la",path], capture_output=True, text=True)
                for line in r.stdout.split('\n')[:20]:
                    tw("  "+line, delay=0.003, color=C.DIM)
    pause()

# ══════════════════════════════════════════════════════════════════
#  WINDOWS-ONLY TOOLS
# ══════════════════════════════════════════════════════════════════
def _need_win():
    if platform.system()!="Windows":
        twl("⚠  This tool requires Windows.", color=C.YELLOW); pause(); return False
    return True

def t_winopt():
    if not _need_win(): return
    clr(); twl("⚡  WINDOWS OPTIMIZER", color=f"{C.MAGENTA}{C.BOLD}"); print()
    steps = [
        ("Disable visual effects",
         'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VisualEffects" /v VisualFXSetting /t REG_DWORD /d 2 /f'),
        ("Disable SysMain",
         "sc config SysMain start= disabled & net stop SysMain"),
        ("Disable search indexing",
         "sc config WSearch start= disabled & net stop WSearch"),
        ("Enable SSD TRIM",
         "fsutil behavior set DisableDeleteNotify 0"),
        ("High Performance power plan",
         "powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"),
    ]
    for msg, cmd in steps:
        tw(f"  → {msg} ... ", delay=0.01, color=C.DIM, nl=False)
        res = subprocess.run(cmd, shell=True, capture_output=True)
        print(f"{C.GREEN}✔{C.RESET}" if res.returncode==0 else f"{C.RED}✗{C.RESET}")
        time.sleep(0.1)
    print(); twl("Optimization complete!", color=C.GREEN)
    pause()

def t_clearcache():
    if not _need_win(): return
    clr(); twl("⚡  CLEAR WINDOWS CACHE", color=f"{C.MAGENTA}{C.BOLD}"); print()
    dirs = [
        os.environ.get("TEMP",""), os.environ.get("TMP",""),
        "C:\\Windows\\Temp", "C:\\Windows\\Prefetch",
        os.path.expanduser("~\\AppData\\Local\\Temp"),
    ]
    total = 0
    for d in dirs:
        if not d or not os.path.exists(d): continue
        count = 0
        for root, _, files in os.walk(d):
            for f in files:
                try:
                    fp = os.path.join(root,f)
                    total += os.path.getsize(fp)
                    os.remove(fp); count += 1
                except Exception: pass
        twl(f"Cleaned: {d}  ({count} files)", color=C.CYAN)
    print(); twl(f"Total freed: {total/1024/1024:.1f} MB", color=C.GREEN)
    pause()

def t_activate():
    if not _need_win(): return
    clr(); twl("⚡  ACTIVATION  (KMS)", color=f"{C.MAGENTA}{C.BOLD}"); print()
    twl("[1]  Windows 10/11 Pro",  color=C.CYAN)
    twl("[2]  Windows 10/11 Home", color=C.CYAN)
    twl("[3]  Office 2019 / 2021", color=C.CYAN)
    ch = input(f"\n  {C.WHITE}Choice : {C.CYAN}").strip(); print(C.RESET,end=""); print()
    keys = {
        "1": ("Windows 10/11 Pro",  "W269N-WFGWX-YVC9B-4J6C9-T83GX"),
        "2": ("Windows 10/11 Home", "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99"),
    }
    if ch in keys:
        name, key = keys[ch]
        twl(f"Activating {name} ...", color=C.DIM)
        for cmd in [f"slmgr /ipk {key}","slmgr /skms kms8.msguides.com","slmgr /ato"]:
            twl(f"→ {cmd}", color=C.DIM)
            subprocess.run(cmd, shell=True)
    elif ch == "3":
        for op in [r"C:\Program Files\Microsoft Office\Office16",
                   r"C:\Program Files (x86)\Microsoft Office\Office16"]:
            vbs = os.path.join(op,"ospp.vbs")
            if os.path.exists(vbs):
                for cmd in [
                    f'cscript "{vbs}" /inpkey:NMMKJ-6RK4F-KMJVX-8D9MJ-6MWKP',
                    f'cscript "{vbs}" /sethst:kms8.msguides.com',
                    f'cscript "{vbs}" /act',
                ]: subprocess.run(cmd, shell=True)
                break
        else:
            twl("Office not found.", color=C.RED)
    print(); twl("Done.", color=C.GREEN)
    pause()

def t_speedup():
    if not _need_win(): return
    clr(); twl("⚡  WINDOWS SPEED UP", color=f"{C.MAGENTA}{C.BOLD}"); print()
    tweaks = [
        ("Disable animations",
         'reg add "HKCU\\Control Panel\\Desktop" /v UserPreferencesMask /t REG_BINARY /d 9012038010000000 /f'),
        ("Disable transparency",
         'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize" /v EnableTransparency /t REG_DWORD /d 0 /f'),
        ("Fast startup",
         'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Power" /v HiberbootEnabled /t REG_DWORD /d 1 /f'),
        ("Remove startup delay",
         'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Serialize" /v StartupDelayInMSec /t REG_DWORD /d 0 /f'),
        ("Flush DNS cache",    "ipconfig /flushdns"),
        ("Disable hibernation","powercfg -h off"),
    ]
    for msg, cmd in tweaks:
        tw(f"  → {msg} ... ", delay=0.01, color=C.DIM, nl=False)
        res = subprocess.run(cmd, shell=True, capture_output=True)
        print(f"{C.GREEN}✔{C.RESET}" if res.returncode==0 else f"{C.RED}✗{C.RESET}")
        time.sleep(0.08)
    print(); twl("Restart recommended.", color=C.GREEN)
    pause()

def t_winupdate():
    if not _need_win(): return
    clr(); twl("⚡  WINDOWS UPDATE", color=f"{C.MAGENTA}{C.BOLD}"); print()
    twl("Running via PowerShell ...", color=C.DIM)
    subprocess.run([
        "powershell","-Command",
        "Install-Module PSWindowsUpdate -Force -EA SilentlyContinue; "
        "Get-WindowsUpdate; Install-WindowsUpdate -AcceptAll -AutoReboot"
    ])
    pause()

def t_winfirewall():
    if not _need_win(): return
    clr(); twl("⚡  WINDOWS FIREWALL", color=f"{C.MAGENTA}{C.BOLD}"); print()
    twl("[1]  Status",         color=C.CYAN)
    twl("[2]  Enable",         color=C.CYAN)
    twl("[3]  Disable",        color=C.CYAN)
    twl("[4]  Block a port",   color=C.CYAN)
    twl("[5]  Allow a port",   color=C.CYAN)
    twl("[6]  List all rules", color=C.CYAN)
    ch = input(f"\n  {C.WHITE}Choice : {C.CYAN}").strip(); print(C.RESET,end=""); print()
    cmds = {
        "1": "netsh advfirewall show allprofiles",
        "2": "netsh advfirewall set allprofiles state on",
        "3": "netsh advfirewall set allprofiles state off",
        "6": "netsh advfirewall firewall show rule name=all",
    }
    if ch in cmds:
        subprocess.run(cmds[ch], shell=True)
    elif ch in ("4","5"):
        port   = input(f"  {C.WHITE}Port : {C.CYAN}").strip(); print(C.RESET,end="")
        action = "block" if ch=="4" else "allow"
        subprocess.run(
            f'netsh advfirewall firewall add rule name="{action}_{port}" '
            f'dir=in action={action} protocol=TCP localport={port}',shell=True)
        twl(f"Port {port} {action}ed.", color=C.GREEN)
    pause()

# ══════════════════════════════════════════════════════════════════
#  LINUX-ONLY TOOLS
# ══════════════════════════════════════════════════════════════════
def _need_lnx():
    if platform.system()=="Windows":
        twl("⚠  This tool requires Linux.", color=C.YELLOW); pause(); return False
    return True

def t_ufw():
    if not _need_lnx(): return
    clr(); twl("⚡  UFW FIREWALL", color=f"{C.GREEN}{C.BOLD}"); print()
    twl("[1]  Status verbose", color=C.CYAN)
    twl("[2]  Enable",         color=C.CYAN)
    twl("[3]  Disable",        color=C.CYAN)
    twl("[4]  Allow port",     color=C.CYAN)
    twl("[5]  Deny port",      color=C.CYAN)
    twl("[6]  Delete rule",    color=C.CYAN)
    ch = input(f"\n  {C.WHITE}Choice : {C.CYAN}").strip(); print(C.RESET,end=""); print()
    if   ch=="1": subprocess.run(["ufw","status","verbose"])
    elif ch=="2": subprocess.run(["ufw","enable"])
    elif ch=="3": subprocess.run(["ufw","disable"])
    elif ch in ("4","5"):
        p = input(f"  {C.WHITE}Port : {C.CYAN}").strip(); print(C.RESET,end="")
        subprocess.run(["ufw","allow" if ch=="4" else "deny",p])
    elif ch=="6":
        p = input(f"  {C.WHITE}Rule (e.g. 22/tcp) : {C.CYAN}").strip(); print(C.RESET,end="")
        subprocess.run(["ufw","delete",p])
    pause()

def t_pkg():
    if not _need_lnx(): return
    clr(); twl("⚡  PACKAGE MANAGER", color=f"{C.GREEN}{C.BOLD}"); print()
    twl("[1]  Update list",    color=C.CYAN)
    twl("[2]  Upgrade all",    color=C.CYAN)
    twl("[3]  Install pkg",    color=C.CYAN)
    twl("[4]  Remove pkg",     color=C.CYAN)
    twl("[5]  Search pkg",     color=C.CYAN)
    twl("[6]  List installed", color=C.CYAN)
    ch = input(f"\n  {C.WHITE}Choice : {C.CYAN}").strip(); print(C.RESET,end=""); print()
    pm = "apt" if os.path.exists("/usr/bin/apt") else "yum"
    if   ch=="1": subprocess.run([pm,"update"])
    elif ch=="2": subprocess.run([pm,"upgrade","-y"])
    elif ch in ("3","4","5"):
        pkg = input(f"  {C.WHITE}Package : {C.CYAN}").strip(); print(C.RESET,end="")
        if   ch=="3": subprocess.run([pm,"install","-y",pkg])
        elif ch=="4": subprocess.run([pm,"remove","-y",pkg])
        else: subprocess.run(["apt","search",pkg] if pm=="apt" else ["yum","search",pkg])
    elif ch=="6":
        subprocess.run(["dpkg","--list"] if pm=="apt" else ["rpm","-qa"])
    pause()

def t_services():
    if not _need_lnx(): return
    clr(); twl("⚡  SERVICE MANAGER", color=f"{C.GREEN}{C.BOLD}"); print()
    twl("[1]  List all",        color=C.CYAN)
    twl("[2]  Status",          color=C.CYAN)
    twl("[3]  Start",           color=C.CYAN)
    twl("[4]  Stop",            color=C.CYAN)
    twl("[5]  Restart",         color=C.CYAN)
    twl("[6]  Enable at boot",  color=C.CYAN)
    twl("[7]  Disable at boot", color=C.CYAN)
    ch = input(f"\n  {C.WHITE}Choice : {C.CYAN}").strip(); print(C.RESET,end=""); print()
    if ch=="1":
        subprocess.run(["systemctl","list-units","--type=service","--all"])
    else:
        svc = input(f"  {C.WHITE}Service name : {C.CYAN}").strip(); print(C.RESET,end="")
        cmds = {
            "2":["systemctl","status",svc],  "3":["systemctl","start",svc],
            "4":["systemctl","stop",svc],    "5":["systemctl","restart",svc],
            "6":["systemctl","enable",svc],  "7":["systemctl","disable",svc],
        }
        if ch in cmds: subprocess.run(cmds[ch])
    pause()

def t_cron():
    if not _need_lnx(): return
    clr(); twl("⚡  CRON MANAGER", color=f"{C.GREEN}{C.BOLD}"); print()
    twl("[1]  View crontab",   color=C.CYAN)
    twl("[2]  Add cron job",   color=C.CYAN)
    twl("[3]  Edit (nano)",    color=C.CYAN)
    twl("[4]  Remove crontab", color=C.CYAN)
    ch = input(f"\n  {C.WHITE}Choice : {C.CYAN}").strip(); print(C.RESET,end=""); print()
    if ch=="1":
        r = subprocess.run(["crontab","-l"], capture_output=True, text=True)
        for line in r.stdout.split('\n'): tw("  "+line, delay=0.005, color=C.CYAN)
    elif ch=="2":
        job = input(f"  {C.WHITE}Cron expr (e.g. 0 2 * * * /script.sh) : {C.CYAN}").strip()
        print(C.RESET,end="")
        r   = subprocess.run(["crontab","-l"], capture_output=True, text=True)
        new = (r.stdout if r.returncode==0 else "") + job + "\n"
        p   = subprocess.Popen(["crontab","-"], stdin=subprocess.PIPE)
        p.communicate(new.encode())
        twl("Job added.", color=C.GREEN)
    elif ch=="3": subprocess.run(["crontab","-e"])
    elif ch=="4":
        ok = input(f"  {C.RED}Remove ALL cron jobs? [y/N] : {C.CYAN}").strip().lower()
        print(C.RESET,end="")
        if ok=="y":
            subprocess.run(["crontab","-r"])
            twl("Crontab removed.", color=C.GREEN)
    pause()

def t_logs():
    if not _need_lnx(): return
    clr(); twl("⚡  LOG VIEWER", color=f"{C.GREEN}{C.BOLD}"); print()
    twl("[1]  syslog   (/var/log/syslog)",  color=C.CYAN)
    twl("[2]  auth     (/var/log/auth.log)", color=C.CYAN)
    twl("[3]  kernel   (dmesg)",             color=C.CYAN)
    twl("[4]  journal  (journalctl -n 60)",  color=C.CYAN)
    twl("[5]  kern.log (/var/log/kern.log)", color=C.CYAN)
    ch = input(f"\n  {C.WHITE}Choice : {C.CYAN}").strip(); print(C.RESET,end=""); print()
    srcs = {
        "1":["tail","-n","60","/var/log/syslog"],
        "2":["tail","-n","60","/var/log/auth.log"],
        "3":["dmesg","--color=never"],
        "4":["journalctl","-n","60","--no-pager"],
        "5":["tail","-n","60","/var/log/kern.log"],
    }
    if ch in srcs:
        r = subprocess.run(srcs[ch], capture_output=True, text=True)
        for line in r.stdout.split('\n'):
            tw("  "+line, delay=0.003, color=C.DIM)
    pause()

# ══════════════════════════════════════════════════════════════════
#  SECURITY TOOLS
# ══════════════════════════════════════════════════════════════════
def t_hash():
    clr(); twl("⚡  FILE HASH", color=f"{C.YELLOW}{C.BOLD}"); print()
    path = input(f"  {C.WHITE}File path : {C.CYAN}").strip(); print(C.RESET,end=""); print()
    if not os.path.exists(path):
        twl("File not found.", color=C.RED); pause(); return
    with open(path,"rb") as f: data = f.read()
    twl(f"MD5    : {hashlib.md5(data).hexdigest()}",    color=C.GREEN)
    twl(f"SHA1   : {hashlib.sha1(data).hexdigest()}",   color=C.CYAN)
    twl(f"SHA256 : {hashlib.sha256(data).hexdigest()}", color=C.YELLOW)
    pause()

def t_passgen():
    clr(); twl("⚡  PASSWORD GENERATOR", color=f"{C.YELLOW}{C.BOLD}"); print()
    try:
        length = int(input(f"  {C.WHITE}Length [16] : {C.CYAN}").strip() or "16")
        count  = int(input(f"  {C.WHITE}Count  [5]  : {C.CYAN}").strip() or "5")
    except ValueError:
        length, count = 16, 5
    print(C.RESET,end=""); print()
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    twl("Generated passwords:", color=C.GREEN)
    for i in range(count):
        pw = ''.join(secrets.choice(chars) for _ in range(length))
        tw(f"  {i+1}.  {pw}", delay=0.013, color=C.CYAN)
    pause()

def t_vuln():
    clr(); twl("⚡  VULN SCANNER", color=f"{C.YELLOW}{C.BOLD}")
    if not is_admin():
        twl("⚠  Admin/Root required!", color=C.RED); pause(); return
    host = input(f"  {C.WHITE}Target : {C.CYAN}").strip(); print(C.RESET,end=""); print()
    twl("Running nmap --script=vuln  (1–2 min) ...", color=C.DIM)
    try:
        r = subprocess.run(["nmap","-sV","--script=vuln",host],
                           capture_output=True, text=True, timeout=180)
        for line in r.stdout.split('\n'):
            col = (C.RED if any(k in line.lower()
                   for k in ("vuln","cve","critical","high","risk")) else C.DIM)
            tw("  "+line, delay=0.003, color=col)
    except FileNotFoundError:
        twl("nmap not found.  Linux: sudo apt install nmap  |  Windows: choco install nmap",
            color=C.RED)
    except subprocess.TimeoutExpired:
        twl("Scan timed out.", color=C.YELLOW)
    pause()

# ══════════════════════════════════════════════════════════════════
#  DISPATCH
# ══════════════════════════════════════════════════════════════════
FMAP = {
    "1":  t_ping,       "2":  t_port_scan,  "3":  t_traceroute,
    "4":  t_dns,        "5":  t_whois,      "6":  t_netinfo,
    "7":  t_bandwidth,  "8":  t_arp,        "9":  t_http,
    "10": t_sysinfo,    "11": t_procs,      "12": t_disk,
    "13": t_ram,        "14": t_cpu,        "15": t_kill,
    "16": t_startup,
    "17": t_winopt,     "18": t_clearcache, "19": t_activate,
    "20": t_speedup,    "21": t_winupdate,  "22": t_winfirewall,
    "23": t_ufw,        "24": t_pkg,        "25": t_services,
    "26": t_cron,       "27": t_logs,
    "28": t_hash,       "29": t_passgen,    "30": t_vuln,
}

# ══════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════
def main():
    enable_ansi()
    cur_os    = select_os()
    vt        = visible_tools(cur_os)
    first_run = True

    while True:
        clr()
        if first_run:
            print_banner()
            first_run = False
        else:
            print_mini_banner(cur_os)

        print_menu(cur_os)

        choice = input(
            f"  {C.WHITE}Select [{C.CYAN}0{C.WHITE}–{C.CYAN}30{C.WHITE}]"
            f" or {C.DIM}os{C.RESET} to switch : {C.CYAN}"
        ).strip().lower()
        print(C.RESET, end="")

        if choice == "0":
            clr()
            tw("\n  Goodbye!  — Axmatov\n", delay=0.04, color=C.CYAN)
            sys.exit(0)
        elif choice == "os":
            cur_os    = select_os()
            vt        = visible_tools(cur_os)
            first_run = True
        elif choice in vt and choice in FMAP:
            clr(); FMAP[choice]()
        elif choice in FMAP:
            twl(f"⚠  Tool #{choice} is not available for "
                f"{'Windows' if cur_os=='windows' else 'Linux'}.", color=C.YELLOW)
            time.sleep(1.2)
        else:
            twl("Invalid choice. Try again.", color=C.RED)
            time.sleep(0.7)

if __name__ == "__main__":
    main()
