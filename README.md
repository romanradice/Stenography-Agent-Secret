# Agent-Secret-Stenography

## Projet
Outil pour cacher un message secret dans une image

## Méthode
chaque pixel est codé par 3 nombres du système RVB.
Chacun de ces 3 nombres est compris entre 0 et 255, avec 1 octet, soit 8 bits, on peut coder 256 valeurs.
Sur chaque pixel, on modifie seulement le bit de poids faible des 3 couleurs.
une image de 600 x 416 soit de 249600 pixels peut donc stocker 93600 caractères.
</br>
</br>
On peut:
- soit chiffrer un message dans une image 
- soit déchiffrer le message d'une image

## Etapes
### Chifrement
- on convertit le message ascii en binaire
- on enregistre la longueur du message sur la premiere ligne
- on change la valeur du dernier bits de chaque couleur des pixels pour les faires correspondres au message en binaire.

### Dechiffrement
- on déchiffre la taille du message sur la premiere ligne
- on déchiffre chaque bits bits de chaque couleur des pixels
- on convertit le message binaire en ascii

## Screenshot

![chiffrer](https://user-images.githubusercontent.com/65543135/174397787-fa68daaa-9e8c-4435-975c-9697667de733.PNG)
![dechiffrer](https://user-images.githubusercontent.com/65543135/174397797-bc819c04-7d66-4db7-a6e7-039dae55958f.PNG)
