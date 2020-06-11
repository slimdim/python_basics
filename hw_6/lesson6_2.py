# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def concreate_mass(self, thickness, sq_m_mass):
        """Рассчёт массы асфальта в тоннах

        thickness -- толщина асфальта в см
        sq_m_mass -- масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см"""
        return self._width * self._length * thickness * sq_m_mass / 1000


my_road = Road(5000, 20)
print(f'Вес дороги: {my_road.concreate_mass(5, 25)} т.')