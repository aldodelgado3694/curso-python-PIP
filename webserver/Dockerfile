FROM python:3.12.3

WORKDIR /webserver
COPY requirements.txt webserver/requirements.txt

RUN pip install --no-cache-dir --upgrade -r webserver/requirements.txt

COPY ./ webserver/

CMD ["uvicorn", "--app-dir", "/webserver", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload", "--reload-dir", "/webserver"]
