from main import *

# ASSERT Conversion:
assert(ascii_vers_binaire([98,111,110,106,111,117,114])==(['0b1100010', '0b1101111', '0b1101110', '0b1101010', '0b1101111', '0b1110101', '0b1110010']))
assert(ascii_vers_binaire([64,82,68,92,81])==(['0b1000000', '0b1010010', '0b1000100', '0b1011100', '0b1010001']))
assert(ascii_vers_binaire([120,103,116,64,95,100])==(['0b1111000', '0b1100111', '0b1110100', '0b1000000', '0b1011111', '0b1100100']))
assert(ascii_vers_binaire([120,76,91,91,105,81])==(['0b1111000', '0b1001100', '0b1011011', '0b1011011', '0b1101001', '0b1010001']))
assert(ascii_vers_binaire([74,81,92,124,95])==(['0b1001010', '0b1010001', '0b1011100', '0b1111100', '0b1011111']))

assert ascii_vers_string((66, 111, 110, 106, 111, 117, 114)) == "Bonjour"
assert ascii_vers_string((78, 83, 73)) == "NSI"
assert ascii_vers_string((80, 121, 116, 104, 111, 110)) == "Python"
assert ascii_vers_string((65, 98, 99)) == "Abc"
assert ascii_vers_string((120, 121, 90)) == "xyZ"

assert string_vers_ascii("bonjour") == [98, 111, 110, 106, 111, 117, 114]
assert string_vers_ascii("MeSsAgE SeCrEt") == [77, 101, 83, 115, 65, 103, 69, 32, 83, 101, 67, 114, 69, 116]
assert string_vers_ascii("Texte") == [84, 101, 120, 116, 101]
assert string_vers_ascii("James Bond") == [74, 97, 109, 101, 115, 32, 66, 111, 110, 100]
assert string_vers_ascii("007") == [48, 48, 55]

assert(binstr_vers_ascii(['0b1100010', '0b1101111', '0b1101110', '0b1101010', '0b1101111', '0b1110101', '0b1110010']) == [98,111,110,106,111,117,114])
assert(binstr_vers_ascii(['0b1000000', '0b1010010', '0b1000100', '0b1011100', '0b1010001']) == [64,82,68,92,81])
assert(binstr_vers_ascii(['0b1111000', '0b1100111', '0b1110100', '0b1000000', '0b1011111', '0b1100100']) == [120,103,116,64,95,100])
assert(binstr_vers_ascii(['0b1111000', '0b1001100', '0b1011011', '0b1011011', '0b1101001', '0b1010001']) == [120,76,91,91,105,81])
assert(binstr_vers_ascii(['0b1001010', '0b1010001', '0b1011100', '0b1111100', '0b1011111']) == [74,81,92,124,95])

# ASSERT Raccourci:
image_par_defaut = Image.open("james_bond.png")
image = image_par_defaut
changer_valeur_pixel(image,0,0,255,255,255)
assert(recuperer_valeur_pixel(image,0,0) == (255,255,255))
changer_valeur_pixel(image,10,20,40,50,60)
assert(recuperer_valeur_pixel(image,10,20) == (40,50,60))
changer_valeur_pixel(image,50,200,20,20,60)
assert(recuperer_valeur_pixel(image,50,200) == (20,20,60))
changer_valeur_pixel(image,99,66,11,88,123)
assert(recuperer_valeur_pixel(image,99,66) == (11,88,123))
changer_valeur_pixel(image,168,190,123,45,67)
assert(recuperer_valeur_pixel(image,168,190) == (123,45,67))

# ASSERT Traduction:
assert clean("blé@") == "blecutearobase"
assert clean("etnonilyenapa") == "etnonilyenapa"
assert clean("@kînîm@gîn@blé") == "arobasekichaponichapomarobasegichaponarobaseblecute"
assert clean("plutôt") == "plutochapot"
assert clean("pâlâlatîtèt") == "pachapolachapolatichapotegravet"

assert unclean("blecutearobase") == "blé@"
assert unclean("etnonilyenapa") == "etnonilyenapa"
assert unclean("arobasekichaponichapomarobasegichaponarobaseblecute") == "@kînîm@gîn@blé"
assert unclean("plutochapot") == "plutôt"
assert unclean("pachapolachapolatichapotegravet") == "pâlâlatîtèt"

assert neufbits(["0001"]) == "000000001"
assert neufbits(["11001"]) == "000011001"
assert neufbits(["1"]) == "000000001"
assert neufbits(["0"]) == "000000000"
assert neufbits(["0", "0110", "1", "011"]) == "000000000000000110000000001000000011"


# ASSERT Chiffrement et dechiffrement:
image = image_par_defaut
image = chiffrer("Bienvenue aventurier !",image)
assert(dechiffrer(image) == "Bienvenue aventurier !")

image = image_par_defaut
image = chiffrer("JE SUIS uN OuRs PolAIre ?",image)
assert(dechiffrer(image) == "JE SUIS uN OuRs PolAIre ?")

image = image_par_defaut
image = chiffrer("Plein de charactère spéciaux @,;:!âôàèé",image)
assert(dechiffrer(image) == "Plein de charactère spéciaux @,;:!âôàèé")

image = image_par_defaut
image = chiffrer("Vamos a la plâîà je suis @ la plage héhéhé x)",image)
assert(dechiffrer(image) == "Vamos a la plâîà je suis @ la plage héhéhé x)")

image = image_par_defaut
image = chiffrer("Le projet nsi c'est terminé !", image)
assert(dechiffrer(image) == "Le projet nsi c'est terminé !")

image = image_par_defaut
image = chiffrer("k@rtoffèlé sàlât", image)
assert dechiffrer(image) == "k@rtoffèlé sàlât"

print("TEST effectué avec succès")
