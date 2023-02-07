FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN   pip install --upgrade pip

COPY ./requirements.txt ./

RUN pip install -r requirements.txt && AlergiasApp//manage.py migrate

COPY ./ ./

CMD   [ "python", "./AlergiasApp/manage.py", "runserver", "0.0.0.0:8000" ]