from rest_framework import serializers
from .models import Movie, MovieGenre, MovieRating


class MovieSerializer(serializers.ModelSerializer):

    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)
            
        if kwargs.get("context", {}).get("genre"):
            self.fields['genre'] = serializers.SerializerMethodField()

    def get_genre(self, obj):
        genres = [ movie_genre.genre.name for movie_genre in MovieGenre.objects.filter(movie=obj).select_related('genre') ]
        return genres

    def to_representation(self, obj):
        representation = super().to_representation(obj)
        representation['metacritic_rating'] = ""
        
        movie_rating = MovieRating.objects.filter(rating__source='Metacritic')
        if movie_rating.exists():
            representation['metacritic_rating'] = movie_rating[0].rating.value
        return representation

    class Meta:
        model = Movie
        fields = '__all__'
