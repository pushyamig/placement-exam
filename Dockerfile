FROM python:3.7

MAINTAINER Pushyami Gundala <pushyami@umich.edu>

RUN apt-get update && \
	apt-get install -y vim-tiny && \
	apt-get upgrade -y && \
	apt-get clean -y

# create place for app to run from
WORKDIR /app/

COPY . /app/

RUN pip install -r requirements.txt

CMD ["python", "main.py"]