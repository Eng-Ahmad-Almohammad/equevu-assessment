# Equevu assessment

This is a simple Django API for a tiny HR system, where job applicants can register
as potential candidates and upload their resumes, and HR managers can log in and see the
list of candidates and download their resumes.

## Running the app

### Install PostgreSQL

Create the file repository configuration:

```bash
sudo sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
```

Import the repository signing key:

```bash
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
```

Update the package lists:

```bash
sudo apt-get update
```

Install the latest version of PostgreSQL.
If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':

```bash
sudo apt-get -y install postgresql
```

Run the postgreql service

```bash
sudo service postgresql start
```

Connect to the Postgresql interface and create a user

```bash
sudo -u postgres psql
```

```sql
CREATE USER 'your_user' WITH PASSWORD 'your_password';
CREATE DATABASE  'your_user';
```

You can give your user the SUPERUSER privileges

```sql
ALTER USER your_user WITH SUPERUSER;
```

Now you connect to the postgresql interface using your user

```bash
psql
```

### Run Django app:

First of all create .env file on the top level of the directories tree and fill it as the .env.template

Collect the static files since we are using whitenose:

```bash
python manage.py collectstatic
```

Migrate the database

```bash
python manage.py migrate
```

Run the server

```bash
python manage.py runserver
```

## Run using Docker

Download Docker from the following [link](https://www.docker.com/products/docker-desktop/) and docker-compose using the following command

```bash
sudo pip install docker-compose
```

Create .env file on the top level of the directories tree and fill it as the .env.template but use "postgres" as db name and user name and password since this is the default configuration for postgres image, make sure to use "db" as value of db host and "5432" as db port.

After creating the .env file all what you need to do is to run:
```bash
docker-compose up --build
```
