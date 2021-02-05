
def readFile(path):
    with open(path, "r") as f:
        a = f.readlines()
        a = [i.strip("\n").strip() for i in a]
        a = [i for i in a if i]
    return a

def writeFile(data, path):
    with open(path, "w") as f:
        for i in data:
            f.write(i + "\n")

def flattenList(nestedList): 
    if not(bool(nestedList)): 
        return nestedList 
    if isinstance(nestedList[0], list): 
        return flattenList(*nestedList[:1]) + flattenList(nestedList[1:]) 
    return nestedList[:1] + flattenList(nestedList[1:]) 

def readFileChannel(path):
    with open(path, "r") as f:
        a = f.readlines()
        a = a[1:]
        a = [i.rstrip("\n") for i in a]
        a = [i for i in a if i]
    frequency = []
    channel = []
    for i in a:
        i = i.split("\t")
        frequency.append(i[0].strip())
        channel.append(i[1].strip())
    return list(set(frequency)), list(set(channel))

def getLabelContact(string):
    a = ['B-contact'] + ['I-contact'] * (len(string.split()) - 1)
    return a

def getLabelFake(string):
    a = ['O'] * len(string.split())
    return a

def readFileEntityWithLabelContact(path):
    with open(path, "r") as f:
        a = f.readlines()
        a = [i.strip("\n").strip() for i in a]
        a = [i for i in a if i]
        a = [" ".join(i.split()) for i in a]
    contact_dict = dict()
    for i in a:
        contact_dict[i] = getLabelContact(i)
    return contact_dict

def readFileEntityWithLabelFake(path):
    with open(path, "r") as f:
        a = f.readlines()
        a = [i.strip("\n").strip() for i in a]
        a = [i for i in a if i]
        a = [" ".join(i.split()) for i in a]
    contact_dict = dict()
    for i in a:
        contact_dict[i] = getLabelFake(i)
    return contact_dict

def getLabelArtist(string):
    a = ['B-artist'] + ['I-artist'] * (len(string.split()) - 1)
    return a

def getLabelAlbum(string):
    a = ['B-album'] + ['I-album'] * (len(string.split()) - 1)
    return a

def getLabelSong(string):
    a = ['B-song'] + ['I-song'] * (len(string.split()) - 1)
    return a

def process_media_entities(artist, song, album):
    artist = [" ".join(i.split()) for i in artist]
    album = [" ".join(i.split()) for i in album]
    song = [" ".join(i.split()) for i in song]

    artist = list(set(artist))
    album = list(set(album))
    song = list(set(song))

    artist_dict = dict()
    album_dict = dict()
    song_dict = dict()
    
    for i in artist:
        artist_dict[i] = getLabelArtist(i)
    for i in album:
        album_dict[i] = getLabelAlbum(i)
    for i in song:
        song_dict[i] = getLabelSong(i)
    return artist_dict, song_dict, album_dict

def readJsonAddressFile(path):
    import json
    with open(path, "r") as f:
        a = json.load(f)
    cities = []
    address = []

    for i in a:
        cities.append(i["City"])
        address.append(i["Street"])
    return cities, address

