class Voiture:
    def __init__(self,marque='Ford',couleur='rouge'):
        self.marque=marque
        self.couleur=couleur
        self.pilote='personne'
        self.vitesse=0

    def choix_conducteur(self,piloteName):
        self.pilote=piloteName
    def accelerer(self,taux,duree):
        if(self.pilote=='pilote'):
            print("cette voiture n'a pas de conducteur")

        else:
            self.vitesse=taux*duree
            #a = (self.vitesse > 0) ? "accelération en cours": "déceleratrion")
            if self.vitesse > 0:
                print("accelération en cours")
            else:
                print( "déceleratrion")
    def affiche_tout(self):
        print ("{} pilotée par {},  vitesse= {} m/s".format(self.marque,self.pilote,self.vitesse))


a1=Voiture()
a1.affiche_tout()

