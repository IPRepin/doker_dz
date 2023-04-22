FROM python:3.8
WORKDIR dz_2/djangoMyTest
COPY . .

EXPOSE 8000


RUN pip install -r requirements.txt
RUN python manage.py migrate

CMD gunicorn djangoMyTest.wsgi -b 0.0.0.0:8000