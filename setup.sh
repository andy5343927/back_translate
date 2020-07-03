#!/usr/bin/env bash
pip install -r requirements.txt
brew install wget
python dowload_data.py
sh back_translate/download.sh