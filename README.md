# Installation
## Initial setup
Clone the repository:
```
git clone https://github.com/PavloShutz/my-second-blog.git
```
Change your current directory:
```
cd my-second-blog
```
Activate virtual environment:
```
python -m venv env
env\Scripts\activate
```
Install required libraries/tools:
```
pip install -r requirements.txt
```
## Configurations
In [settings.py](my_second_blog/settings.py), you should do the following:
1) Create `.env` file and add this variable:
   ```dotenv
    SECRET_KEY=""
    ```
2) In terminal:
   - Start django's shell:
   ```commandline
    python manage.py shell
    ```
   - Execute the following lines:
   ```python
   >>> from django.core.management.utils import get_random_secret_key
   >>> get_random_secret_key()
   some_random_secret_key
   ```
   - Paste the key and set `SECRET_KEY`.
## PostgreSQL
> ![IMPORTANT]
> You need to have PostgreSQL installed on your machine to proceed.
> Use https://neon.com/postgresql/tutorial, for example, to do basic setup.

> ![NOTE]
> We assume that the username is `postgres`. Replace it, if required, by that
> that you provided in the installation.

Follow the next steps to properly configure your database:
1) Create a database:\
    In terminal:
    ```commandline
    chcp 1251
    psql -U postgres
    ```
    In postgresql shell:
    ```postgresql
    CREATE DATABASE secondblogdb;
    ```
2) Create `.my_pgpass` file next to [manage.py](manage.py) file:
   ```
   hostname:port:database:username:password
   ```
3) Create `%APPDATA%\postgresql\.pg_service.conf` and paste the following there:
   ```
    [second_blog_service]
    host=localhost
    dbname=secondblogdb
    port=5432
    user=postgres
    ```
