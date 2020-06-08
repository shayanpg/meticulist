import unittest
from src.database import *


class SQLiteTestCases(unittest.TestCase):

    def test_connect(self):
        self.assertNotEqual(None, connect(':memory:'))

    def test_read_write(self):
        conn = connect(':memory:')
        create = """
        CREATE TABLE IF NOT EXISTS testing (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT, 
        description TEXT, 
        priority INTEGER
        )
        """
        execute_query(conn, create)

        data = """
                INSERT INTO
                    testing (name, description, priority)
                VALUES
                    ('eat', 'like with food', 1),
                    ('dont eat', 'maybe go outside', 3);
                """
        execute_query(conn, data)

        select = """
        SELECT name FROM testing WHERE id=1
        """
        a = execute_read_query(conn, select)[0][0]

        self.assertEqual(a, 'eat')


if __name__ == '__main__':
    unittest.main()
