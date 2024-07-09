Welcome to Append Solution.
For run this project some requirements.

install python -: sudo apt install python
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
nohup python manage.py runserver "portname" &
portname is optional. it's required for server.
