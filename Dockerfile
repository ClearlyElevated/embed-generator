FROM python:3.6-slim-buster

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apt-get update
RUN apt-get install git
RUN pip install --no-cache-dir -r requirements.txt

COPY embed_generator/ .

CMD [ "python", "-u", "bot.py" ]
