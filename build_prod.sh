SCRIPT = "
cd loading-time;
npm install;
bower install;
pip install -r requirements.txt;
./app/manage.py migrate
echo "Done."
"
ssh web@104.236.21.37 "$(SCRIPT)"
