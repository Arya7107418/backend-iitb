<<<<<<< HEAD
FROM python:3.9
WORKDIR /app
COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/.
RUN python manage.py collectstatic --noinput
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "course_api.wsgi:application"]
=======

FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
>>>>>>> bbd71357a0c4df9983a720848aad8e695a1594c4
