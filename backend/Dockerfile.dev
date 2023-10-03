FROM python:3.9

# python dependencies
COPY ./requirements.txt /
RUN pip install -r ./requirements.txt
COPY ./scripts/entrypoint.sh ./scripts/start.sh ./scripts/gunicorn.sh /
# upload scripts

# Fix windows docker bug, convert CRLF to LF
RUN sed -i 's/\r$//g' /start.sh && chmod +x /start.sh && sed -i 's/\r$//g' /entrypoint.sh && chmod +x /entrypoint.sh &&\
    sed -i 's/\r$//g' /gunicorn.sh && chmod +x /gunicorn.sh

WORKDIR /backend
