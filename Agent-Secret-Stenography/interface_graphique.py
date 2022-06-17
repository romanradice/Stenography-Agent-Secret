from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk

from PIL import ImageTk
from main import *


# CONST
fichier_image = "asset/james_bond.png"
radio_text = ["Chiffrement", "Déchiffrement"]
radio_value = [1, 2]


def ouvrir_image(fichier_image):
    """
    ouvre une image et l'affiche dans le label
    fichier_image : path de l'image
    """
    try:
        image = Image.open(fichier_image)
        if image.size[0] > 800 or image.size[1] > 450:
            image = image.resize((800, 450), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label_img.config(image=photo)
        label_img.image = photo
        return image

    except FileNotFoundError:
        print("Image introuvable")
    return None


def action_valider(image, radioVariable):
    """
    crypte ou decrypte l'image
    radioVariable : option choisis
    1 cryptage ; 2 décryptage
    sortie : si cryptage : image ; si décryptage : message
    """
    if radioVariable.get() == 1:  # Chiffrement
        if image != None:
            text = message.get("1.0", "end")
            image = chiffrer(text, image)
            if image != None:
                image.save("007.png", "png")
                tk.messagebox.showinfo("Info", "Image enregistrée avec succès")
            else:
                tk.messagebox.showerror(title="Erreur", message="Le message est trop long pour être sténographié dans l'image")
    elif radioVariable.get() == 2:  # Déchiffrement
        if image != None:
            text = dechiffrer(image)
            change_message_texte(text)


def mode_chiffrement():
    """
    mode decryptage : réactive le Text, désactive le mode readonly
    """
    message.configure(state="normal")  # pour pouvoir ecrire dans le text desactive le mode readonly


def mode_dechiffrement():
    """
    mode decryptage : active le readonly sur le Text
    """
    message.configure(state='normal')  # pour pouvoir ecrire dans le text desactive le mode readonly
    message.delete(1.0, "end")  # suprimme le texte
    message.configure(state='disabled')  # remet le mode readonly


def change_message_texte(texte):
    """
    change le message du Text en mode décryptage
    texte : texte a afficher dans le TEXT message
    """
    message.configure(state='normal')  # pour pouvoir ecrire dans le text desactive le mode readonly
    message.delete(1.0, "end")  # suprimme le texte
    message.insert(1.0, texte)  # ecrit le texte
    message.configure(state='disabled')  # remet le mode readonly


# MENU BAR
def ouvrir_Fichier():
    """
    ouvre un fichier image et actualise le label image
    """
    file = tk.filedialog.askopenfilename(initialdir="/Desktop", title="Choose image file", filetypes=(
        ('png files', '.png'), ('jpg files', '.jpg'), ("All files", ".*")))
    if file != "":
        global fichier_image, image
        fichier_image = str(file)
        image = ouvrir_image(fichier_image)


def a_propos():
    """
    A propos du logiciel : projet nsi 2020/2021
    """
    tk.messagebox.showinfo(title="A Propos", message="Projet de NSI 2020/2021 par Radice Roman, Albisson Hugo et Roy Agathe")


def sauvegarde_fichier(image):
    """
    sauvegarde l'image
    image : image a sauvegarder
    """
    image.save("007.png", "png")
    tk.messagebox.showinfo("Info", "Image enregistrée")


def mise_en_place_menuBar(root):
    """
    cree le menu de la fenetre et lui assigne des fonctions
    root : fenetre graphique
    sortie : Bar de menu
    """
    MenuBar = tk.Menu(root)
    menuFile = tk.Menu(MenuBar, tearoff=0)
    menuFile.add_command(label="Ouvrir", command=ouvrir_Fichier)
    menuFile.add_separator()
    menuFile.add_command(label="Sauvegarder", command=lambda: sauvegarde_fichier(image))
    menuFile.add_separator()
    menuFile.add_command(label="Quitter", command=root.destroy)
    MenuBar.add_cascade(label="Fichier", menu=menuFile)

    menuHelp = tk.Menu(MenuBar, tearoff=0)
    menuHelp.add_command(label="A propos", command=a_propos)
    MenuBar.add_cascade(label="Aide", menu=menuHelp)
    return MenuBar


# Création de la fenêtre
root = tk.Tk()  # creation d'une fenetre
root.title("Agent Secret")  # nom de la fenetre
radioVariable = tk.IntVar()

# creation d'un Label
presentation = tk.Label(root, text="Agent Secret: Chiffrer ou déchiffrer une image")  # creation du label
# place le label dans la fenetrea l'emplacement 0,0 avec une taille 2,1
presentation.grid(row=0, column=0, columnspan=2, sticky="nsew")

# creation du label contenant l'image
label_img = tk.Label(root)  # creation du label
# place le label dans la fenetrea l'emplacement 0,1 avec une taille 2,2
label_img.grid(row=1, column=0, rowspan=2, columnspan=2, sticky="nsew")
image = ouvrir_image(fichier_image)

# Bar de menu
Menubar = mise_en_place_menuBar(root)  # Creation de la bar de menu
root.config(menu=Menubar)

# Création d'un radio button
b_radio_1 = tk.Radiobutton(root, variable=radioVariable, text=radio_text[0], value=radio_value[0], indicatoron=0)
# place le bouton radio 1 dans la fenetrea l'emplacement 3,0 avec une taille 1,1
b_radio_1.grid(row=3, column=0, sticky="nsew")
b_radio_2 = tk.Radiobutton(root, variable=radioVariable, text=radio_text[1], value=radio_value[1], indicatoron=0)
# place le bouton radio 2 dans la fenetrea l'emplacement 3,1 avec une taille 1,1
b_radio_2.grid(row=3, column=1, sticky="nsew")
b_radio_1.invoke()

# creation d'un Text Message
message = tk.Text(root)
# place le TEXT message dans la fenetre a l'emplacement 4,0 avec une taille 2,1
message.grid(row=4, column=0, columnspan=2, sticky="ew")

# Radio
# assigne une commande au radio boutton 1
b_radio_1["command"] = lambda: mode_chiffrement()
# assigne une commande au radio boutton 2
b_radio_2["command"] = lambda: mode_dechiffrement()

# Création d'un bouton valider
bouton_valider = tk.Button(root, text="Valider")
# Place le bouton valider dans la fenetre à l'emplacement 4,0 avec une taille 2,1
bouton_valider.grid(row=6, column=0, columnspan=2, sticky="nsew")
bouton_valider["command"] = lambda: action_valider(image, radioVariable)  # Assigne une commande au bouton

# Adaptation fenêtre
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(4, weight=1)

root.mainloop()
