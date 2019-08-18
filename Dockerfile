FROM python:3.6

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY embed_generator/ .

CMD [ "python", "-u", "bot.py" ]