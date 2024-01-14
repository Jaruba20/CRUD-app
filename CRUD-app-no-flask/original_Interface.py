import argparse

import Database_interact as send

def set_table(table_name):
    send.set_table(table_name)

def show_all():
    send.show_all()

def add_song_to_db(*args):
    send.add_song_to_db(args)

def search_song_by(**kwargs):
    send.search_song_by(kwargs)

def delete_song_by(**kwargs):
    send.delete_song_by(kwargs)

def update_song_by(**kwargs):
    send.update_song_by(kwargs)


def main():
    parser = argparse.ArgumentParser(description="CRUD operations over a music DB")
    subparsers = parser.add_subparsers(help="Subcommands", dest="command")

    # Subparser for selecting the table to modify.
    create_parser = subparsers.add_parser('set_table', help='Select the working table')
    create_parser.add_argument('--name', help='Name of the table', required=True)

    # Subparser for showing the hole table.
    create_parser = subparsers.add_parser('show_all', help='Show the hole table')

    # Subparser for the 'create' command
    create_parser = subparsers.add_parser('create', help='Add a song to the DB')
    create_parser.add_argument('--song', help='Name of the song', required=True)
    create_parser.add_argument('--album', help="Name of the album", required=True)
    create_parser.add_argument('--artist', help="Name of the artist", required=True)
    

    # Subparser for the 'search' command
    search_parser = subparsers.add_parser('search', help='Search in the music db')
    search_parser.add_argument('--song', help='Name of the song', default=None)
    search_parser.add_argument('--album', help='Name of the album', default=None)
    search_parser.add_argument('--artist', help='Name of the artist', default=None)

    # Subparser for the 'delete' command
    search_parser = subparsers.add_parser('delete', help='Delete a song/songs of the music db')
    search_parser.add_argument('--song', help='Name of the song', default=None)
    search_parser.add_argument('--album', help='Name of the album', default=None)
    search_parser.add_argument('--artist', help='Name of the artist', default=None)
   
   # Subparser for the 'update' command
    search_parser = subparsers.add_parser('update', help='Update a song/songs of the music db')
    search_parser.add_argument('--song', help='Name of the song(condition)', default=None)
    search_parser.add_argument('--album', help='Name of the album(condition)', default=None)
    search_parser.add_argument('--artist', help='Name of the artist(condition)', default=None)
    search_parser.add_argument('--set_song', help='Name of the song to set', default=None)
    search_parser.add_argument('--set_album', help='Name of the album to set', default=None)
    search_parser.add_argument('--set_artist', help='Name of the artist to set', default=None)

    args = parser.parse_args()
   
    match args.command:
        #case "login":
        #    login(user=args.user)
        #case "logout":
        #    logout()
        case "set_table":
            set_table(args.name)
        case "show_all":
            show_all()
        case "create":
            add_song_to_db(args.song, args.album, args.artist)
        case "search":
            search_song_by(song=args.song, album=args.album, artist=args.artist)
        case "delete":
            delete_song_by(song=args.song, album=args.album, artist=args.artist)
        case "update":
            update_song_by(set_song=args.set_song, set_album=args.set_album, set_artist=args.set_artist, song=args.song, album=args.album, artist=args.artist)
        case _:
            parser.print_help()

if __name__ == '__main__':
    main()