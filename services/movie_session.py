from datetime import datetime
from django.db.models import QuerySet
from db.models import CinemaHall, Movie, MovieSession


def create_movie_session(
        movie_show_time: datetime,
        cinema_hall_id: int,
        movie_id: int
) -> MovieSession:
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie = Movie.objects.get(id=movie_id)

    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie)


def get_movies_sessions(
        session_date: str = None
) -> MovieSession | QuerySet[MovieSession]:
    if session_date:
        date_object = datetime.strptime(session_date, "%Y-%m-%d").date()
        return MovieSession.objects.filter(show_time__date=date_object)
    return MovieSession.objects.all()


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession | QuerySet[MovieSession]:
    if movie_session_id:
        return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    movie_session = MovieSession.objects.get(id=session_id)

    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id:
        movie_session.cinema_hall_id = CinemaHall.objects.get(
            id=cinema_hall_id)

    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()
