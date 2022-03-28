FROM python:3.9.10-buster

ADD . /app
WORKDIR /app

RUN gzip -d ko_w2v_model.gz

ENV FLASK_APP=app
ENV FLASK_ENV=production
ENV TZ=Asia/Seoul

RUN pip install -r requirements.txt

CMD ["uwsgi", "uwsgi.ini"]