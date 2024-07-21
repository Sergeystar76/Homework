class Vehicle:
    COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner:str , __model:str, __color:str, __engine_power:int):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(__model):
        return __model
    def get_horsepower(__engine_power):
        return __engine_power
    def get_color(__color):
        return
    def print_info(self):
        print(f"Модель: {self.__model}")
        print(f"Мощность двигателя: {self.__engine_power}")
        print(f"Цвет:  {self.__color}")
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color:str):
        self.new_color = new_color

        for i in self.COLOR_VARIANTS:
            if self.new_color == i or self.new_color == i.upper():
                self.__color = self.new_color

        if self.new_color != self.__color:
            # else:
            print(f'Нельзя сменить цвет на {new_color}.')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5



vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
