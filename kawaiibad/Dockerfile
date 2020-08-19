FROM python
RUN apt-get update
RUN python3  -m pip install -U discord.py

WORKDIR /usr/src/app
COPY src .

ENTRYPOINT exec python3 /usr/src/app/kawaiibad.py
