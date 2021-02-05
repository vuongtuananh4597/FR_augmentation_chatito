import numpy as np
from utils import *

# path template general
path_template_general = "general_command/template/FR_common_general.txt"
path_template_radio = "general_command/template/radio.txt"
path_template_quickcontrol = "general_command/template/quickcontrol.txt"
path_template_climate1 = "general_command/template/clim1.txt"
path_template_climate2 = "general_command/template/clim2.txt"

PERCENT = [str(i) for i in np.arange(10,100)]
LEVEL_ALL = [str(i) for i in np.arange(2,7)]
TEMPERATURE = [str(i) for i in np.arange(15,36)]
TEMP_CHANGE = [str(i) for i in np.arange(2,11)]
RADIO_NAME = "FM"
FREQUENCY, CHANNEL = readFileChannel("general_command/entity_file/FM_radio_station")


path_template_phone = "entity_command/phonebook/template/FR_phonebook_template.txt"

PERSON = readFileEntityWithLabelContact("entity_command/phonebook/entity_file/FR_nicknames.txt")
PHONE_NUMBER = readFileEntityWithLabelFake("entity_command/phonebook/entity_file/FR_phone.txt")


# path template navigation
path_template_navigation = "entity_command/navigation/template/FR_navigation_template.txt"
CITY, STREET_NAME = readJsonAddressFile("entity_command/navigation/entity_file/French_address_dict.json")

# path template media
path_template_media = "entity_command/media/template/FR_media_template.txt"
artist_album = readFile("entity_command/media/entity_file/FR_artist_album.txt")
song_artist = readFile("entity_command/media/entity_file/FR_song_artist.txt")
artist_album = artist_album[1:]
song_artist = song_artist[1:]

ARTIST = []
SONG = []
ALBUM = []
print(artist_album)

for i in artist_album:
    i = i.split(",")
    try:
        ARTIST.append(i[0].strip())
        ALBUM.append(i[1].strip())
    except:
        continue
for i in song_artist:
    i = i.split(",")
    try:
        SONG.append(i[0].strip())
        ARTIST.append(i[1].strip())
    except:
        continue
ARTIST_v1 = list(set(ARTIST))
SONG_v1 = list(set(SONG))
ALBUM_v1 = list(set(ALBUM))

ARTIST, SONG, ALBUM = process_media_entities(ARTIST_v1, SONG_v1, ALBUM_v1)



