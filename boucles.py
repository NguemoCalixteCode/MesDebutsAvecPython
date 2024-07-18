chaine_de_nombre = input("Entrez une suite de nombres séparés par des virgules: ");
liste_de_nombre = [];
somme_nombre = 0;
conteur = 0;
nombre_pairs =0;
for nombre in chaine_de_nombre.split(","):
    liste_de_nombre.append(int(nombre));
for n in liste_de_nombre:
    somme_nombre = somme_nombre + n;
moyenne_nombre = somme_nombre / len(liste_de_nombre);
for nombre in liste_de_nombre:
    if nombre > moyenne_nombre:
        conteur = conteur + 1;
    if nombre%2 == 0:
        nombre_pairs = nombre_pairs + 1;


print(f"La liste est : {liste_de_nombre} \n la somme est {somme_nombre}");
print(f"\n La moyenne est {moyenne_nombre}, \n Le nombre de nombre supérieur à la moyenne est {conteur} ")
print(f"\nLe nombre de nombre pairs est {nombre_pairs}")