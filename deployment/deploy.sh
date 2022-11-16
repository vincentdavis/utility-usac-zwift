#!/bin/bash
git clone https://github.com/we-race-here/utility.git /home/jenkins/utility
cd /home/jenkins/utility
git checkout main
mkdir -p media

sudo cp -rf ../nginx.conf  /etc/nginx/nginx.conf
sudo cp -rf ../default.conf  /etc/nginx/sites-available/default
#cp ../.env /home/jenkins/zp-results/zp_result/
#cp ../ca-certificate.crt /home/jenkins/zp-results/
pip install uwsgi
#python manage.py collectstatic
python manage.py migrate

# Restart nginx
sudo /etc/init.d/nginx start || sudo /etc/init.d/nginx start

# Running Celery
#celery -A zp_result worker -l info &
#celery -A zp_result beat &

# Running Server
uwsgi --socket mysite.sock --module utility.wsgi --buffer-size=100000 --chmod-socket=666 --master --processes 4 --threads 2