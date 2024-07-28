#!/bin/bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python
python -m --ensurepip upgrade
pip3 install cmu-graphics
python3 main.py
echo "running"
