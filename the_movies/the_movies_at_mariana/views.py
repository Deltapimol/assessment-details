import traceback
import logging
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR
from .models import Movie, MovieGenre
from .serializers import MovieSerializer


logger = logging.getLogger("django")


@api_view(['GET'])
def fetch_movies(request):
    """
        Fetch movies. Can be filtered by genre or searched by movie title.
    """
    try:
        genre = request.query_params.get('genre')
        search = request.query_params.get('search')

        filter_query = Q()

        # Filter by genre. Separate by ',' for multiple genres
        if genre:
            genres = [ genre.strip().capitalize() for genre in genre.split(',') ]
            filter_query.add(Q(genre__name__in=genres), Q.AND)
        
        # Search by movie title
        if search:
            filter_query.add(Q(movie__title__startswith=search), Q.AND)
    
        movie_genres = MovieGenre.objects.filter(filter_query).select_related('movie', 'genre')
        movies = []
        for movie_genre in movie_genres:
            movies.append(movie_genre.movie)

        serialized_data = MovieSerializer(movies, many=True, context={"genre": True}).data
            
        return Response({"message": "Movies fetched successfully!", "data": serialized_data}, status=HTTP_200_OK)
    except Exception:
        logger.error(traceback.format_exc())
        return Response({"message": "Something went wrong"}, status=HTTP_500_INTERNAL_SERVER_ERROR)
