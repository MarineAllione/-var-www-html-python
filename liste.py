# coding: utf-8

maliste = [10, 18, 14, 20, 12, 16]

def minMaxMoy(liste):

       #Initialisation
       # mini = 0
       # maxi = 0
       # moyenne = 0
       mini, maxi, somme = liste[0], liste[0], 0.0 #liste[0]

       #Boucle sur chaque élément de la liste 
       for i in liste:
            if i < mini:
                   mini = i
            if i > maxi:
                   maxi = i
            somme += i
        
       #Calcul de la moyenne
       moyenne = somme / len(liste) 

       #Retourne le resultat      
       return (mini, maxi, moyenne)

resultat = minMaxMoy(maliste)
print(resultat)
