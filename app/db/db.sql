CREATE TABLE user(
    id INTEGER PRIMARY KEY,
    login VARCHAR(32),
    password VARCHAR(32)
);

CREATE TABLE movie(
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    title TEXT,
    rating REAL,
    count_watched_series INTEGER,
    movie_type VARCHAR(6),
    condition VARCHAR(9),
    FOREIGN KEY(user_id) REFERENCES user(id)
);