""""Classe compteBanquaire"""
class CompteBanquaire:

    """Constructeur prend deux parametre dont Dupond et 1000 par defaut si aucun n'est fournis lors de l'instanciation"""
    def __init__(self,nom="Dupond",solde=1000):
        self.nom=nom
        self.solde=solde

    def depot(self,somme):
        self.solde= self.solde+somme

    def retrait(self,somme):
        #verification
        if(self.solde<somme):
            print("Solde insuffisant,retrait nn effectué")

        self.solde=self.solde-somme
        print("retrait effectué")
    def affiche(self):
        print("Le solde du compte bancaire de {} est de {}".format(self.nom,self.solde))



monCompte=CompteBanquaire()
monCompte.affiche()