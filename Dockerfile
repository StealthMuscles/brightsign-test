FROM python:3.10-slim

ENV API_KEY=df8193be439058914e2da642c5ae3a67

RUN pip3 install pipenv

RUN useradd --create-home --shell /bin/bash locateip_user
WORKDIR /home/locateip_user
USER locateip_user

COPY . .
RUN pipenv install
ENTRYPOINT ["pipenv", "run", "python3", "locateip.py"]
