# Python version
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Define a build argument with a default value
ARG DJANGO_ENV=production

# Set the DJANGO_ENV environment variable with the build argument value
ENV DJANGO_ENV=$DJANGO_ENV

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements/base.txt /code/
RUN pip install -r base.txt
EXPOSE 8000

# Copy project
COPY . /code/

RUN chmod +x /code/entrypoint.sh
