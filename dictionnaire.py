fruits ={
    "pomme":"rouge",
    "banane":"jaune",
    "orange":"orange",
};

fruits ["kiwi"] = "vert"

couleur_banane = fruits["banane"];

fruits["pomme"] = "vert"
print(couleur_banane)

fruits.pop("orange");
print(fruits)