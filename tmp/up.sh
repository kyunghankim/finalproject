echo '>>> Git Pull'
git pull

echo '>>> Install Packages'
pip install -r requirements.txt

export DJANGO_SETTINGS_MODULE='finalproject.settings.prod'

echo '>>> Database Migrate'
python manage.py migrate

echo '>>> Collect Staticfiles'
python manage.py collectstatic --noinput

echo '>>> Restart Servers'
sudo systemctl restart nginx
sudo systemctl restart uwsgi