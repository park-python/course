FROM alpine:3.4
MAINTAINER Python course at Bauman University

RUN apk add --update python3 py-pip

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY app.py /app

ENTRYPOINT ["python"]
CMD ["app.py"]
