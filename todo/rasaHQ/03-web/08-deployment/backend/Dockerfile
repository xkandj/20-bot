FROM rasa/rasa:latest-full

WORKDIR /app

COPY . /app
COPY ./data /app/data
COPY ./models /app/models

VOLUME /app
VOLUME /app/data
VOLUME /app/models

CMD ["run", "-m", "/app/models", "--enable-api", "--cors", "*"]
