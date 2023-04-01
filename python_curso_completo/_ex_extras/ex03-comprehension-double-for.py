mat = [[2,3,4],
     [7,9,10],
     [12,13,14]]

pair_mat = [el for list_el in mat
            for el in list_el
            if el % 2 == 0]

print(pair_mat)