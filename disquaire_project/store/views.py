#from django.shortcuts import render
from django.http import HttpResponse
#from .models import ALBUMS

# Create your views here.
def index(request):
    message = "Salut tous le monde !"
    return HttpResponse(message)

def listing(request):
    album = ["<li>{}</li>".format(album['name']) for album in ALBUMS]
    message = """<ul>{}</ul>""".format("\n".join(album))
    return HttpResponse(message)

def detail(request, album_id):
    id = int (album_id) #make sure we have an integerself.
    album = ALBUMS[id] # get the album with its idself.
    artists = "".join([artist['name'] for artist in album['artists']]) #grab artists name and create a string out of it
    message = "Le nom de l' album es {}. il a été écrit par {}".format(album['name'], artists)
    return HttpResponse(message)


def search(request):
    query = request.GET.get('query')
    if not query:
        message = "Aucun artiste n ' est demandé"
    else:
        albums = [
            album for album in ALBUMS
            if query in "".join(artist['name'] for artist in album['artists'])
        ]

        if len(albums) == 0:
            message = "Misère de misère, nous n avons trouvé aucun résulta !"
        else:
            album = ["<li>{}</li>".format(album['name']) for album in albums]
            message = """
                Nous avons trouvé les albums correspondant á votre requète ! Les voici :
                <ul>
                    {}
                </ul>
            """.format("</li><li>".join(album))

    return HttpResponse(message)
