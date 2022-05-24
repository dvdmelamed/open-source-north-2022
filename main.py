from typing import Optional
from fastapi import FastAPI
import sqlite3 as sqlite

app = FastAPI()


@app.get("/movies/count")
def get_movies():
    db = sqlite.connect("movies.db")
    res = db.execute("select count(*) from movies")
    count = res.fetchone()[0]
    return dict(result=count)


@app.get("/movies")
def search_movie(title: Optional[str] = None):
    db = sqlite.connect("movies.db")
    res = db.execute("select * from movies where title='{title}'".format(title=title))
    movies = [dict(id=record[0], title=record[1], release=record[2]) for record in res.fetchall()]
    return dict(result=movies)


@app.get("/movie/{movie_id}")
def get_movie(movie_id):
    db = sqlite.connect("movies.db")
    res = db.execute("select * from movies where id={movie_id}".format(movie_id=movie_id))
    records = res.fetchone()
    record = records if records is not None else None
    return dict(movie=record[0])


@app.get("/movie/{movie_id}/stars")
def get_movie_stars(movie_id):
    db = sqlite.connect("movies.db")
    res = db.execute("SELECT name from people JOIN stars ON people.id = stars.person_id JOIN movies "
                     "ON stars.movie_id = movies.id WHERE movies.id={movie_id}".format(movie_id=movie_id))
    stars = [record[0] for record in res.fetchall()]
    return dict(movie=int(movie_id), stars=stars)
