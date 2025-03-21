# Naruszenie zasady DIP
from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class Light(Device):
    def turn_on(self):
        print("Light is on")

    def turn_off(self):
        print("Light is off")


class Fan(Device):
    def turn_on(self):
        print("Fan is spinning")

    def turn_off(self):
        print("Fan is stopped")


class Button:
    def __init__(self, device: Device):
        self.device = device

    def press(self):
        self.device.turn_on()


# Usage
light = Light()
light_button = Button(light)
fan = Fan()
fan_button = Button(fan)

light_button.press()
fan_button.press()