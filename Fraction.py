class Fraction:
    """
    Classe Fraction
    Permet de représenter et de faire des calculs sur des nombres rationnels
    """

    def __init__(self, numerateur = 1, denominateur = 1):
        """
        F = Fraction() : crée une fraction égale à 1
        F = Fraction(a) : crée une fonction égale à a
        F = Fraction(a,b): crée une fonction égale à a/b
        """
        a, b = numerateur, denominateur
        while b != 0:
            r = a % b
            a, b = b, r
        self.__numerateur = numerateur // a
        self.__denominateur = denominateur // a
        if self.__denominateur < 0:
            self.__denominateur *= -1
            self.__numerateur *= -1
        return None

    def __repr__(self):
        """
        Donne une représentation de l'objet "Fraction" dans la console
        """
        return "Fraction(" + str(self.__numerateur) + "," + str(self.__denominateur) + ")"

    def __str__(self):
        """
        Donne une représentation sommaire de la fraction avec print
        """
        if self.__denominateur == 1:
            return str(self.__numerateur)
        else:
            numerateur = str(self.__numerateur)
            denominateur = str(self.__denominateur)
            largeur = max(len(numerateur), len(denominateur))
            chaine = " " * (largeur - len(numerateur)) + numerateur + "\n"
            chaine += chr(8213) * largeur + "\n"
            chaine += " " * (largeur - len(denominateur)) + denominateur
            return chaine

    def numerateur(self):
        """
        Retourne le numérateur de la fraction
        """
        return self.__numerateur

    def denominateur(self):
        """
        Retourne le dénominateur de la fraction
        """
        return self.__denominateur

    def __add__(self, frac):
        """
        Retourne self + frac sous forme de fraction
        """
        if self.__denominateur == frac.denominateur():
            numerateur_resultat = self.__numerateur + frac.numerateur()
            denominateur_resultat = self.__denominateur
        else:
            numerateur_resultat = self.__numerateur * frac.denominateur() + frac.numerateur() * self.__denominateur
            denominateur_resultat = self.__denominateur * frac.denominateur()
        return Fraction(numerateur_resultat, denominateur_resultat).simplifie()

    def __sub__(self, frac):
        """
        Retourne self - frac sous forme de fraction
        """
        if self.__denominateur == frac.denominateur():
            numerateur_resultat = self.__numerateur - frac.numerateur()
            denominateur_resultat = self.__denominateur
        else:
            numerateur_resultat = self.__numerateur * frac.denominateur() - frac.numerateur() * self.__denominateur
            denominateur_resultat = self.__denominateur * frac.denominateur()
        return Fraction(numerateur_resultat, denominateur_resultat).simplifie()

    def __mul__(self, frac):
        """
        Retourne self * frac sous forme de fraction
        """
        numerateur_resultat = self.__numerateur * frac.numerateur()
        denominateur_resultat = self.__denominateur * frac.denominateur()
        return Fraction(numerateur_resultat, denominateur_resultat).simplifie()

    def __truediv__(self, frac):
        """
        Retourne self / frac sous forme de fraction
        """
        numerateur_resultat = self.__numerateur * frac.denominateur()
        denominateur_resultat = self.__denominateur * frac.numerateur()
        return Fraction(numerateur_resultat, denominateur_resultat).simplifie()

    def __pow__(self, n):
        """
        Retourne self ** n sous forme de fraction
        """
        numerateur_resultat = self.__numerateur ** n
        denominateur_resultat = self.__denominateur ** n
        return Fraction(numerateur_resultat, denominateur_resultat).simplifie()

    def __pos__(self):
        """
        Retourne +self sous forme de fraction
        """
        numerateur_resultat = self.__numerateur
        denominateur_resultat = self.__denominateur
        return Fraction(numerateur_resultat, denominateur_resultat).simplifie()

    def __neg__(self):
        """
        Retourne -self sous forme de fraction
        """
        numerateur_resultat = -self.__numerateur
        denominateur_resultat = self.__denominateur
        return Fraction(numerateur_resultat, denominateur_resultat).simplifie()

    def __abs__(self):
        """
        Retourne abs(self) sous forme de fraction
        """
        numerateur_resultat = abs(self.__numerateur)
        denominateur_resultat = abs(self.__denominateur)
        return Fraction(numerateur_resultat, denominateur_resultat).simplifie()


    def __eq__(self, frac):
        """
        Retourne self == frac
        """
        return self.simplifie().numerateur() == frac.simplifie().numerateur() and self.simplifie().denominateur() == frac.simplifie().denominateur()

    def __ne__(self, frac):
        """
        Retourne self != frac
        """
        return self.simplifie().numerateur() != frac.simplifie().numerateur() or self.simplifie().denominateur() != frac.simplifie().denominateur()

    def __lt__(self, frac):
        """
        Retourne self < frac
        """
        return self.valeur() < frac.valeur()

    def __gt__(self, frac):
        """
        Retourne self > frac
        """
        return self.valeur() > frac.valeur()

    def __le__(self, frac):
        """
        Retourne self <= frac
        """
        return self < frac or self == frac

    def __ge__(self, frac):
        """
        Retourne self >= frac
        """
        return self > frac or self == frac

    def simplifie(self):
        """
        Simplifie la fraction en fraction irréductible
        """
        a, b = self.__numerateur, self.__denominateur
        while b != 0:
            r = a % b
            a, b = b, r
        return Fraction(self.__numerateur // a, self.__denominateur // a)

    def valeur(self):
        """
        Donne la valeur numérique de la fraction
        """
        return self.__numerateur / self.__denominateur

    def __float__(self):
        """
        Retourne la valeur numérique de la fraction sous forme d'un flottant
        """
        return self.valeur()

    def floor(self):
        """
        Retourne le plus grand entier inférieur ou égal à la fraction
        """
        return int(self.valeur())

    def ceil(self):
        """
        Retourne le plus petit entier supérieur à la fraction
        """
        return int(self.valeur()) + 1

    def __int__(self):
        """
        Retourne le plus grand entier inférieur ou égal à la fraction
        """
        return self.floor()