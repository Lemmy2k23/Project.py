class Person:
    company='CKC'
    
    def _init_(self,x,y):
        self.gender = 'M'
        self.age = 20


george = Person()
John = Person()

george.company = 'mircosoft'
John.company = 'alibaba'

george.age = 55
John.age = 16

george.gender = 'undefined'
John.gender = 'M'



print('george:','\nAge:',george.age,
'\ncompany:' ,george.company, '\n'
'\nJohn:',
'\nJohn.age',John.age,
'\nJohn.company:',John.company)








































































































































































 
