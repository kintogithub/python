FROM python:3.6.4

RUN mkdir -p app

WORKDIR /app

COPY . /app


RUN pip install -r requirements.txt


ENV FLASK_APP=hello.py

EXPOSE 80


ENTRYPOINT ["flask","run","--port", "80", "--host", "0.0.0.0"]
