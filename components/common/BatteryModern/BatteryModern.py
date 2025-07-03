import random

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.properties import NumericProperty, ColorProperty, BooleanProperty
from kivy.uix.widget import Widget

class BatteryModern(Widget):
    percent = NumericProperty(75)
    charging = BooleanProperty(False)
    fill_color = ColorProperty([0.2, 0.8, 0.2, 1])  # Verde por defecto

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update_colors()
        #Clock.schedule_interval(self.simulate_battery, 2)

    def update_colors(self):
        # Actualiza colores según porcentaje
        if self.percent > 70:
            self.fill_color = [0.2, 0.8, 0.2, 1]  # Verde
        elif self.percent > 30:
            self.fill_color = [1, 0.8, 0.2, 1]  # Amarillo
        else:
            self.fill_color = [1, 0.2, 0.2, 1]  # Rojo

    def simulate_battery(self, dt):
        # Simular carga/descarga
        if self.charging:
            self.percent = min(100, self.percent + 5)
        else:
            self.percent = max(0, self.percent - random.randint(2, 8))

        # Cambiar estado de carga aleatoriamente
        if random.random() < 0.2:
            self.charging = not self.charging

        self.update_colors()
        Animation(duration=0.5).start(self)
