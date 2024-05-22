# assessment-details

## The App name is the_movies_at_mariana

### Initial Setup

##### Migration commands

```bash
python3 manage.py makemigrations

python3 manage.py migrate

```

##### Create Superuser

```bash
python3 manage.py createsuperuser
```

##### Runserver

```bash
python3 manage.py runserver

```

#### Load JSON data into database

The JSON data is present in data/index.json file. You have to load it in the database using the following base command.

```bash
python3 manage.py load_movie_data

```

### API details

#### The endpoint for fetching movies

http://localhost:8000/api/v1/movie

You can pass 'genre' query parameter separated by commas and you can search by movie title using 'search' query parameter.

e.g. Search for movies starting with 'in' for 'drama' and 'history' genres

http://localhost:8000/api/v1/movie/?search=in&genre=drama,history