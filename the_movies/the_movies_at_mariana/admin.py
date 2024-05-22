from django.contrib import admin
from .models import Movie, Genre, Rating, MovieGenre, MovieRating


class MovieAdmin(admin.ModelAdmin):

    list_display = ["id", "title", "year_released"]


class RatingAdmin(admin.ModelAdmin):

    list_display = ["id", "source"]


class GenreAdmin(admin.ModelAdmin):

    list_display = ["id", "name"]


class MovieGenreAdmin(admin.ModelAdmin):

    list_display = ["id", "movie", "genre"]

    def movie(self, obj):

        movie_title = obj.movie.title
        return movie_title
    
    def genre(self, obj):
        
        genre = obj.genre.name
        return genre


class MovieRatingAdmin(admin.ModelAdmin):

    list_display = ["id", "movie", "source"]

    def movie(self, obj):

        movie_title = obj.movie.title
        return movie_title
    
    def source(self, obj):
        
        source = obj.rating.source
        return source


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(MovieGenre, MovieGenreAdmin)
admin.site.register(MovieRating, MovieRatingAdmin)
