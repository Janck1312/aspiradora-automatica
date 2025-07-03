from kivy.properties import NumericProperty
from kivy.graphics import Color, Line
from kivy.uix.widget import Widget

class CircularBattery(Widget):
    value = NumericProperty(0)  # Porcentaje de batería (0-100)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(pos=self.update_canvas, size=self.update_canvas, value=self.update_canvas)

    def update_canvas(self, *args):
        self.canvas.clear()
        with self.canvas:
            # Fondo del círculo
            Color(0.9, 0.9, 0.9, 1)  # Gris claro
            Line(circle=(self.center_x, self.center_y, min(self.size) / 2 - 5), width=2)

            # Nivel de batería (relleno)
            if self.value > 0:
                if self.value > 50:
                    Color(0, 0.7, 0, 1)  # Verde
                elif self.value > 20:
                    Color(1, 0.7, 0, 1)  # Amarillo
                else:
                    Color(1, 0, 0, 1)  # Rojo

                Line(
                    circle=(
                        self.center_x,
                        self.center_y,
                        min(self.size) / 2 - 5,
                        0,
                        self.value * 3.6  # Convertir % a grados (360°)
                    ),
                    width=10
                )
