FROM python:3
RUN apt-get update -y && apt-get install -y build-essential
WORKDIR /home/app/parser
COPY ./ /home/app/parser
RUN pip install -r requirements.txt