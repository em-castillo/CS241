class Date:

    def __init__(self):
        self.day = 1
        self.month = 1
        self.year = 2000

    def prompt(self):
        self.day = int(input("Day: "))
        self.month = int(input("Month: "))
        self.year = int(input("Year: "))

    def display(self):
        print(f"{self.month}/{self.day}/{self.year}")


# test = Date()
# test.prompt()
# test.display()

