from helpers.CommonCape import CommonCape
from kivy.uix.screenmanager import Screen


class BaseScreenComponent(Screen, CommonCape):

    def setLoading(self, state)-> None:
        self.ids.loadingEl.active = state
    
    
