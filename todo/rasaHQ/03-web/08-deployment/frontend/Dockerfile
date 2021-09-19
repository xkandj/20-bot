FROM python:3.7

ENV PORT=3000

WORKDIR /app/frontend

COPY . /app/frontend

VOLUME /app/frontend

EXPOSE $PORT

CMD python -m http.server $PORT

#ENTRYPOINT ["python"]
#CMD ["run_http_server.py"]