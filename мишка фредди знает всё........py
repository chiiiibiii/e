class Me:
    def __init__(self, name):
        self.name = name
    def eat (self,food):
        if food == 1 or food == 3:
            print("Сьогодні смачненьке")
        elif food  == 2 or food == 4:
            print("Нормальне харчування")


name = input("Як тебе звати?")
print(name, ", Обери що будеш їсти ")
name=Me(name)
for day in range(7):
    print("\n---------------------------------------\n"
         "day", day+1)
    print("1 - піцу/n"
      "2 - пюре з м'сом\n"
      "3 - бургер\n"
      "4 - салатік")
    food = int(input("введи число, що відповідає обраній справі:  "))
    name.eat(food)
