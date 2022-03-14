FROM python:3.9.10-buster

WORKDIR /Model-API/app
ADD . /Model-API/app

ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV TZ=Asia/Seoul

RUN pip install -r requirements.txt

ENTRYPOINT ["flask"]

CMD ["run", "--host", "0.0.0.0"]