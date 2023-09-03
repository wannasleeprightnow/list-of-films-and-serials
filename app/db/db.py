import sqlite3

from config import SQLITE_DB_FILE


def _connect_db() -> sqlite3.Connection:
    if not getattr(_connect_db, "db", None):
        db = sqlite3.connect(SQLITE_DB_FILE)
        _connect_db.db = db

    return _connect_db.db


def close_db() -> None:
    _connect_db().close()


def execute(sql: str, params: tuple) -> None:
    con = _connect_db()
    con.execute(sql, params)
    con.commit()


def _get_cursor(sql: str, params: tuple) -> sqlite3.Cursor:
    con = _connect_db()
    cursor = con.execute(sql, params)
    con.row_factory = sqlite3.Row
    return cursor


def fetch_all(sql: str, params: tuple) -> list[dict]:
    cursor = _get_cursor(sql, params)
    rows = cursor.fetchall()
    results = []
    for row_ in rows:
        results.append(_get_result_with_column_names(cursor, row_))
    cursor.close()
    return results


def _get_result_with_column_names(cursor: sqlite3.Cursor, row: sqlite3.Row) -> dict:
    column_names = [d[0] for d in cursor.description]
    resulting_row = {}
    for index, column_name in enumerate(column_names):
        resulting_row[column_name] = row[index]
    return resulting_row
