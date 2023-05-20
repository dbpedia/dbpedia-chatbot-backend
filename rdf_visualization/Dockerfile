FROM python:3.7

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Bundle app source
COPY . .

EXPOSE 3001

CMD [ "python", "app.py" ]
