FROM eeacms/pylint:latest as builder
WORKDIR /code
COPY pylint.cfg /etc/pylint.cfg
COPY *.py ./
COPY requirements.txt ./
RUN ["/docker-entrypoint.sh", "pylint"]

FROM newtmitch/sonar-scanner as sonarqube
WORKDIR /usr/src
COPY ./sonar-runner.properties /usr/lib/sonar-scanner/conf/sonar-scanner.properties
COPY --from=builder /code/*.py ./
RUN sonar-scanner -Dsonar.projectBaseDir=/usr/src

FROM python:3.10.0-alpine as serve
WORKDIR /usr/src
COPY --from=builder /code/*.py ./
COPY --from=builder /code/requirements.txt ./
RUN pip install -r requirements.txt
CMD ["python", "main.py"]

