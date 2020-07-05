"""
By Chiegang Sape 01-03-2020 23:18

Instructions:
Fonctions d'appel dans cet ordre :
    problème = gen_matrix(v,c)
    contraindre(problème, chaîne)
    obj(problème, chaîne de caractères)
    maxz(problème)
gen_matrix() produit une matrice à laquelle on donne des contraintes et une fonction objective pour maximiser ou minimiser.
    Elle prend var (nombre de variables) et cons (nombre de contraintes) comme paramètres.
    gen_matrix(2,3) va créer une matrice 4x7 par conception.
contraint() contrainte du problème. Il prend le problème comme premier argument et une chaîne comme second. La chaîne doit être
    saisi sous la forme 1,2,G,10 signifiant 1(x1) + 2(x2) >= 10.
    Utilisez "L" pour <= au lieu de "G".
N'utilisez obj() qu'après avoir saisi toutes les contraintes, sous la forme 1,2,0 signifiant 1(x1) +2(x2) +0
    Le dernier terme est toujours réservé à une constante et le 0 ne peut être omis.
Utilisez maxz() pour résoudre un problème de maximisation LP. Utilisez minz() pour résoudre un problème de minimisation.
Divulgation -- la fonction pivot(), sous-composante de maxz() et minz(), a quelques bogues. Jusqu'à présent, ceux-ci ne se sont produits que lorsque
    minz() a été appelé.
"""

import numpy as np

# génère une matrice vide de taille adéquate pour les variables et les contraintes.
def gen_matrix(var,cons):
    tab = np.zeros((cons+1, var+cons+2))
    return tab

# vérifie dans la colonne la plus à droite les valeurs négatives AU-DESSUS de la dernière ligne. 
# Si des valeurs négatives existent, un autre pivot est nécessaire.
def next_round_r(table):
    m = min(table[:-1,-1])
    if m>= 0:
        return False
    else:
        return True

# vérifie que la ligne inférieure, à l'exclusion de la dernière colonne, pour les valeurs négatives. 
# Si des valeurs négatives existent, un autre pivot est nécessaire.
def next_round(table):
    lr = len(table[:,0])
    m = min(table[lr-1,:-1])
    if m>=0:
        return False
    else:
        return True

# Semblable à la fonction next_round_r, 
# mais renvoie l'indice de ligne de l'élément négatif dans la colonne la plus à droite
def find_neg_r(table):
    # lc = number of columns, lr = number of rows
    lc = len(table[0,:])
    # search every row (excluding last row) in final column for min value
    m = min(table[:-1,lc-1])
    if m<=0:
        # n = row index of m location
        n = np.where(table[:-1,lc-1] == m)[0][0]
    else:
        n = None
    return n

# renvoie l'index de la colonne de l'élément négatif dans la ligne du bas
def find_neg(table):
    lr = len(table[:,0])
    m = min(table[lr-1,:-1])
    if m<=0:
        # n = row index for m
        n = np.where(table[lr-1,:-1] == m)[0][0]
    else:
        n = None
    return n

# localise l'élément pivot dans le tableau pour enlever l'élément négatif de la colonne la plus à droite.
def loc_piv_r(table):
        total = []
        # r = row index of negative entry
        r = find_neg_r(table)
        # finds all elements in row, r, excluding final column
        row = table[r,:-1]
        # finds minimum value in row (excluding the last column)
        m = min(row)
        # c = column index for minimum entry in row
        c = np.where(row == m)[0][0]
        # all elements in column
        col = table[:-1,c]
        # need to go through this column to find smallest positive ratio
        for i, b in zip(col,table[:-1,-1]):
            # i cannot equal 0 and b/i must be positive.
            if i**2>0 and b/i>0:
                total.append(b/i)
            else:
                # placeholder for elements that did not satisfy the above requirements. Otherwise, our index number would be faulty.
                total.append(0)
        element = max(total)
        for t in total:
            if t > 0 and t < element:
                element = t
            else:
                continue

        index = total.index(element)
        return [index,c]
# processus similaire, renvoie un élément de tableau spécifique sur lequel il faut pivoter.
def loc_piv(table):
    if next_round(table):
        total = []
        n = find_neg(table)
        for i,b in zip(table[:-1,n],table[:-1,-1]):
            if i**2>0 and b/i>0:
                total.append(b/i)
            else:
                # placeholder for elements that did not satisfy the above requirements. Otherwise, our index number would be faulty.
                total.append(0)
        element = max(total)
        for t in total:
            if t > 0 and t < element:
                element = t
            else:
                continue

        index = total.index(element)
        return [index,n]

# Saisit une chaîne de caractères et renvoie une liste de numéros à classer dans un tableau
def convert(eq):
    eq = eq.split(',')
    if 'G' in eq:
        g = eq.index('G')
        del eq[g]
        eq = [float(i)*-1 for i in eq]
        return eq
    if 'L' in eq:
        l = eq.index('L')
        del eq[l]
        eq = [float(i) for i in eq]
        return eq

# La dernière ligne du tablue dans un problème de minimum est l'opposé d'un problème de maximisation, 
# les éléments sont donc multipliés par (-1)
def convert_min(table):
    table[-1,:-2] = [-1*i for i in table[-1,:-2]]
    table[-1,-1] = -1*table[-1,-1]
    return table

# génère x1,x2,...xn pour le nombre variable de variables.
def gen_var(table):
    lc = len(table[0,:])
    lr = len(table[:,0])
    var = lc - lr -1
    v = []
    for i in range(var):
        v.append('x'+str(i+1))
    return v

# fait pivoter le tableau de telle sorte que les éléments négatifs soient éliminés de la dernière ligne 
# et de la dernière colonne
def pivot(row,col,table):
    # number of rows
    lr = len(table[:,0])
    # number of columns
    lc = len(table[0,:])
    t = np.zeros((lr,lc))
    pr = table[row,:]
    if table[row,col]**2>0: #new
        e = 1/table[row,col]
        r = pr*e
        for i in range(len(table[:,col])):
            k = table[i,:]
            c = table[i,col]
            if list(k) == list(pr):
                continue
            else:
                t[i,:] = list(k-r*c)
        t[row,:] = list(r)
        return t
    else:
        print('Cannot pivot on this element.')

# vérifie s'il y a de la place dans la matrice pour ajouter une autre contrainte
def add_cons(table):
    lr = len(table[:,0])
    # want to know IF at least 2 rows of all zero elements exist
    empty = []
    # iterate through each row
    for i in range(lr):
        total = 0
        for j in table[i,:]:
            # use squared value so (-x) and (+x) don't cancel each other out
            total += j**2
        if total == 0:
            # append zero to list ONLY if all elements in a row are zero
            empty.append(total)
    # There are at least 2 rows with all zero elements if the following is true
    if len(empty)>1:
        return True
    else:
        return False

# ajoute une contrainte à la matrice
def constrain(table,eq):
    if add_cons(table) == True:
        lc = len(table[0,:])
        lr = len(table[:,0])
        var = lc - lr -1
        # set up counter to iterate through the total length of rows
        j = 0
        while j < lr:
            # Iterate by row
            row_check = table[j,:]
            # total will be sum of entries in row
            total = 0
            # Find first row with all 0 entries
            for i in row_check:
                total += float(i**2)
            if total == 0:
                # We've found the first row with all zero entries
                row = row_check
                break
            j +=1

        eq = convert(eq)
        i = 0
        # iterate through all terms in the constraint function, excluding the last
        while i<len(eq)-1:
            # assign row values according to the equation
            row[i] = eq[i]
            i +=1
        #row[len(eq)-1] = 1
        row[-1] = eq[-1]

        # add slack variable according to location in tableau.
        row[var+j] = 1
    else:
        print('Cannot add another constraint.')

# des vérifications pour déterminer si une fonction objective peut être ajoutée à la matrice
def add_obj(table):
    lr = len(table[:,0])
    # want to know IF exactly one row of all zero elements exist
    empty = []
    # iterate through each row
    for i in range(lr):
        total = 0
        for j in table[i,:]:
            # use squared value so (-x) and (+x) don't cancel each other out
            total += j**2
        if total == 0:
            # append zero to list ONLY if all elements in a row are zero
            empty.append(total)
    # There is exactly one row with all zero elements if the following is true
    if len(empty)==1:
        return True
    else:
        return False

# ajouter la fonction objective à la matrice
def obj(table,eq):
    if add_obj(table)==True:
        eq = [float(i) for i in eq.split(',')]
        lr = len(table[:,0])
        row = table[lr-1,:]
        i = 0
    # iterate through all terms in the constraint function, excluding the last
        while i<len(eq)-1:
            # assign row values according to the equation
            row[i] = eq[i]*-1
            i +=1
        row[-2] = 1
        row[-1] = eq[-1]
    else:
        print('You must finish adding constraints before the objective function can be added.')

# résout le problème de maximisation pour une solution optimale, renvoie le dictionnaire avec les clés x1,x2...xn et max.
def maxz(table, output='summary'):
    while next_round_r(table)==True:
        table = pivot(loc_piv_r(table)[0],loc_piv_r(table)[1],table)
    while next_round(table)==True:
        table = pivot(loc_piv(table)[0],loc_piv(table)[1],table)

    lc = len(table[0,:])
    lr = len(table[:,0])
    var = lc - lr -1
    i = 0
    val = {}
    for i in range(var):
        col = table[:,i]
        s = sum(col)
        m = max(col)
        if float(s) == float(m):
            loc = np.where(col == m)[0][0]
            val[gen_var(table)[i]] = table[loc,-1]
        else:
            val[gen_var(table)[i]] = 0
    val['max'] = table[-1,-1]
    for k,v in val.items():
        val[k] = round(v,6)
    if output == 'table':
        return table
    else:
        return val

# résout les problèmes de minimisation pour une solution optimale, renvoie le dictionnaire avec les clés x1,x2...xn et min.
def minz(table, output='summary'):
    table = convert_min(table)

    while next_round_r(table)==True:
        table = pivot(loc_piv_r(table)[0],loc_piv_r(table)[1],table)
    while next_round(table)==True:
        table = pivot(loc_piv(table)[0],loc_piv(table)[1],table)

    lc = len(table[0,:])
    lr = len(table[:,0])
    var = lc - lr -1
    i = 0
    val = {}
    for i in range(var):
        col = table[:,i]
        s = sum(col)
        m = max(col)
        if float(s) == float(m):
            loc = np.where(col == m)[0][0]
            val[gen_var(table)[i]] = table[loc,-1]
        else:
            val[gen_var(table)[i]] = 0
    val['min'] = table[-1,-1]*-1
    for k,v in val.items():
        val[k] = round(v,6)
    if output == 'table':
        return table
    else:
        return val

if __name__ == "__main__":

    m = gen_matrix(2,3)
    constrain(m,'1,-1,L,14')
    constrain(m,'2,3,G,5')
    constrain(m,'0,1,L,5')
    obj(m,'8,-5,14')
    print(maxz(m))

