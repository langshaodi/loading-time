git pull origin master
source ~/.bashrc
workon loading-time
npm install
bower install
pip install -r requirements.txt
gulp build
./app/manage.py migrate
systemctl restart loading-time