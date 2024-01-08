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

TABLE_NAME = "songs"
"""
def select_table(name):
     TABLE_NAME = name
"""

def add_song_to_db(args):
    try:
        with connection.cursor() as cursor:

            insert_song = f"""
            INSERT INTO {TABLE_NAME} (song_name, album_name, artist_name)
            VALUES (%s, %s, %s)
            """

            cursor.execute(insert_song, args)
    
            select_all_songs_query = "SELECT * FROM songs"
            cursor.execute(select_all_songs_query)

        
            all_songs = cursor.fetchall()
            for song in all_songs:
                print(song)
    
        connection.commit()

    finally:
            connection.close()


def search_song_by(kwargs):

    try:
        with connection.cursor() as cursor:

            search_song = f"SELECT * FROM {TABLE_NAME} WHERE"
            conditions = []
            values = []

            if kwargs["song"]:
                conditions.append("song_name = %s")
                values.append(kwargs["song"])
            if kwargs["album"]:
                conditions.append("album_name = %s")
                values.append(kwargs["album"])
            if kwargs["artist"]:
                conditions.append("artist_name = %s")
                values.append(kwargs["artist"])

            if conditions:
                search_song += " " + " AND ".join(conditions)

            cursor.execute(search_song, tuple(values))
        
            all_songs = cursor.fetchall()
            for song in all_songs:
                print(song)
    
        connection.commit()

    finally:
            connection.close()



def delete_song_by(kwargs):

    try:
        with connection.cursor() as cursor:

            delete_song = f"DELETE FROM {TABLE_NAME} WHERE"
            conditions = []
            values = []

            if kwargs["song"]:
                conditions.append("song_name = %s")
                values.append(kwargs["song"])
            if kwargs["album"]:
                conditions.append("album_name = %s")
                values.append(kwargs["album"])
            if kwargs["artist"]:
                conditions.append("artist_name = %s")
                values.append(kwargs["artist"])

            if conditions:
                delete_song += " " + " AND ".join(conditions)

            cursor.execute(delete_song, tuple(values))
        
            all_songs = cursor.fetchall()
            for song in all_songs:
                print(song)
    
        connection.commit()

    finally:
            connection.close()



def update_song_by(kwargs):

    try:
        with connection.cursor() as cursor:

            update_song = f"""UPDATE {TABLE_NAME}
                              SET"""
            conditions = []
            values = []

            if kwargs["set_song"]:
                conditions.append("song_name = %s")
                values.append(kwargs["set_song"])
            if kwargs["set_album"]:
                conditions.append("album_name = %s")
                values.append(kwargs["set_album"])
            if kwargs["set_artist"]:
                conditions.append("artist_name = %s")
                values.append(kwargs["set_artist"])

            if conditions:
                update_song += " " + " , ".join(conditions) 
            
            conditions = []

            if kwargs["song"]:
                conditions.append("song_name = %s")
                values.append(kwargs["song"])
            if kwargs["album"]:
                conditions.append("album_name = %s")
                values.append(kwargs["album"])
            if kwargs["artist"]:
                conditions.append("artist_name = %s")
                values.append(kwargs["artist"])
            
            if conditions:
                update_song += "WHERE" + " " + " AND ".join(conditions)    

            cursor.execute(update_song, tuple(values))
            select_all_songs_query = "SELECT * FROM songs"
            cursor.execute(select_all_songs_query)
        
            all_songs = cursor.fetchall()
            for song in all_songs:
                print(song)
    
        connection.commit()

    finally:
            connection.close()




    
    
    

    
    
