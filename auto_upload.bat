git add .
set comment="auto uploaded"
git commit -m "%comment%"
git pull --rebase
git push origin main