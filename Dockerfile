FROM debian

RUN apt-get update
# sqlite3 is part of python3
RUN apt-get install -y python3-flask

RUN useradd -m user
USER user
WORKDIR /home/user
RUN mkdir data
WORKDIR data

COPY --chown=user app.py app.py
COPY --chown=user db.py db.py
COPY --chown=user static static
COPY --chown=user templates templates

CMD ["flask", "run", "-h", "::", "-p", "8080"]
