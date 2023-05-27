#!/usr/bin/python3

class HistoryData():

    '''
        Manage history information of
        the humanity history. 

       NOTE: This only use strings.
    '''

    def __init__(self, n, p):

        self.name = n

        self.period = p

        self.description = ''

    def show(self):
        '''
            Show data in readable text format.
        '''
        print(self.name + ' happened ' + self.period + '...\n' + self.description)
