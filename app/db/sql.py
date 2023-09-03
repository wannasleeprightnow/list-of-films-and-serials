select_movie = """SELECT * FROM movie
WHERE user_id = ? AND title = ?"""

delete_movie = """DELETE FROM movie
WHERE user_id = ? AND title = ?"""

insert_movie = """INSERT INTO movie(user_id, title, rating, count_watched_series, movie_type, condition)
VALUES(?, ?, ?, ?, ?, ?)"""

select_all_user_movies = """SELECT title, rating, count_watched_series, movie_type, condition FROM movie
WHERE user_id=?"""

select_user_data = """SELECT * FROM user 
WHERE login=?"""

insert_user_data = """INSERT INTO user(login, password) VALUES(?, ?)"""
