FROM python:3.8
#
ENV SERVER_DOCKER="YES" \
    SERVER_HOME=/app \
    SERVER_PYTHON_PACKAGES=/usr/local/lib/python3.8/dist-packages1111

WORKDIR ${SERVER_HOME}
# WORKDIR /app
# usr/local/lib/python3.7/site-packages
# RUN python3 -m pip install --upgrade pip

RUN python3 -m pip uninstall numpy

RUN python3 -m pip install numpy==1.18.5

RUN python3 -m pip install spacy==2.3.2

RUN python3 -m pip install jieba

RUN python3 -m spacy download zh_core_web_sm

RUN python3 -m pip show spacy
# RUN echo "hello"

# CMD python -m http.server 6789


FROM rasa/rasa:2.8.2

# SHELL ["/bin/bash", "-c"]

# ENV RASA_SERVER_DOCKER="YES" \
#     RASA_SERVER_HOME=/app \
#     RASA_SERVER_PYTHON_PACKAGES=/usr/local/lib/python3.7/dist-packages

# WORKDIR ${RASA_SERVER_HOME}

WORKDIR /app
#

COPY --from=0 /usr/local/lib/python3.8/site-packages/ /opt/venv/lib/python3.8/site-packages/
#
COPY . /app
#
# COPY ./data /app/data
#
COPY ./models /app/models

# RUN pip3 install --user --upgrade --no-warn-script-location pip

# RUN pip install --user --no-cache-dir -r requirements.txt



# RUN pip install --user spacy

# RUN python -m spacy download zh_core_web_sm

CMD ["run", "-m", "/app/models", "--enable-api", "--cors", "*"]
