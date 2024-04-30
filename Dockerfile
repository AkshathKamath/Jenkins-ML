FROM python:3.10-slim-buster

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
#copy to code directory
COPY . /code 

#set permissions

RUN chmod +x /code/Source

RUN pip install --no-cache-dir --upgrade -r code/Source/requirements.txt

EXPOSE 8005

WORKDIR /code/Source

ENV PYTHONPATH "${PYTHONPATH}:/code/Source"

CMD pip install -e .