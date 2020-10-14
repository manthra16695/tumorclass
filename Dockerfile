FROM python:3.7

EXPOSE 8000
# RUN apt-get update -y

# RUN apt-get install -y python3-pip python3-dev build-essential

WORKDIR /app

# CMD ["python", "/app/src/__main__.py"]

ADD . /app

COPY ./requirements.txt /app/requirements.txt

# ENTRYPOINT ["python3"]

RUN pip3 install -r requirements.txt

RUN python manage.py makemigrations

RUN python manage.py migrate


COPY . /app

CMD [ "python", "tumorclass_web/manage.py", "runserver", "0.0.0.0:8000","-e","production" ]

