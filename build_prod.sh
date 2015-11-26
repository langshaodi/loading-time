mkdir -p run
git pull origin master
source ~/.bashrc
workon loading-time
npm install
bower install
pip install -r requirements.txt
grunt build
./app/manage.py collectstatic --noinput
sleep 1
./app/manage.py migrate
sudo systemctl restart loading-time
