moy,iteration, number =0.0,0, input().split(',') #input par l'utilisateur trasforme l'input en list séparer par les virgule et le resultat sera dans moy
for i, ha in enumerate (number):   #parcours la liste
    if number[i].isdigit():        #verifie si il sagit d'un chiffre
        moy += int (number[i])     #additionne
        iteration += 1             #prend le nombre de nombre dans la liste
moy /= iteration                   #calcul la moyenne
print (moy)                        #affiche la moyenne