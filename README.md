# dataset_handler

dataset_handler is an API service for getting information from a dataset.

## Features

- Get all columns;
- Get only requested columns;
- Filter data by one or several columns: date (from / to), shops, countries;
- Group data by one or more columns: dates, shops, countries;
- Order data by any columns;
- Import CSV files into database;

## Tech

dataset_handler uses a number of open source projects to work properly:

- [Django 2.2.19] - a high-level Python Web framework.
- [Python 3.9]

And of course dataset_handler itself is open source with a [private repository][Nadin007/dataset_handler]
 on GitHub.

## Installation

Clone and go to the repository using the terminal:

```sh
git clone https://github.com/Nadin007/dataset_handler.git
```

```sh
cd dataset_handler
```

Running dataset_handler in dev mode:
- Create and activate a virtual environment

```sh
python3 -m venv env

```
```sh
source venv/bin/activate

```
- Install dependencies from requirements.txt file

```sh
pip install -r requirements.txt
```
- In the folder with the manage.py file, run the command:

```sh
cd dataset_handler
```

```sh
python3 manage.py runserver
````

## Import CSV files into database

Use load_data applications to import data from a CSV file into a database.
When you invoke func. you should pass the path to the csv file:

```sh
python3 manage.py load_data './data/dataset.csv'
````

## License

MIT


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Django 2.2.19]: <https://www.djangoproject.com/download/>
   [Python 3.7]: <https://www.python.org/downloads/release/python-390/>
   [Nadin007/dataset_handler]: <https://github.com/Nadin007/dataset_handler.git>
   



Author
Tumareva Nadia
