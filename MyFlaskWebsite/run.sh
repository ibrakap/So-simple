#!/bin/bash
echo -e "\033[0;31mStarting flask server at background\e[0m"
gunicorn --bind 0.0.0.0:80 app.py:app -D

