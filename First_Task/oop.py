class Citizen:
    def __init__ (self, name, surname, age, nationality, visa):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__nationality = nationality
        self.__visa = visa

    @property
    def name (self):
        return self.__name
    
    @property
    def surname (self):
        return self.__surname
    
    @property
    def age (self):
        return self.__age

    @property
    def nationality (self):
        return self.__nationality

    @property
    def visa (self):
        return self.__visa
    
    @name.setter
    def name (self, name):
        self.__name = name

    @surname.setter
    def surname (self, surname):
        self.__surname = surname

    @age.setter
    def age (self, age):
        self.__age = age

    @nationality.setter
    def nationality (self, nationality):
        self.__nationality = nationality

    @visa.setter
    def visa (self, visa):
        self.__visa = visa


class Worker (Citizen):
    def __init__ (self, name, surname, age, nationality, visa, company_name, \
            company_adress, work_number):
        Citizen.__init__ (self, name, surname, age, nationality, visa)
        self.__company_name = company_name
        self.__company_adress = company_adress
        self.__company_work_number = work_number
    
    @property
    def company_name (self):
        return self.__company_name

    @property
    def company_adress (self):
        return self.__company_adress

    @property
    def work_number (self):
        return self.__work_number

    @company_name.setter
    def company_name (self, comapny_name):
        self.__company_name = company_name

    @company_adress.setter
    def company_adress (self, comapny_adress):
        self.__company_adress = company_adress

    @work_number.setter
    def work_number (self, work_number):
        self.__work_number = work_number


class Scientist (Worker):
    def __init__ (self, name, surname, age, nationality, visa, company_name, \
            company_adress, work_number, science_area, scientist_type, articles_number):
        Worker.__init__ (self, name, surname, age, nationality, visa, company_name, \
                company_adress, work_number)    
        self.__science_area = science_area
        self.__scientist_type = scientist_type
        self.__articles_number = articles_number

    @property
    def science_area (self):
        return self.__science_area

    @property
    def scientist_type (self):
        return self.__scientist_type

    @property
    def articles_number (self):
        return self.__articles_number
    
    @science_area.setter
    def science_area (self, science_area):
        self.__science_area = science_area

    @scientist_type.setter
    def scientist_type (self, scientist_type):
        self.__scientist_type = scientist_type

    @articles_number.setter
    def articles_number (self, articles_number):
        self.__articles_number = articles_number


def main ():
    master = Scientist ("Ivan", "Ivanov", "23", "Tatar", "Russian", "RQC", "Pervomayskaya 30", "555101", "Theoretical physics", "Theorist", 4)
    for property, value in vars (master).items ():
        print (property, ":", value)
    print ("\n")

    phd = Scientist ("Alex", "Holland", "26", "American", "The USA", "Intell", "Growstreet 21A", "3121772", "Kerenel programming", \
            "Developer", 10)
    for property, value in vars (phd).items ():
        print (property, ":", value)
    print ("\n")
    
    doctor_of_science = Scientist ("Jan", "Van Bassten", "32", "Dutchman", "Netherlands", "BinckBank", "Kalverstraat 4", "88003535", \
            "Mathematical statistics", "Theorist", 21)
    for property, value in vars (doctor_of_science).items ():
        print (property, ":", value)


main ()






