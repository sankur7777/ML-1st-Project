From python:3.9
copy . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $port
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
