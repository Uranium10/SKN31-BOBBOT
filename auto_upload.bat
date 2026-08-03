git add .
set comment=
cls
set /p comment=Enter Comment:
if "%comment%" == "" comment="auto uploaded"
git commit -m "%comment%"
git pull --rebase
git push origin main