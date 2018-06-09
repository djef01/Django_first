#from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, Artist, Contact, Booking
#from .models import ALBUMS

# Create your views here.
def index(request):
    #request albums
    albums = Album.objects.filter(available=True).order_by('created_at')[:12]
    # then format the requestself.
    # note that we don't use album['name'] anymore but album.name
    # because it's now an attributeself.
    formatted_abums = ["<li>{}</li>".format(album.title) for album in albums]
    message = """<ul>{}</ul>""".format("\n".join(formatted_abums))
    return HttpResponse(message)

def listing(request):
    albums = Album.objects.filter(available=True)
    formatted_abums = ["<li>{}</li>".format(album.title) for album in albums]
    message = """<ul>{}</ul>""".format("\n".join(formatted_abums))
    return HttpResponse(message)

def detail(request, album_id):
    album = Album.objects.get(pk=album_id)
    artists = "".join([artist.name for artist in album.artists.all()]) #grab artists name and create a string out of it
    message = "Le nom de l' album es {}. il a été écrit par {}".format(album.title, artists)
    return HttpResponse(message)


def search(request):
    query = request.GET.get('query')
    if not query:
        album = Album.objects.all()
    else:
        # title contains the query and query is not sensitive to case.
        albums = Album.objects.filter(title__icontains=query)

    if not albums.exists():
            message = "Misère de misère, nous n avons trouvé aucun résulta !"
    else:
            albums = ["<li>{}</li>".format(album.title) for album in albums]
            message = """
                Nous avons trouvé les albums correspondant á votre requète ! Les voici :
                <ul>{}</ul>
            """.format("</li><li>".join(albums))

    return HttpResponse(message)
