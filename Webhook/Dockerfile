FROM python:3.9

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Bundle app source
COPY . .

EXPOSE 5000

CMD ["uvicorn", "main:app", "--workers", "1", "--host=0.0.0.0", "--port=5000"]	