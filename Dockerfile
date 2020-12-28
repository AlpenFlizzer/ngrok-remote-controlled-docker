FROM ubuntu:20.04

RUN apt update && apt install -y python3.8 python3-pip wget unzip curl

RUN pip3 install pipenv

WORKDIR /usr/src/ngrok_api

COPY /core/ ./

Run ./ngrok_install.sh

RUN pipenv install --deploy --ignore-pipfile

Run rm ngrok_install.sh

EXPOSE 5000

CMD ["pipenv", "run", "python", "ngrok_control.py"]