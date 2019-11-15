#!/bin/bash
apt install tesseract-ocr
apt install bsdgames
wget https://storage.googleapis.com/gctf-2018-attachments/7ad5a7d71a7ac5f5056bb95dd326603e77a38f25a76a1fb7f7e6461e7d27b6a3
file 7ad5a7d71a7ac5f5056bb95dd326603e77a38f25a76a1fb7f7e6461e7d27b6a3
unzip 7ad5a7d71a7ac5f5056bb95dd326603e77a38f25a76a1fb7f7e6461e7d27b6a3
tesseract OCR_is_cool.png O
clear
cat O.txt |caesar 7|grep "CTF" 
