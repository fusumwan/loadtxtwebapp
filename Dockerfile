FROM python:3.13.7

ENV PYTHONUNBUFFERED True

# set the working directory
WORKDIR /usr/src/app

# Install system dependencies needed for building Python packages
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    python3-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    libopenblas-dev \
    liblapack-dev \
    && apt-get clean

# Upgrade pip and install Cython via pip
RUN pip install --upgrade pip && \
    pip install --no-cache-dir cython

# install dependencies
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy src code
COPY ./accountslogin ./accountslogin

# SSL certificates not needed for Cloud Run (handled by Google's load balancer)

EXPOSE 8080

# start the server
# CMD ["uvicorn", "accountslogin.main:app", "--host", "0.0.0.0", "--port", "8080", "--proxy-headers", "--ssl-keyfile", "./accountslogin/learnwiseaiwebapp_ssl_key.pem", "--ssl-certfile", "./accountslogin/learnwiseaiwebapp_ssl_cert.pem"]
# CMD ["uvicorn", "accountslogin.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload", "--ssl-keyfile", "./accountslogin/learnwiseaiwebapp_ssl_key.pem", "--ssl-certfile", "./accountslogin/learnwiseaiwebapp_ssl_cert.pem"]
# CMD ["uvicorn", "accountslogin.main:app", "--host", "0.0.0.0", "--port", "8080", "--proxy-headers", "--ssl-keyfile", "learnwiseaiwebapp_ssl_key.pem", "--ssl-certfile", "learnwiseaiwebapp_ssl_cert.pem"]
# CMD ["uvicorn", "accountslogin.main:app", "--host", "0.0.0.0", "--port", "8080", "--proxy-headers", "--ssl-keyfile", "./learnwiseaiwebapp_ssl_key.pem", "--ssl-certfile", "./learnwiseaiwebapp_ssl_cert.pem"]
CMD ["uvicorn", "accountslogin.main:app", "--host", "0.0.0.0", "--port", "8080", "--proxy-headers"]
