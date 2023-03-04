FROM python:3.10

SHELL ["/bin/bash", "-c"]

RUN pip install --upgrade pip

RUN useradd -ms /bin/bash app

copy --chown=app:app . .

RUN pip install -r requirements.txt

WORKDIR "/dZENcode_test"
RUN python manage.py makemigrations
RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
