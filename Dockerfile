FROM python:3

ADD . .

RUN pip install -r requirements.txt

RUN export FLASK_APP=wsgi.py;export FLASK_DEBUG=1;export APP_CONFIG_FILE=config.py

RUN python3 wsgi.py