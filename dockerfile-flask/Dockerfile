FROM python
RUN rm /etc/apt/sources.list
COPY sources.list /etc/apt/sources.list
ADD . /docker
RUN apt-get update
RUN apt-get install vim -y
RUN pip install -r /docker/requirements.txt
EXPOSE 5000