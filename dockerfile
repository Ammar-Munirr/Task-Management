FROM python:3.11

ENV PYTHONUNBUFFERED=1

RUN mkdir/app

WORKDIR /app

COPY requirement.txt /code/

RUN pip install --user -r requirement.txt

COPY . /code/

CMD ['python','manage.py','runserver']