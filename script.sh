#!/bin/bash
trap "echo ' Trapped Ctrl-C'" SIGHUP
source /bin/activate
python3  main.py

