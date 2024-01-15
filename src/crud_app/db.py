from abc import ABC, abstractmethod

class DataBase(ABC):

    def __init():
        pass

    @abstractmethod
    def create(song: str, album : str, artist: str):
        pass
    
    @abstractmethod
    def search(song: str, album : str, artist: str):
        pass

    @abstractmethod
    def delete(song: str, album : str, artist: str):
        pass

class MySQL(DataBase):
    print("hola2")

db = DataBase()

db.test()