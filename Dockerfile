FROM eeacms/pylint:latest as builder
WORKDIR /code
COPY pylint.cfg /etc/pylint.cfg
COPY *.py ./
COPY requirements.txt ./
RUN set -eux; \
    /docker-entrypoint.sh pylint && \
    exit 0


FROM python:3.10.0-alpine as serve
WORKDIR /usr/src
COPY --from=builder /code/*.py ./
COPY --from=builder /code/requirements.txt ./
RUN pip install -r requirements.txt
CMD ["python", "main.py"]

