"""
By Chiegang Sape 02-03-2020 03:18

"""

from munkres import Munkres, print_matrix
 
matrix = [[10,15,13],
[5,14,16],
[11,13,14]
        ]
 
m = Munkres()
 
indexes = m.compute(matrix)
 
print_matrix(matrix)
 
print ('resultat=', indexes)
print ('coût=', sum([matrix[i[0]][i[1]] for i in indexes]))
