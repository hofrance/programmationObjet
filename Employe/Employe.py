""""Classe Personne"""
import datetime


class Personne :
    def __init__(self,matricule,nom,prenom,dateNaisance,dateEmbauche,salaire):
        self.matricule=matricule
        self.nom=nom
        self.prenom=prenom
        self.dateNaisance=dateNaisance
        self.dateEmbauche=dateEmbauche
        self.salaire=salaire

    def getAge(self):
        return (self.dateNaisance-datetime.date)

    """"continuer
    """

        