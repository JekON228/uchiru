#!/bin/bash
trap "echo ' Trapped Ctrl-C'" SIGHUP
source venv/bin/activate
python3  main.py

