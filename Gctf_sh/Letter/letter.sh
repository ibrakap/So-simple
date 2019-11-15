#!/bin/bash
apt install python-pdfminer
wget https://storage.googleapis.com/gctf-2018-attachments/5a0fad5699f75dee39434cc26587411b948e0574a545ef4157e5bf4700e9d62a
mv 5a0fad5699f75dee39434cc26587411b948e0574a545ef4157e5bf4700e9d62a Letter
unzip Letter
clear
echo "Flag:"
pdf2txt challenge.pdf | grep "CTF"
