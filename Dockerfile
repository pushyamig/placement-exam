FROM python:3.7

MAINTAINER Pushyami Gundala <pushyami@umich.edu>

RUN apt-get update && \
	apt-get install -y vim-tiny && \
	apt-get upgrade -y && \
	apt-get clean -y

# create place for app to run from
WORKDIR /app/

COPY . /app/

ENV API_UTILS_VERSION v1.3
RUN pip install git+https://github.com/tl-its-umich-edu/api-utils-python@${API_UTILS_VERSION}
RUN pip install -r requirements.txt

# Sets the local timezone of the docker image
ENV TZ=America/Detroit
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

CMD ["python", "main.py"]