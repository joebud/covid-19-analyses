#!/bin/bash

# pip install PyInstaller

pyi-makespec --name COVID-19-ANALYSIS-debug  --log-level=DEBUG  --onefile   ./src/COVID-19-ANALYSIS.py  2> build-debug.txt    
              
pyinstaller --distpath=./debug/dist/lin/  --workpath=./debug/build/lin/  --noconfirm     COVID-19-ANALYSIS-debug.spec

cp ./README.* ./debug/dist/lin/COVID-19-ANALYSIS/
cp -R ./data ./debug/dist/lin/COVID-19-ANALYSIS/
 
read -p "Press [Enter] key..."

 

