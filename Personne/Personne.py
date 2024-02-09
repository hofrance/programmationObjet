""""La classe personne"""

class Personne:
    def __init__(self,nom="inconnu",prenom="inconnu",age=0,adresse="inconnu"):
        self.nom=nom
        self.prenom=prenom
        self.age=age
        self.adresse=adresse

    def decrirePersonne(self):
        print("Nom: {} ,Prenom: {}, Age:{},Adresse: {} ".format(self.nom,self.prenom,self.age,self.adresse))

    def compararerAPersonne(self,personne):
        if self.age > personne.age:
            print("{} est plus grand que {}".format(self.nom,personne.nom))
        elif self.age < personne.age:
            print("{} est plus jeune que {}".format(self.nom, personne.nom))
        else:
            print("{} et {} ont le même age".format(self.nom, personne.nom))
    def verifMajor(self):
        print("Est majeur :{} ".format(self.age>18))
        return (self.age>18)


moi=Personne("richard","hofrance",19)

moi.verifMajor()