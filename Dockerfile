FROM eeacms/pylint:latest as builder
WORKDIR /code
COPY pylint.cfg /etc/pylint.cfg
COPY *.py ./
COPY requirements.txt ./
# Run pylint with errors-only and exit-zero options
RUN ["/docker-entrypoint.sh", "pylint", "--errors-only", "--exit-zero"]


FROM python:3.10.0-alpine as serve
WORKDIR /usr/src
COPY --from=builder /code/*.py ./
COPY --from=builder /code/requirements.txt ./
RUN pip install -r requirements.txt
CMD ["python", "main.py"]

