FROM python:3.9
WORKDIR /app
RUN apt-get update -y && apt-get upgrade -y
COPY ./requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN apt-get update -y && apt-get upgrade -y
COPY .. ./src
CMD gunicorn -w 3 --chdir ./src MySiteOnePage.wsgi --bind 0.0.0.0:8000
