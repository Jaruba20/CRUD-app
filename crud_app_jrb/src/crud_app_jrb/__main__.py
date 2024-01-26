import argparse

import db_interact as send


def set_table(table_name):
    send.set_table(table_name)


def user_query(query):
    # send.user_query(args[0], args[1])
    return send.user_query(query)


def show_all():
    return send.show_all()


def add_song_to_db(*args):
    return send.add_song_to_db(args)


def search_song_by(**kwargs):
    return send.search_song_by(kwargs)


def delete_song_by(**kwargs):
    return send.delete_song_by(kwargs)


def update_song_by(**kwargs):
    return send.update_song_by(kwargs)



def main():
    parser = argparse.ArgumentParser(description="CRUD operations over a music DB")
    subparsers = parser.add_subparsers(help="Subcommands", dest="command")

    # Subparser for selecting the table to modify.
    set_parser = subparsers.add_parser("set_table", help="Select the working table")
    set_parser.add_argument("--name", help="Name of the table", required=True)

    # Subparser for letting the user enter a query.
    user_query_parser = subparsers.add_parser(
        "entry_query", help="Entry a hole MySQL query"
    )
    user_query_parser.add_argument("--query", help="Query to enter", required=True)
    # user_query_parser.add_argument('--number', help='Int/float to enter', required=True)

    # Subparser for showing the hole table.
    show_all_parser = subparsers.add_parser("show_all", help="Show the hole table")

    # Subparser for the 'create' command
    create_parser = subparsers.add_parser("create", help="Add a song to the DB")
    create_parser.add_argument("--song", help="Name of the song", required=True)
    create_parser.add_argument("--album", help="Name of the album", required=True)
    create_parser.add_argument("--artist", help="Name of the artist", required=True)
    create_parser.add_argument("--genre", help="Name of the genre", required=True)

    # Subparser for the 'search' command
    search_parser = subparsers.add_parser("search", help="Search in the music db")
    search_parser.add_argument("--song", help="Name of the song", default=None)
    search_parser.add_argument("--album", help="Name of the album", default=None)
    search_parser.add_argument("--artist", help="Name of the artist", default=None)
    search_parser.add_argument("--genre", help="Name of the genre", required=None)

    # Subparser for the 'delete' command
    delete_parser = subparsers.add_parser(
        "delete", help="Delete a song/songs of the music db"
    )
    delete_parser.add_argument("--song_id", help="Id of the song", default=None)
    delete_parser.add_argument("--song", help="Name of the song", default=None)
    delete_parser.add_argument("--album", help="Name of the album", default=None)
    delete_parser.add_argument("--artist", help="Name of the artist", default=None)
    delete_parser.add_argument("--genre", help="Name of the genre", required=None)

    # Subparser for the 'update' command
    update_parser = subparsers.add_parser(
        "update", help="Update a song/songs of the music db"
    )
    update_parser.add_argument(
        "--song", help="Name of the song(condition)", default=None
    )
    update_parser.add_argument(
        "--album", help="Name of the album(condition)", default=None
    )
    update_parser.add_argument(
        "--artist", help="Name of the artist(condition)", default=None
    )
    update_parser.add_argument(
        "--genre", help="Name of the genre(condition)", default=None
    )
    update_parser.add_argument(
        "--set_song", help="Name of the song to set", default=None
    )
    update_parser.add_argument(
        "--set_album", help="Name of the album to set", default=None
    )
    update_parser.add_argument(
        "--set_artist", help="Name of the artist to set", default=None
    )
    update_parser.add_argument(
        "--set_genre", help="Name of the genre to set", default=None
    )

    args = parser.parse_args()

    match args.command:
        # case "login":
        #    login(user=args.user)
        # case "logout":
        #    logout()
        case "set_table":
            set_table(args.name)
        case "entry_query":
            # user_query(args.query, args.number)
            user_query(args.query)
        case "show_all":
            show_all()
        case "create":
            add_song_to_db(args.song, args.album, args.artist, args.genre)
        case "search":
            search_song_by(
                song=args.song, album=args.album, artist=args.artist, genre=args.genre
            )
        case "delete":
            delete_song_by(
                song_id=args.song_id,
                song=args.song,
                album=args.album,
                artist=args.artist,
                genre=args.genre,
            )
        case "update":
            update_song_by(
                set_song=args.set_song,
                set_album=args.set_album,
                set_artist=args.set_artist,
                set_genre=args.set_genre,
                song=args.song,
                album=args.album,
                artist=args.artist,
                genre=args.genre,
            )
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
