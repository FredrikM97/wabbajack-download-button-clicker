Auto Image Clicker

Small utility that searches for an image on your screen and clicks it when found.

Project structure example:

auto_clicker.py
images/
└── download_button_1.png
requirements.txt
setup.sh
setup.bat
build.sh

---

Setup (Recommended)

Linux / macOS / Windows Git Bash:

Run:
source setup.sh

This will:
- Create a virtual environment venv/
- Activate it in the current shell
- Install all dependencies

Important: On Linux/macOS, the script must be sourced, not executed (./setup.sh will not keep the venv active).

Windows:

Run:
setup.bat

This will:
- Create venv\
- Activate it
- Install all requirements

---

Usage

If your image is inside the project:

Linux/macOS:
python auto_clicker.py --image "images/download_button_1.png"

Windows:
python auto_clicker.py --image "images\download_button_1.png"

You can also use an absolute path if preferred.

---

Common Examples

Fast mode:
python auto_clicker.py --image "images/download_button_1.png" --speed fast

Higher confidence:
python auto_clicker.py --image "images/download_button_1.png" --confidence 0.9

---

Arguments

--image           (required) Path to image file
--confidence      Match confidence (default 0.8)
--retries         Retry attempts per loop (default 3)
--retry-delay     Delay between retries (default 0.5)
--loop-delay      Delay between loops (default 7.0)
--speed           slow | normal | fast
--exit-hotkey     Default: ctrl+shift+e

Stop the program with the configured hotkey or CTRL+C.

---

Build Executable

Use the cross-platform build script build.sh:

./build.sh

This will:
- Detect your OS
- Clean old build files (build/, .spec)
- Build a single executable in dist/
- Remove temporary build folders and spec files automatically

After building:
- Linux / macOS: dist/auto_clicker
- Windows (Git Bash, Cygwin, WSL): dist/auto_clicker.exe

Run example:

Linux/macOS:
dist/auto_clicker --image "images/download_button_1.png"

Windows:
dist\auto_clicker.exe --image "images\download_button_1.png"