from app_enums.routes_enum import RoutesEnum
from components.common.base_screen.BaseScreenComponent import BaseScreenComponent
from kivy.app import App
from helpers.showMessages import ShowMessages
from kivy.uix.screenmanager import Screen

class PagesModule(BaseScreenComponent, ShowMessages):
    """This class is the parent of all pages that will be added..."""
    @property
    def root(self):
        return App.get_running_app().root
    appRoutes = RoutesEnum()
