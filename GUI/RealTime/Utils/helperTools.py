def configureMultipleRows(self, quantity, uniform = None):
    for i in range(0, quantity):
        self.rowconfigure(i, weight = 1, uniform = uniform)
        
def configureMultipleColumns(self, quantity, uniform = None):
    for i in range(0, quantity):
        self.columnconfigure(i, weight = 1, uniform = uniform)