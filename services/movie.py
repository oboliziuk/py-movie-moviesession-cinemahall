from django.db.models import QuerySet
from db.models import Movie


def get_movies(
        genres_ids: list[int],
        actors_ids: list[int]
) -> QuerySet[Movie]:

    queryset = Movie.objects.all()

    if genres_ids and actors_ids:
        queryset = queryset.filter(genre__in=genres_ids, actor__in=actors_ids)

    if genres_ids:
        queryset = queryset.filter(genre__in=genres_ids)

    if actors_ids:
        queryset = queryset.filter(actor__in=actors_ids)

    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    if movie_id:
        return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None) -> Movie:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        new_movie.genres.set(genres_ids)

    if actors_ids:
        new_movie.actors.set(actors_ids)

    return new_movie
