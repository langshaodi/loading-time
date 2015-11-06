cd loading-times
pwd
git pull origin master
source ~/.bashrc
workon loading-time
npm install
bower install
pip install -r requirements.txt
./app/manage.py migrate
echo "done!"