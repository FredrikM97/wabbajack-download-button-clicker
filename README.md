# Auto Image Clicker

Small utility that searches for an image on your screen and clicks it when found.

Project structure example:

auto_clicker.py
images/
└── download_button_1.png
requirements.txt
setup.sh
setup.bat
build.sh

## Setup (Recommended)

Run:
source setup.sh

Run:
setup.sh

This will:
- Create venv\
- Activate it
- Install all requirements


## Usage

If your image is inside the project:

python auto_clicker.py --image "images\download_button_1.png"

You can also use an absolute path if preferred.

## Common Examples

Fast mode:
python auto_clicker.py --image "images/download_button_1.png" --speed fast

Higher confidence:
python auto_clicker.py --image "images/download_button_1.png" --confidence 0.9


Arguments
```
--image           (required) Path to image file
--confidence      Match confidence (default 0.8)
--retries         Retry attempts per loop (default 3)
--retry-delay     Delay between retries (default 0.5)
--loop-delay      Delay between loops (default 7.0)
--speed           slow | normal | fast
--exit-hotkey     Default: ctrl+shift+e
```