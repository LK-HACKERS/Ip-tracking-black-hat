🌐 IP Tracking Tool

LK-HACKERS
Track any website's IP address directly from your Android Termux!

---

📱 Description

This is an IP Address Tracking Tool built for Android Termux that resolves any domain to its corresponding IPv4 address.
It features a stylish hacker-styled interface with:

· 🔴 Red ASCII Banner with tool branding
· 🟢 Real-time domain resolution
· 🟡 URL cleaning (removes http://, https://, and trailing slashes)
· 🔵 Color-coded output for better readability
· ⚡ Error handling for invalid domains

---

🛠️ Installation Guide (Termux)

Follow these steps to install and run:

```bash
pkg update && pkg upgrade
pkg install python git -y
git clone https://github.com/LK-HACKERS/Ip-tracking-black-hat.git
cd Ip-tracking-black-hat
python run.py
```

Note: The main script file is track.py (or the filename containing the code)

---

🚀 How to Use

1. After installation, run:
   ```bash
   python track.py
   ```
2. The tool will display a banner and prompt:
   ```
   Enter Target Website (e.g., google.com):
   ```
3. Enter any domain name (with or without http:// or https://):
   ```
   Enter Target Website (e.g., google.com): facebook.com
   ```
4. The tool will resolve and display the IP address:
   ```
   ========================================
    TARGET: facebook.com
    IP ADDRESS: 157.240.1.35
   ========================================
   [+] Process Completed ip Tracking Successfully!
   ```

---

📸 Output Example

```
 ██╗██████╗
 ██║██╔══██╗
 ██║██████╔╝
 ██║██╔═══╝
 ██║██║
 ╚═╝╚═╝

 ████████╗██████╗  █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗
 ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝
    ██║   ██████╔╝███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗
    ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║
    ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝
    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝

    ---------------------------------------------
    [ TARGET: IP ADDRESS TRACKING LK-HACKERS BLACK HAT TOOL ]
    [ DEVELOPED BY: CYBER BLACK LION ]
    ---------------------------------------------

[!] Ready to hunt IP address...
Enter Target Website (e.g., google.com): youtube.com

========================================
 TARGET: youtube.com
 IP ADDRESS: 142.250.185.110
========================================
[+] Process Completed ip Tracking Successfully!
```

---

⚠️ Important Notice

DISCLAIMER: This tool is designed for educational purposes only.

· Only use on domains you own or have explicit permission to test
· Unauthorized tracking or scanning may violate laws in your country
· The developer is not responsible for any misuse of this tool

---

🛡️ Features

Feature Description
🎨 Color Output Red, Green, Yellow, Cyan for visual clarity
🧹 URL Cleaning Automatically removes protocols and slashes
⚡ Fast Resolution Uses Python's built-in socket library
🛑 Error Handling Gracefully handles invalid domains
📱 Termux Optimized Works perfectly on Android Termux

---

👨‍💻 Developer

CYBER BLACK LION
LK-HACKERS Team

For Educational Purposes Only

---

📌 Version

v1.0 – IP Tracking Tool

---

🔧 Requirements

· Python 3.x
· Internet connection (for DNS resolution)
· Termux or any Linux terminal

---

❓ Support

If you encounter any issues, please open an Issue.

---

📝 License

This project is for educational purposes only. Use at your own risk.

---

Happy Tracking! 🔥
