FROM python:3.11-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Set current directory as ENV
ENV PATH=/app:$PATH

# Needed for tzdata
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/Los_Angeles

# default workdir
WORKDIR /app

# install python dependencies
COPY requirements.txt ./requirements.txt
RUN pip install requirements.txt

# copy app
COPY app.py ./app.py

# command
CMD ["waitress-serve", "--host", "0.0.0.0", "--port", "8001", "app:app"]