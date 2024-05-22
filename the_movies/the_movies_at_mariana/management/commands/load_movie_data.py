import json
import logging
import traceback
from django.conf import settings
from django.db import transaction
from django.core.management.base import BaseCommand

from ...models import Movie, Genre, Rating, MovieGenre, MovieRating


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Load movie JSON data into database"

    def handle(self, *args, **options):

        try:
            with open(f'{settings.BASE_DIR}/data/index.json') as f:
                
                data_list = json.load(f)
                
                for data in data_list:
                    logger.info("Loaded JSON file")

                    date = data.get('date')
                    movies = data.get('movies')
                    with transaction.atomic():
                        for movie in movies:
                            
                            genre_ids = []
                            genres = movie.get('genre')
                            for genre in genres:
                                genre, _ = Genre.objects.get_or_create(name=genre)
                                genre_ids.append(genre.id)

                            rating_ids = []
                            ratings = movie.get('Ratings')
                            for rating in ratings:
                                rating, _ = Rating.objects.get_or_create(source=rating.get('source'), value=rating.get('value'))
                                rating_ids.append(rating.id)

                            movie_record = Movie.objects.create(title=movie.get('title'), poster=movie.get('poster'), year_released=movie.get('year'), runtime=movie.get('runtime'), date=date)

                            movie_genre_mappings = []
                            for genre_id in genre_ids:
                                movie_genre_mappings.append(MovieGenre(movie_id=movie_record.id, genre_id=genre_id))
                            
                            movie_rating_mappings = []
                            for rating_id in rating_ids:
                                movie_rating_mappings.append(MovieRating(movie_id=movie_record.id, rating_id=rating_id))

                            logger.info(f"Creating Movie Genre and Rating mappings for movie id {movie_record.id}")

                            MovieGenre.objects.bulk_create(movie_genre_mappings)
                            MovieRating.objects.bulk_create(movie_rating_mappings)
                    
        except Exception:
            logger.error(traceback.format_exc())

