#!/usr/bin/env python
import numpy as np


#embed, numpy,enumerate
def print_list(l):
    print l

def sort_manual(shops):

    shops_sorted = []

    for key,value in shops.iteritems():
        shops_sorted.append([key,value])


    for i in range(len(shops)):
        j=i
        while (j<len(shops)):
            if shops_sorted[i][1]<shops_sorted[j][1]:
                temp = shops_sorted[i]
                shops_sorted[i] = shops_sorted[j]
                shops_sorted[j] = temp
            j+=1
        i+=1

    print 'Manual sorting result: '
    print_list(shops_sorted)

def sort_python(shops):

    shops_sorted = []

    for key,value in shops.iteritems():
        shops_sorted.append([key,value])

    shops_sorted=sorted(shops_sorted,key=lambda l:l[1], reverse=True)

    #TODO: Here implement sorting using python's built in sorting functions

    print 'Python sorting result: '
    print_list(shops_sorted)

def sort_numpy(shops):
    
    shops_sorted = []
    shops_sorted=np.array([x for x in shops.items()])
    shops_sorted = shops_sorted[np.argsort(shops.values(), axis=0), :][::-1].tolist()

    print 'Numpy sorting result: '
    print_list(shops_sorted)

def main():

    shops = {}
    shops['21st Street'] = 0.9
    shops['Voluto'] = 0.6
    shops['Coffee Tree'] = 0.45
    shops['Tazza D\' Oro'] = 0.75
    shops['Espresso a Mano'] = 0.95
    shops['Crazy Mocha'] = 0.35
    shops['Commonplace'] = 0.5

    sort_manual(shops)
    sort_python(shops)
    sort_numpy(shops)
    

if __name__ == "__main__":
    main()
