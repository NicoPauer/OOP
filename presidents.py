#!/usr/bin/python3

# This import only works of this way
from HistoryData import *


# Add objects to a list for made easier control all them over
presidents = [HistoryData('1° George Washington', '1789-1797'), HistoryData('2° James Adams', '1797-1801'), HistoryData('3° Thomas Jefferson', '1801-1809')]

print('The USA presidents are: \n')
for president in presidents:
 # Show data of each president
    president.show()

print('\tTHIS ONLY AN SHORT EXAMPLE TO KEEP SHORT USA PRESIDENTS LIST SOURCE CODE.\n')
