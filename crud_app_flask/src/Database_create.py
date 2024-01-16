import pymysql

# Requires a Mysql database
# For example with:
# docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -e MYSQL_DATABASE=db -p 8001:3306 -d mysql:latest

# MySQL connection parameters
username = "root"
password = "my-secret-pw"
hostname = "localhost"
port = 8001
database = "db"

# Create a connection to MySQL using pymysql
connection = pymysql.connect(
    host=hostname,
    user=username,
    password=password,
    port=port,
    database=database,
    cursorclass=pymysql.cursors.DictCursor  # Use DictCursor for fetching results as dictionaries
)


try:
    # Create a cursor object to execute SQL queries
    with connection.cursor() as cursor:

        # Example query: Create a table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS songs (
            song_id INT PRIMARY KEY AUTO_INCREMENT,
            song_name VARCHAR(255),
            album_id INT,
            album_name VARCHAR(255),
            artist_id INT,
            artist_name VARCHAR(255)
        )
        """
        cursor.execute(create_table_query)

        # Example query: Insert a new song
        insert_songs_query = """
        INSERT INTO songs (song_name, album_id, album_name, artist_id, artist_name)
        VALUES ("cancion_1", 1, "album_1", 1, "artista_1"),
               ("cancion_2", 1, "album_1", 1, "artista_1"),
               ("cancion_3", 1, "album_1", 1, "artista_1"),
               ("cancion_4", 1, "album_1", 1, "artista_1"),
               ("cancion_5", 2, "album_2", 1, "artista_1"),
               ("cancion_6", 2, "album_2", 1, "artista_1"),
               ("cancion_7", 3, "album_3", 2, "artista_2"),
               ("cancion_8", 3, "album_3", 2, "artista_2")
        """
        cursor.execute(insert_songs_query)

        # Select all songs
        select_all_songs_query = "SELECT * FROM songs"
        cursor.execute(select_all_songs_query)

        # Fetch all rows
        all_songs = cursor.fetchall()
        for song in all_songs:
            print(song)

    # Commit the changes to the database
    connection.commit()

finally:
    # Close the connection
    connection.close()