from entities.player import Player
from database_connection import get_database_connection


class PlayerRepository:
    """The class is responsible for the players database operations.

    Attributes:
        connection: Database connection object
    """

    def __init__(self, connection):
        """Class constructor.

        Args:
            connection: Database connection object
        """

        self._connection = connection

    def create(self, name: str):
        """Adds a new player to the SQLite-database. New player has a name and 0 wins. 

        Args:
            name (str): Players name.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO Players (name,wins) VALUES (?,?)", [name, 0])
        self._connection.commit()

    def add_win(self, name: str):
        """When a player wins the game, its wins will be updated by +1. 

        Args:
            name (str): Players name.
        """

        cursor = self._connection.cursor()
        cursor.execute("UPDATE Players SET wins=wins+1 WHERE name=?", [name])
        self._connection.commit()

    def get_all(self) -> list:
        """Getting all the players from the SQLite-database.

        Returns:
            list: All the players as Player-objects. 
        """

        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Players")
        rows = cursor.fetchall()

        return [Player(row["name"], row["wins"]) for row in rows]


player_repository = PlayerRepository(get_database_connection())
