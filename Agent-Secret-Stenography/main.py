from PIL import Image

# Conversion
def string_vers_ascii(message: str) -> int:
    """
    Convertie une chaine de charactere en une liste de nombre correspondant a la table ASCII
    message : message a convertir
    output : liste_ASCII : liste de int correspondant a chaque lettre du message en ASCII
    """
    liste_ascii = []
    for charactere in message:
        liste_ascii.append(ord(charactere))
    return liste_ascii


def ascii_vers_binaire(message_ascii: list) -> list:
    """
    convertie en une liste de binaire une liste d'ascii
    message en ascii = liste de nombre correspondant à un message en ascii
    output : binaire = liste de binaire en string
    """
    binaire = []
    for ligne in message_ascii:
        binaire.append(str(bin(ligne)))
    return binaire


def ascii_vers_string(message_en_ascii: list) -> str:
    """
    Input: une liste contenant chaque lettre en ASCII
    Output: une chaine de caractère contenant le message traduit en utilisant la table ASCII;
    """
    message = ""
    for i in message_en_ascii:
        message += chr(i)
    return message


def binstr_vers_ascii(message_binstr: list) -> list:
    """
    Input: une liste contenant chaque lettre en binaire
    Output: une chaine de caractère contenant le message traduit en ASCII
    """
    liste_ascii = []
    for i in message_binstr:
        liste_ascii.append(int(i, 2))
    return liste_ascii


# Tradution
def clean(text: str) -> str:
    """
    Input: le message avec des caractères accentués
    Ouput: le même message mais avec des codes plutôt que des caractères spéciaux
    """
    text = text.replace("é", "ecute")
    text = text.replace("è", "egrave")
    text = text.replace("ç", "ccedilla")
    text = text.replace("@", "arobase")
    text = text.replace("à", "agrave")
    text = text.replace("ê", "echapo")
    text = text.replace("â", "achapo")
    text = text.replace("î", "ichapo")
    text = text.replace("ô", "ochapo")
    return text


def unclean(text: str) -> str:
    """
    Input: le message avec des codes à la place des caractères spéciaux
    Output: le message d'origine avec les caractères spéciaux à la place des codes de caractères
    """
    text = text.replace("ecute", "é")
    text = text.replace("egrave", "è")
    text = text.replace("ccedilla", "ç")
    text = text.replace("arobase", "@")
    text = text.replace("agrave", "à")
    text = text.replace("echapo", "ê")
    text = text.replace("achapo", "â")
    text = text.replace("ichapo", "î")
    text = text.replace("ochapo", "ô")
    return text


# Raccourcis
def recuperer_valeur_pixel(image, coord_x, coord_y) -> tuple:
    """
    recuperer la couleur de 1 pixel d'une image r,v,b
    image : l'image a modifier
    coord_x : coordonnée x du pixel a modifier
    coord_y : coordonnée y du pixel a modifier
    output : retourne un tuple rouge,vert,bleu de couleur ascii
    """
    rouge, vert, bleu = image.getpixel((coord_x, coord_y))
    return (rouge, vert, bleu)


def neufbits(message_bin: list) -> str:
    """
    Input: une liste de string contenant le messages en binaire avec différentes tailles
    Output: un string contenant l'ensemble du message en binaire avec tout les caractères exprimé en binaire sur 9 bits
    """
    for i in message_bin:  # On met tous les caractères sur le même nombre de bit
        if len(i) != 9:
            a = i.zfill(9)
            message_bin[message_bin.index(i)] = a

    msg_bin = "".join([str(k) for k in message_bin])  # On transforme la liste contenant les différents caractères en un string
    msg_bin = msg_bin.replace("b", "0")  # On remplace l'identificateur par défaut de python par un 0
    return msg_bin


def changer_valeur_pixel(image, coord_x, coord_y, rouge, vert, bleu):
    """
    change la couleur d"un pixel d"une image
    image: l"image a modifier
    coord_x: coordonnée x du pixel a modifier
    coord_y: coordonnée y du pixel a modifier
    rouge: valeur rouge de 0 a 255 du pixel a modifier
    vert: valeur vert de 0 a 255 du pixel a modifier
    bleu: valeur bleu de 0 a 255 du pixel a modifier
    output : None
    """
    image.putpixel((coord_x, coord_y), (rouge, vert, bleu))
    return


def chiffrer(text: str, image):
    """
    Input: le texte à sténographier et l'image dans laquelle il faut sténographier le message
    Ouput: l'image avec le message et la taille du message sténographiés
    Appelle les autres fonctions pour réaliser la suite d'opérations nécessaires
    """
    text = clean(text)
    message_ascii = string_vers_ascii(text)
    message_bin = ascii_vers_binaire(message_ascii)
    msg_bin = neufbits(message_bin)
    image = stenographie_taille(image, msg_bin)
    if image == None:
        return None
    image = stenographie(image, msg_bin)
    return image


def dechiffrer(image):
    """
    Input: l'image avec un code sténographié
    Ouput: le messages sténographié dans l'image
    Appelle les autres fonctions pour réaliser la suite d'opérations nécessaires
    """
    taille_message = destenographie_taille(image)
    message = destenographie(image, taille_message)
    message = unclean(message)
    return message


# Verification (supprimable)
def verif_taille_image(image, taille_message):
    """
    verifie que le message peut tenir dans l'image
    image : image a verifié
    taille_message : taille du message a vérifier
    sortie : boolean
            true : le message tient dans l'image
            false : le message ne tient pas dans l'image
    """

    largeur, hauteur = image.size  # taille de l'image
    if taille_message < largeur*hauteur-largeur-1:
        return True
    else:
        return False


# Taille
def stenographie_taille(image, msg_bin: list):
    """
    Input: l'image où il faut inclure la taille du message et le message dont il faut déterminer la taille
    Output: l'image avec la taille du message sténographié sur la première ligne
    On détermine la taille du message puis on l'écrit en binaire dans les dernières valeurs des couleurs de chaque pixel
    """
    largeur, hauteur = image.size
    x, y, place = 0, 0, 0  # coordonnée du pixel x, y
    taille = len(msg_bin)
    if verif_taille_image(image,taille) is False:
	    print("erreur l'image donnée est trop petite pour inclure le message donnée")
	    return None
    taille = bin(taille).replace("b", "0")
    taille = taille.zfill(largeur * 3)

    for _ in range(int(len(taille) / 3)):
        # On récupère les valeurs des couleurs du pixel
        rouge, vert, bleu = image.getpixel((x, y))
        # On transforme les valeurs des couleurs en binaire pour les traiter
        rouge, vert, bleu = bin(rouge), bin(vert), bin(bleu)

        rougeliste = [j for j in rouge]  # qu'on met en liste pour la modifier
        rougeliste[-1] = taille[place]  # On applique les modifications
        # On retransforme en string
        rouge = "".join([str(k) for k in rougeliste])
        place += 1

        vertliste = [j for j in vert]  # qu'on met en liste pour la modifier
        vertliste[-1] = taille[place]  # On applique les modifications
        # On retransforme en string
        vert = "".join([str(k) for k in vertliste])
        place += 1

        bleuliste = [j for j in bleu]  # qu'on met en liste pour la modifier
        bleuliste[-1] = taille[place]  # On applique les modifications
        # On retransforme en string
        bleu = "".join([str(k) for k in bleuliste])
        place += 1

        rouge, vert, bleu = int(rouge, 2), int(vert, 2), int(bleu, 2)
        changer_valeur_pixel(image, x, y, rouge, vert, bleu)
        x += 1

    return image


def destenographie_taille(image) -> int:
    """
    decrypte la taille du message dans une image
    image : image a décrypter
    sortie : taille du message en int
    """
    l, h = image.size  # taille de l'image
    val = ""
    for x in range(l):  # coordonnée du pixel x
        r, v, b = recuperer_valeur_pixel(image, x, 0)  # valeur rouge, vert, bleu ascii allant de 0 à 255
        couleur_binaire = ascii_vers_binaire([r, v, b])  # valeur rouge, vert, bleu sous forme binaire
        for couleur in couleur_binaire:
            val += couleur[-1]  # recupere le dernier bit de la couleur
    taille_message = int(val, 2)  # transforme la taille du message binaire en int
    return taille_message // 3


# Sténographie
def stenographie(image, msg_bin: list):
    """
    Input: l'image où il faut inclure le message et le message à inclure
    Output: l'image avec le message sténographié à partir de la seconde ligne
    On écrit le message en binaire dans les dernières valeurs des couleurs de chaque pixel
    """
    largeur, hauteur = image.size
    x, y, place = 0, 1, 0  # coordonnée du pixel x, y
 
    for _ in range(int(len(msg_bin) / 3)):
        # On récupère les valeurs des couleurs du pixel
        rouge, vert, bleu = image.getpixel((x, y))
        # On transforme les valeurs des couleurs en binaire pour les traiter
        rouge, vert, bleu = bin(rouge), bin(vert), bin(bleu)

        rougeliste = [j for j in rouge]  # qu'on met en liste pour la modifier
        rougeliste[-1] = msg_bin[place]  # On applique les modifications
        # on retransforme en string
        rouge = "".join([str(k) for k in rougeliste])
        place += 1

        vertliste = [j for j in vert]  # qu'on met en liste pour la modifier
        vertliste[-1] = msg_bin[place]  # On applique les modifications
        # on retransforme en string
        vert = "".join([str(k) for k in vertliste])
        place += 1

        bleuliste = [j for j in bleu]  # qu'on met en liste pour la modifier
        bleuliste[-1] = msg_bin[place]  # On applique les modifications
        # on retransforme en string
        bleu = "".join([str(k) for k in bleuliste])
        place += 1

        rouge, vert, bleu = int(rouge, 2), int(vert, 2), int(bleu, 2)
        changer_valeur_pixel(image, x, y, rouge, vert, bleu)
        x += 1
        if (x == largeur - 1):
            y += 1
            x = 0
            if y == hauteur - 1:
                break

    return image


def destenographie(image, taille_message: int) -> str:
    """
    decrypte le message dans une image
    image : image a décrypter
    taille_message : taille du message a décrypter
    sortie : message en str
    """
    l, h = image.size
    bits_par_lettre = 9  # nombre de bits par charactere
    nb_bits = 0 
    x = 0  # coordonnée du pixel x
    y = 1  # coordonnée du pixel y
    tab_bits = []
    tab_octet = []
    for nb_bits in range(taille_message):
        r, v, b = recuperer_valeur_pixel(image, x, y)  # valeur rouge , vert , bleu en ascii
        couleur_binaire = ascii_vers_binaire([r, v, b])  # valeur rouge , vert , bleu en binaire
        tab_bits.append(couleur_binaire[0][-1])  # ajoute la couleur rouge binaire au tableau
        tab_bits.append(couleur_binaire[1][-1])  # ajoute la couleur vert binaire au tableau
        tab_bits.append(couleur_binaire[2][-1])  # ajoute la couleur bleu binaire au tableau

        x += 1  # rajoute 1 aux coordonnées de x 
        if x == l-1:  # si x est au bord de l'image
            y += 1
            x = 0
            if y == h-1:
                break
    tab = []
    for i in range(len(tab_bits)):
        tab.append(tab_bits[i])
        if (i+1) % bits_par_lettre == 0:
            tab_octet.append(tab)  # regroupe par charactere les bits
            tab = []

    liste_binaire = []
    for octet in tab_octet:
        val = ''
        for bit in octet:
            val += str(bit)
        liste_binaire.append(val)  # octet sous forme de str

    liste_ascii = binstr_vers_ascii(liste_binaire)  # convertie le binaire en ascii
    liste_lettre = ascii_vers_string(liste_ascii)  # convertie le ascii en str
    message = "".join(liste_lettre)
    return message

if __name__ == "__main__":

    text = """Dans ses Histoires, l'historien grec Hérodote (484-445 av. J.-C.) rapporte
    ainsi une anecdote qui eut lieu au moment de la seconde guerre médique. En 484 av. J.-C., Xerxès Ier,
    roi des Perses, décide de préparer une armée gigantesque pour envahir la Grèce (Livre VII, 5-19).
    Quatre ans plus tard, lorsqu'il lance l'offensive, les Grecs sont depuis longtemps au courant de ses
    intentions. C'est que Démarate, ancien roi de Sparte réfugié auprès de Xerxès, a appris l'existence
    de ce projet et décide de transmettre l'information à Sparte (Livre VII, 239) :

    il prit une tablette double, en gratta la cire, puis écrivit sur le bois même les projets de Xerxès ;
     ensuite il recouvrit de cire son message : ainsi le porteur d'une tablette vierge ne risquait pas
     d'ennuis.

    Un autre passage de la même oeuvre fait également référence à la stéganographie : au paragraphe 35 du
    livre V, Histiée incite son gendre Aristagoras, gouverneur de Milet, à se révolter contre son roi,
    Darius, et pour ce faire,

    il fit raser la tête de son esclave le plus fidèle, lui tatoua son message sur le crâne et attendit
    que les cheveux eussent repoussé ; quand la chevelure fut redevenue normale, il fit partir l'esclave
    pour Milet.

    En Chine, on écrivait le message sur de la soie, qui ensuite était placée dans une petite boule
    recouverte de cire. Le messager avalait ensuite cette boule.

    Dès le ier siècle av. J.-C., Pline l'Ancien décrit comment réaliser de l'encre invisible (ou encre
    sympathique). Les enfants de tous les pays s'amusent à le faire en écrivant avec du lait ou du jus de
    citron : le passage de la feuille écrite sous une source chaude (fer à repasser chaud, flamme de bougie...) révèle le message.
    """

    image = Image.open("asset/james_bond.png")
    image = chiffrer(text, image)
    image.save("007.png", "png")
