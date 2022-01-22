@echo off
cd ..
Automated_testing.py -f users.json > Report.txt
cls
echo Output can be found at ../report.txt

pause