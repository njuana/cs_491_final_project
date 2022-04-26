
   
FROM ubuntu:latest

RUN apt update
RUN apt install python3 -y

WORKDIR /usr/src/app

COPY . .

CMD [ "python3", "./test_test_project.py"]
