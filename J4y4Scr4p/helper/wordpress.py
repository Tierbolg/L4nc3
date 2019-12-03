from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods import posts
import config.properties as properties

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