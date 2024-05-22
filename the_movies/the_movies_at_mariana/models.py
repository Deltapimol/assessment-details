from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False)
    poster = models.CharField(max_length=256)
    year_released = models.CharField(max_length=4)
    runtime = models.CharField(max_length=32)
    date = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=64, unique=True, blank=False, null=False)

    def __str__(self) -> str:
        return self.name


class Rating(models.Model):
    source = models.CharField(max_length=64, blank=False, null=False)
    value = models.CharField(max_length=64, blank=False, null=False)

    def __str__(self) -> str:
        return self.source


class MovieGenre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.movie.title} | {self.genre.name}"


class MovieRating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.movie.title} | {self.rating.source}"


# Metacritic Rating