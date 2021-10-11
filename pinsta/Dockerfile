FROM python:3.7.10

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $HOME
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/django_statics
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME

# prevent docker to copy pyc file
ENV PYTHONDONTWRITEBYTECODE 1
# enable realtime log
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y libpq-dev postgresql postgresql-contrib

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./entrypoint.sh .

COPY . .

ENTRYPOINT ["sh", "/home/app/web/entrypoint.sh"]

