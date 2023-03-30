FROM pylint:latest as builder
WORKDIR /code
COPY pylint.cfg /etc/pylint.cfg
COPY *.py ./
RUN ["/docker-entrypoint.sh", "pylint"]



#FROM python:3.10.0-alpine
#COPY requirements.txt .
#COPY main.py .
#RUN pip install -r requirements.txt
#CMD ["python", "main.py"]

