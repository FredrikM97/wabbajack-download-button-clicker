#!/bin/bash

# Detect OS
OS="$(uname -s)"
echo "Detected OS: $OS"

EXE_NAME="auto_clicker"
if [[ "$OS" == MINGW* || "$OS" == CYGWIN* || "$OS" == MSYS* ]]; then
    EXE_NAME+=".exe"
fi

echo "Cleaning previous builds..."
# Clean for all platforms using bash commands
rm -rf build dist *.spec 2>/dev/null

echo "Building executable..."
pyinstaller --onefile auto_clicker.py --hidden-import=cv2 --clean

echo "Cleaning temporary files..."
rm -rf build *.spec 2>/dev/null

echo "Done. Executable is in dist/$EXE_NAME"