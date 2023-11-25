class Human_work():
    def __init__(self,name,age,job):
        # information
        self.name = name
        self.age = age
        self.job = job

        #work rate
        self.day_per_week = 5
        self.day_per_month = 20
        #add class salary
        self.salary = Salary()
        self.gender = Gender()
    
    def adddayworkforweek(self,day):
        #add day work for week 
        if day <= self.day_per_week:
            self.day_per_week = day
            print('Awsome man i will engage this Promotion !!')
        else:
            print('Oh Damm !! i think that lots of work time')

    def adddayworkformonth(self,day):
        #add day work for week
        if day <= self.day_per_month:
            self.day_per_month = day
            print('Awsome man i will engage this Promotion !!')
        else:
            print('Oh Damm !! i think that lots of  work time')

    def show_salary(self,add):
        self.salary.add_salary(add)
        return self.salary
    
    def show_gender(self,gender):
        self.gender.ability(gender)
        

class Salary():
    def __init__(self,salary=500):
        self.salary = salary

    def add_salary(self,add):
        self.salary += add
        print('add salary')


class Gender():
    def __init__(self,man='man',woman='woman'):
        self.man = man
        self.woman = woman

    def ability(self,gender):
        if gender == 'man':
            print('strong')
        else:
            print('weak')


def showallin(*number):
    for i in number:
        if i>200:
            print('Damm!!')
    return i















   















