
# ROUTEMOBILE-ASSIGNMENT



Before running the project, ensure you have the following installed:

- Python (>=3.6)
- Django
- RabbitMQ
- Celery
- SQLite (or any other supported database)

You can install Python dependencies using the provided `requirements.txt` file:

Before installing `requirements.txt` first create virtual env :

To create virtual environment :

    python -m venv myenv

Activate virtual environment :

    myenv/Scripts/activate

Now install `requirements.txt` :

    pip install -r requirements.txt

Once all requirements get installed, run django server.
Go to the folder containing `manage.py` and run following command :

    python manage.py runserver

it will run django server on `http://localhost/8000`

To API Endpoint postman collection is provided with name `routemobile.postman_collection.json`. Import it in postman test accordingly

If you face any issue make changes in env file `.env` and look for other settings in config file `config.json`. Change path accordingly.

How to run celery worker ?

go to folder `simple_worker` and run the following command :

    celery -A tasks  worker -l info -P eventlet -E

