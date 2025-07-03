from kivy.properties import StringProperty, NumericProperty

from kivy.clock import Clock
from pages.PagesModule import PagesModule
from pages.dashboard.DashboardService import DashboardService

class Dashboard(PagesModule):
    dashboardService = DashboardService()
    powerState = "false"
    buttonLabel = StringProperty("Encender")

    event_battery = None
    batteryPercent = NumericProperty(100)

    event_cronometer = None
    tiempo = StringProperty("0h 0min 0seg")
    is_cronometer_running = False
    seconds = NumericProperty(0)

    rest_battery_seconds = 3600
    rest_tiempo = StringProperty("1h 0min")

    distance_traveled = NumericProperty(0)
    distance_traveled_display = StringProperty("0 mts")

    def toggle_power(self):
        self.powerState = "true" if self.powerState == "false" else "false"
        self.buttonLabel = "Encender" if self.powerState == "false" else "Apagar"
        self.dashboardService.toggle_machine_power_state(self.powerState)
        if self.powerState == 'true':
            self.on_cronometer_start()
            self.start_calc_distance_traveled()
            self.start_calc_battery_percent()
        else:
            self.on_cronometer_stop()
            self.stop_calc_distance_traveled()
            self.stop_calc_battery_percent()

    def calc_battery_percent(self, dt):
        self.batteryPercent -= 1
        self.rest_battery_seconds -= 60
        hours = int(self.rest_battery_seconds / 3600)
        minutes = int(self.rest_battery_seconds / 60)
        seconds = int(self.rest_battery_seconds % 60)
        self.rest_tiempo = f"{hours}h {minutes}min"

    """Se ejecuta al cargar la vista"""
    def load_machine_state(self):
        self.dashboardService.load_machine_power_state()

    """Se ejecuta al dejar la vista"""
    def stop_calc_battery_percent(self):
        Clock.unschedule(self.calc_battery_percent)

    def start_calc_battery_percent(self):
        Clock.schedule_interval(self.calc_battery_percent, 60)

    def on_cronometer_start(self):
        self.event_cronometer = Clock.schedule_interval(self.update_cronometer, 1)

    def on_cronometer_stop(self):
        self.event_cronometer.cancel()

    def update_cronometer(self, dt:int|float):
        self.seconds += dt
        hours = int(self.seconds / 3600)
        minutes = int(self.seconds / 60)
        seconds = int(self.seconds % 60)
        self.tiempo = f"{hours}h {minutes}min {seconds}seg"

    def start_calc_distance_traveled(self):
        Clock.schedule_interval(self.update_calc_distance_traveled, 1)

    def stop_calc_distance_traveled(self):
        Clock.unschedule(self.update_calc_distance_traveled)

    def update_calc_distance_traveled(self, dt:int | float):
        self.distance_traveled += 0.20 #0.20 mts/seg
        self.distance_traveled_display = f"{self.distance_traveled} mts"