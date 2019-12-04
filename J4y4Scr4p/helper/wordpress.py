from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods import posts, media
import config.properties as properties
import urllib.request
import os

def publishPost():    
    cliente = Client(properties.ENDPOINT_WORDPRESS, properties.USER_WORDPRESS, properties.PASS_WORDPRESS)
    nueva_entrada = WordPressPost()
    nueva_entrada.title = "Entrada con categorías"
    nueva_entrada.content = "Soy otra entrada publicada con la api de wp :)<br>En este caso llevo etiquetas y categorías"
    nueva_entrada.terms_names = {
                'post_tag': ['movies','politics'],
                'category': ['movies','politics']
        }
    id_entrada_publicada = cliente.call(posts.NewPost(nueva_entrada))
    print("Correcto! Se guardó la entrada como borrador, y su id es {}".format(id_entrada_publicada))
    print("Publicando entrada...")
    nueva_entrada.post_status = 'publish'
    resultado = cliente.call(posts.EditPost(id_entrada_publicada, nueva_entrada))
    if resultado is True:
        print("Entrada publicada")
    else:
        print("Algo salió mal")

def publicarlistadeposts(listawordpress):
    cliente = Client(properties.ENDPOINT_WORDPRESS, properties.USER_WORDPRESS, properties.PASS_WORDPRESS)
    for post in listawordpress:
        idImage=subeimagenpost(post.urlimagen)
        nueva_entrada = WordPressPost()
        nueva_entrada.title = post.titulo
        #nueva_entrada.content = post.contenido + post.urlpost       
        nueva_entrada.content=construyereadMore(post.contenido,post.urlpost)
        nueva_entrada.terms_names = {
                'post_tag': [post.categoria],
                'category': [post.categoria]
        }
        nueva_entrada.thumbnail=idImage
        id_entrada_publicada = cliente.call(posts.NewPost(nueva_entrada))
        nueva_entrada.post_status = 'publish'
        resultado = cliente.call(posts.EditPost(id_entrada_publicada, nueva_entrada))
        if resultado is True:
           print("Entrada publicada")

        else:
          print("Algo salió mal")


def construyereadMore(contenido,linkpost):
    espacio='<br>'
    ref1='<a href="'
    ref2='" target="_blank" rel="noopener">Read More</a>'
    concatboth=contenido+espacio+ref1+linkpost+ref2
    return concatboth
    

def subeimagenpost(mapapost):
    filename = mapapost.split('/')[-1]
    urllib.request.urlretrieve(mapapost, filename)
    cliente = Client(properties.ENDPOINT_WORDPRESS, properties.USER_WORDPRESS, properties.PASS_WORDPRESS)
    # prepare metadata
    data = {
            'name': filename,
            'type': 'image/jpeg',  # mimetype
    }
    with open(filename, 'rb') as img:
        data['bits'] = xmlrpc_client.Binary(img.read())
    response = cliente.call(media.UploadFile(data))
    if os.path.exists(filename):        
        os.remove(filename)
    return response['id']
    


       