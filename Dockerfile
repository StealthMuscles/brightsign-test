FROM python:3.10-slim

RUN pip3 install pipenv

RUN useradd --create-home --shell /bin/bash locateip_user
WORKDIR /home/locateip_user
USER locateip_user

COPY . .
RUN pipenv install
ENTRYPOINT ["pipenv", "run", "python3", "locateip.py"]
