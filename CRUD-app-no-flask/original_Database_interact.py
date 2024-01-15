import pymysql
import configparser
import pandas as pd

cfg = "original.cfg"
config = configparser.ConfigParser()
config.read(cfg)


# Requires a Mysql database
# For example with:
# docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -e MYSQL_DATABASE=db -p 8001:3306 -d mysql:latest


# Create a connection to MySQL using pymysql
connection = pymysql.connect(
    host=config.get("CONNECTION", "hostname"),
    user=config.get("CONNECTION", "username"),
    password=config.get("CONNECTION", "password"),
    port=int(config.get("CONNECTION", "port")),
    database=config.get("CONNECTION", "database"),
    cursorclass=pymysql.cursors.DictCursor  # Use DictCursor for fetching results as dictionaries
)

TABLE_NAME = config.get("DATABASE", "table")

# HACE FALTA EL GETTER? LO HAGO POR SI DURANTE LA EJECUCIÓN LO HE CAMBIADO CON set_table(), Y LO TENGO QUE VOLVER A LLAMAR ANTES DE CERRAR EL PROGRAMA
# NO SÉ SI SE VUELVE A EJECUTAR EL config.get DE ARRIBA O NO. ENTIENDO QUE NO.
def get_table():
    config.read(cfg) #VER SI ME HACE FALTA ESTO O NO
    TABLE_NAME = config.get("DATABASE", "table")
    return TABLE_NAME

def set_table(name):
    '''
    Changes the working table in the cfg file.
    '''
    TABLE_NAME = config.set("DATABASE", "table", name)
    with open(cfg, "w") as config_file:
        config.write(config_file)
    
    print("Saved new working table")

def interact(userQuery, userValues = None):
    '''Executes the desired query in the database'''
    try:
        with connection.cursor() as cursor:
            
            cursor.execute(userQuery, userValues)

            rows = cursor.fetchall()
            
            if not rows:
                print("No results to display")
                return
            
            df = pd.DataFrame.from_dict(rows)
            df.set_index("song_id", inplace=True)
            print(df)

            connection.commit()
            
            '''for row in rows:
                print(row)'''

    finally:
            connection.close()

#def user_query(query, number):
def user_query(query):
    '''Sends to execute a query introduced by the user'''
    #return interact(query, (int(number),))
    return interact(query)


def show_all():
    '''Shows the hole table'''
    show_table = f"""
        SELECT * FROM {get_table()}
        """
    return interact(show_table)
        
def add_song_to_db(args):
    '''Adds a song to the table'''

    insert_song = f"""
        INSERT INTO {get_table()} (song_name, album_name, artist_name) 
        VALUES (%s, %s, %s)
        """
    interact(insert_song, args)


def search_song_by(kwargs):
    search_song = f"SELECT * FROM {get_table()} WHERE"
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
    if kwargs["genre"]:
        conditions.append("genre = %s")
        values.append(kwargs["genre"])
    if conditions:
        search_song += " " + " AND ".join(conditions)

    return interact(search_song, values)


def delete_song_by(kwargs):
    delete_song = f"DELETE FROM {get_table()} WHERE"
    conditions = []
    values = []
    if kwargs["song_id"]:
        conditions.append("song_id = %s")
        values.append(kwargs["song_id"])
    if kwargs["song"]:
        conditions.append("song_name = %s")
        values.append(kwargs["song"])
    if kwargs["album"]:
        conditions.append("album_name = %s")
        values.append(kwargs["album"])
    if kwargs["artist"]:
        conditions.append("artist_name = %s")
        values.append(kwargs["artist"])
    if kwargs["genre"]:
        conditions.append("genre = %s")
        values.append(kwargs["genre"])
    if conditions:
        delete_song += " " + " AND ".join(conditions)

    interact(delete_song, values)


def update_song_by(kwargs):
    update_song = f"""UPDATE {get_table()}
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
    if kwargs["set_genre"]:
        conditions.append("genre = %s")
        values.append(kwargs["set_genre"])
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
    if kwargs["genre"]:
        conditions.append("genre = %s")
        values.append(kwargs["genre"])
    
    if conditions:
        update_song += "WHERE" + " " + " AND ".join(conditions)

    interact(update_song, values)
    
