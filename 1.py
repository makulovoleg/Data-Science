from time import sleep
class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']
    def rinning(self):
        i = 0
        while i != 3:
            print(TrafficLight.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            i = i + 1
t = TrafficLight()
t.rinning()