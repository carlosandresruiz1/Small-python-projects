from lyricsgenius import Genius
from data import token
genius = Genius(token)
name = input("nombre del artista: ")
artist=genius.search_artist(name)
song = input("nombre de la cancion: ")
song = artist.song(song)
print(song.lyrics)