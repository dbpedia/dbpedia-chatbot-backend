FROM python:3.7

WORKDIR /app
COPY . /app
COPY ../config.env /app/.env

RUN pip install virtualenv 
RUN virtualenv venv && . venv/bin/activate
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip3 install python-dotenv

EXPOSE 8080

CMD ["uvicorn", "main:app", "--workers", "1", "--host=0.0.0.0", "--port=8080"]