FROM python:3.7

WORKDIR /app
COPY . /app

RUN pip install virtualenv 
RUN virtualenv venv && . venv/bin/activate
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "main:app", "--workers", "1", "--host=0.0.0.0", "--port=8080"]	