FROM python:3.12

ENV PYTHONUNBUFFERED 1

# Upgrade base packages.
RUN apt update \
    && apt upgrade -y \
    && pip install --upgrade pip

# Setup application.
# - packages
RUN apt install -y postgresql-client \
    && apt clean
# - python
RUN mkdir /code
COPY ./back/.env /code/.env
#COPY ./back/requirements.lock /code/requirements.lock
COPY ./back/requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip install -r requirements.txt \
    && rm -rf ~/.cache/pip
# - startup
# CMD python
