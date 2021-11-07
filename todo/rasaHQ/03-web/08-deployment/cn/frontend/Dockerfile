FROM python:3.8

ENV PORT=3000

WORKDIR /app/frontend

COPY . /app/frontend

EXPOSE $PORT

CMD python -m http.server $PORT