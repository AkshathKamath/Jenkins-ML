FROM python:3.10-slim-buster

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
#copy all current directory files to code directory of the container
COPY . /code 

#set permissions for Source folders inside container (As model will be created & stored)
RUN chmod +x /code/Source

RUN pip install --no-cache-dir --upgrade -r code/Source/requirements.txt

# Expose 8005 port of the container
EXPOSE 8005

# Set working directory as Source for subsequent commands
WORKDIR /code/Source

ENV PYTHONPATH "${PYTHONPATH}:/code/Source"

CMD pip install -e .