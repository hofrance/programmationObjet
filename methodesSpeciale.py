"""Ici, nous allons serrer des vis et taper sur des clous!"""


class BoiteOutil:
    """Boite à outils."""

    def __init__(self):
        """Initialise les outils."""
        self.outils = []

    def ajoute_outil(self, outil):
        """Ajoute un outil."""
        self.outils.append(outil)

    def enleve_outil(self, outil):
        """Enleve un outil."""
        index = self.outils.index(outil)
        del self.outils[index]

    def  __repr__(self):
        """Affichage"""
        print("outils dans la boîte:")
        for outil in self.outils:
            print(outil)


class Tournevis:
    """Tournevis."""

    def __init__(self, taille=3):
        """Initialise la taille."""
        self.taille = taille

    def serrer(self, vis):
        """Serrer une vis."""
        vis.serrer()

    def desserre(self, vis):
        """Desserre une vis."""
        vis.desserre()

    def __repr__(self):
        """Affichage de l'objet."""
        return "Tournevis de taille " + str(self.taille)


class Marteau:
    """Marteau."""

    def __init__(self, couleur="rouge"):
        """Initialise la couleur."""
        self.couleur = couleur

    def peindre(self, couleur):
        """Paint le marteau."""
        self.couleur = couleur

    def planter(self, clou):
        """Enfonce un clou."""
        clou.enfoncer()

    def retirer(self, clou):
        """Enleve un clou."""
        clou.enlever()

    def __repr__(self):
        """Affichage de l'objet."""
        return "Marteau de couleur " + self.couleur


class Vis:
    """Vis."""
    MAX_DEGRE = 5

    def __init__(self):
        """Initialise son degré de serrage."""
        self.degre_serrage = 0

    def desserre(self):
        """Déserre le vis."""
        if self.degre_serrage > 0:
            self.degre_serrage -= 1

    def serrer(self):
        """Serre le vis."""
        if self.degre_serrage < self.MAX_DEGRE:
            self.degre_serrage += 1

    def __str__(self):
        """Affichage d'une forme lisible de l'objet."""
        return "Vis avec un serrage de " + str(self.degre_serrage)


class Clou:
    """Clou."""

    def __init__(self):
        """Initialise son statut "dans le mur"."""
        self.dans_mur = False

    def enfoncer(self):
        """Enfonce le clou dans un mur."""
        if not self.dans_mur:
            self.dans_mur = True

    def enlever(self):
        """Enlève le clou du mur."""
        if self.dans_mur:
            self.dans_mur = False

    def __str__(self):
        """Affichage d'une forme lisible de l'objet."""
        if self.dans_mur:
            etat_mur = "dans le mur"
        else:
            etat_mur = "hors du mur"

        return "Clou " + etat_mur


# Instanciez une boîte à outils, un tournevis, et un marteau.
marteau = Marteau()
tournevis = Tournevis()
boite = BoiteOutil()

# Placez le marteau et le tournevis dans la boîte à outils.
print("")
boite.ajoute_outil(marteau)
boite.ajoute_outil(tournevis)

# Instanciez une vis, et serrez-la avec le tournevis.
# Affichez la vis avant après avoir été serrée.
print("")
vis = Vis()
print(vis)
tournevis.serrer(vis)
print(vis)

# Instanciez un clou, puis enfoncez-le avec le marteau.
# Affichez le clou avant et après avoir été enfoncé.
print("")
clou = Clou()
print(clou)
marteau.planter(clou)
print(clou)

# --------------------------------------------------------------
# Que pouvez-vous faire d’autre avec ces classes et ces objets?

# enlever un outil
print("")
boite.__repr__()
boite.enleve_outil(marteau)
print("on a enlevé le marteau")
boite.__repr__()

# désserrer la vis
print("")
tournevis.desserre(vis)
print(vis)

# enlever le clou
print("")
marteau.retirer(clou)
print(clou)

# repeindre le marteau
print("")
print(marteau)
marteau.peindre("jaune")

print(marteau)