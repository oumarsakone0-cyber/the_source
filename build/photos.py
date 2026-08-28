# -*- coding: utf-8 -*-
"""
Photographies du site.

Toutes les images sont des photographies du parc et des véhicules de
THE SOURCE TRANSPORT, hébergées dans assets/img/photos/. Le site ne dépend
d'aucune banque d'images ni d'aucun service extérieur.

Chaque clé du dictionnaire PHOTOS correspond au fichier
assets/img/photos/<clé>.jpg. Pour changer une image : écrasez le fichier en
gardant son nom. Pour en ajouter une : inscrivez la clé ici et déposez le .jpg.

La valeur est le texte alternatif — il est lu par Google et par les lecteurs
d'écran, donc il décrit ce que l'on voit, pas ce que la photo illustre.
"""

DIR = "assets/img/photos/"

PHOTOS = {
    # --- bannières et panneaux ---
    "hero":         "La flotte THE SOURCE TRANSPORT alignée sur le parc",
    "partenaire":   "Tracteurs MAN et Renault stationnés sur le parc d'Abidjan",
    "parc":         "Vue d'ensemble du parc de véhicules de l'entreprise",
    "equipe":       "L'équipe d'exploitation et les remorques plateaux sur le parc",

    # --- prestations ---
    "lourd":        "Tracteur DAF attelé à une benne, prêt au départ",
    "vente":        "Véhicules disponibles à la vente et à la location sur le parc",
    "vtc":          "Véhicules de tourisme mis à disposition avec chauffeur",
    "international":"Tracteurs et semi-remorque citerne en manœuvre vers la sortie",
    "leger":        "Pickups et véhicules utilitaires du parc",

    # --- matériels ---
    "benne":        "Semi-remorques bennes prêtes pour le transport de matériaux",
    "citerne":      "Tracteurs Renault et semi-remorque citerne sur le parc",
    "cabines":      "Cabines de tracteurs Renault alignées avant affectation",
    "iveco":        "Tracteurs IVECO du parc THE SOURCE TRANSPORT",
}

# Emplacements qui attendent encore une photo dédiée : ils réutilisent
# provisoirement une image existante. Remplacer le fichier suffit.
EN_ATTENTE = ("vente", "vtc", "leger")


def url(key, w=1200, h=None, q=72):
    """Chemin de l'image. w/h ne servent plus qu'à documenter l'usage."""
    if key not in PHOTOS:
        raise KeyError("Photo inconnue : %r. Clés valides : %s"
                       % (key, ", ".join(sorted(PHOTOS))))
    return DIR + key + ".jpg"


def alt(key):
    return PHOTOS[key]


def img(key, w=1200, h=None, cls="", sizes="100vw", eager=False, ratio=None):
    """Balise <img> complète, avec chargement différé hors de l'écran."""
    loading = 'loading="eager" fetchpriority="high"' if eager else 'loading="lazy"'
    style = f' style="aspect-ratio:{ratio}"' if ratio else ''
    return (f'<img src="{url(key)}" alt="{alt(key)}" class="{cls}"{style} '
            f'{loading} decoding="async">')


def credits_html():
    """Aucune photo de banque d'images n'est utilisée."""
    return ""
