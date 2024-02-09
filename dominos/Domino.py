"""La classe domino"""
class Domino:
    """
    On definit la valeur avec des attributs
    definies par défaut ici zero pour A et B si c'est pas fournis

     """
    def __init__(self,A=0,B=0):
        self.A=A
        self.B=B


    """"
    Methode pour afficher les les points
    """
    def affiche_points(self):
        print("face A:{}  face B:{}".format(self.A,self.B))

    """"Methode pour caluculer la somme"""
    def valeur(self):
        return(self.A+self.B)

"""
On instanciation de  la classe domino avec deux objets
"""
d1=Domino(2,6)
d2=Domino(4,3)

#affichage du premier dominos
d1.affiche_points()