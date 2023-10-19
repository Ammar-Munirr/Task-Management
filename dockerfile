FROM python:3.11

ENV PYTHONUNBUFFERED=1

RUN mkdir /app

WORKDIR /app

COPY requirement.txt .

RUN pip install --user -r requirement.txt

COPY . .

CMD ['python','manage.py','runserver']
