FROM ubuntu
WORKDIR /

RUN apt-get update
RUN apt-get install -y python3-pip

COPY . .
RUN pip3 install -r requirements.txt

EXPOSE 5000
CMD ["python3","controller.py"]