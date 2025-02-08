import csv

def csv1(chemin_fichier, separateur):
    tableau = []
    with open(chemin_fichier, newline='', encoding='utf-8') as fichier:
        lecteur = csv.reader(fichier, delimiter=separateur)
        for ligne in lecteur:
            tableau.append(ligne)
    return tableau

# Exemple d'utilisation
print("\n==== Exemple fonction csv1() ====")
tab = csv1('data/exemple.csv', ',')
print(tab)

# Questions préliminaires

# 1. Un fichier texte contenant des données tabulaires où chaque ligne représente une entrée et les valeurs sont séparées par un délimiteur (le plus souvent une virgule).
# 2. Ils se trouvent sur la première ligne du fichier CSV. En Python, descripteurs = tab[0].
# 3. annee_ligne4 = tab[4][0]  # '2021'
# 4. prix_ligne4 = float(tab[4][1])  # 56.3

def tranche(chaine, d, f):
    return chaine[d:f]

# Exemple d'utilisation
print("\n==== Exemple fonction tranche() ====")
print(tranche("bonjour à vous tous", 10, 14))  # Résultat : 'vous'

def indices(chaine, car):
    return [i for i, c in enumerate(chaine) if c == car]

# Exemple d'utilisation
print("\n==== Exemple fonction indices() ====")
print(indices("bonjour à vous tous", 'o'))  # Résultat : [1, 4, 11, 16]

def partage(chaine, car):
    return chaine.split(car)

# Exemple d'utilisation
print("\n==== Exemple fonction partage() ====")
print(partage("bonjour à vous tous", 'o'))  # Résultat : ['b', 'nj', 'ur à v', 'us t', 'us']
print(partage(",chp2,chp3,,chp5,,,", ','))  # Résultat : ['', 'chp2', 'chp3', '', 'chp5', '', '', '']

