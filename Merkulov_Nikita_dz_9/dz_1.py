from time import sleep


class TrafficLight:
    color_ = 'светофор выключен'

    def running(self):
        try:
            while True:
                print('Красный')
                sleep(7)
                print('Жёлтый')
                sleep(2)
                print('Зелёный')
                sleep(10)
                print('Жёлтый')
                sleep(2)
        except KeyboardInterrupt:
            print('Светофор сломался...')


a = TrafficLight()
a.running()
