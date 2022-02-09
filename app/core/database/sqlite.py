# this file will contain functions interacting with the database
from pathlib import Path
import sqlite3


class SQLite:
    """
    Context handler to do away with boiler plate code required when using the
    `sqlite3.Connection` context handler.

    Connects to the sqlite database at the given path, generates and returns
    the cursor to be used for database operations by the rest of the app.
    """

    def __init__(self, path: Path):
        self.path = path

    def __enter__(self):
        self.connection = sqlite3.Connection(self.path)
        self.cursor = self.connection.cursor()

        # we won't be able to use any of the context manager's methods in the
        #  `with` block if we do not return the class instance
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # exc_type, exc_val and exc_tb refer to exception type, value and
        # traceback, respectively; __ext__ receives a tuple of 3 None types
        # if no exception is encountered
        self.connection.close()
