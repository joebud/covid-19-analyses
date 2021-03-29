#!/bin/bash

pyi-makespec --name COVID-19-ANALYSIS   --log-level=INFO  --key=HBUWEY87CWBHJHG876WCG    ./src/COVID-19-ANALYSIS.py     2> build.txt    
              

pyinstaller --distpath=./dist/lin/  --workpath=./build/lin/  --noconfirm  --clean   COVID-19-ANALYSIS.spec

# --windowed 


cp ./README.* ./dist/lin/COVID-19-ANALYSIS/
cp -R ./data ./dist/lin/COVID-19-ANALYSIS/ 


read -p "Press [Enter] key..."


