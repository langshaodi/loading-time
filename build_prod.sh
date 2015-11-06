git pull origin master
source ~/.bashrc
workon loading-time
npm install
bower install
pip install -r requirements.txt
grunt build
./app/manage.py migrate
sudo systemctl restart loading-time
