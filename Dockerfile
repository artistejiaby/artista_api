FROM python:3.12-slim-buster

RUN mkdir -p /home/app

ENV HOME=/home/app
ENV APP_HOME=/home/app/backclone
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends netcat
COPY requirements.txt $APP_HOME
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY scripts/entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh

COPY . $APP_HOME

EXPOSE 8001

ENTRYPOINT ["/entrypoint.sh"]
