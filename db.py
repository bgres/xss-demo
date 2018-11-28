import sqlite3


def connect_db():
    db = sqlite3.connect('database.db')
    db.cursor().execute('CREATE TABLE IF NOT EXISTS comments '
                        '(id INTEGER PRIMARY KEY, '
                        'comment TEXT)')
    db.commit()
    return db


def add_comment(comment):
    db = connect_db()
    db.cursor().execute('INSERT INTO comments (comment) '
                        'VALUES (?)', (comment,))
    db.commit()


def get_comments(search_query=None):
    db = connect_db()
    results = []
    get_all_query = 'SELECT comment FROM comments'
    for (comment,) in db.cursor().execute(get_all_query).fetchall():
        if search_query is None or search_query in comment:
            results.append(comment)
    return results
