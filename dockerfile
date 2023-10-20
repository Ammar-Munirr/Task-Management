FROM python:3.11

ENV PYTHONUNBUFFERED=1

RUN mkdir /app

WORKDIR /app

COPY requirement.txt .

RUN pip install --user -r requirement.txt

COPY . .

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
