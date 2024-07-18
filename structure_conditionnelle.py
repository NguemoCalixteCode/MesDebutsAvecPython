nombre_a_gauche = 8;
nombre_a_droite = 6;
symbole = "/";
resultat = 0;

if isinstance(nombre_a_gauche, int) and isinstance(nombre_a_droite, int):
    match symbole:
        case "+":
            resultat = nombre_a_droite + nombre_a_gauche
        case "-":
            resultat = nombre_a_droite - nombre_a_gauche
        case "*":
            resultat = nombre_a_droite * nombre_a_gauche
        case "/":
            if nombre_a_gauche != 0:
                resultat = nombre_a_droite / nombre_a_gauche
            else:
                print("Division par 0 impossible");
        case _:
            print("Erreur : symbole inconnu");
    print(resultat);
    
else:
    print("Erreur");