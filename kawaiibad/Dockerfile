FROM python
RUN apt-get update
RUN python3 -m pip install -U discord.py
RUN python3 -m pip install nekos.py

WORKDIR /usr/src/app
COPY src .

ENTRYPOINT exec python3 /usr/src/app/kawaiibad.py
