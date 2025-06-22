from app_enums.events_enum import EventsEnum
from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty


class onAddProductToKart(EventDispatcher):
    """This class define the add prd to kart event"""
    delete_record = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        self.register_event_type(EventsEnum.on_add_prd_to_kart)
        super(onAddProductToKart, self).__init__(**kwargs)

    def on_add_prd_to_kart(self, *args):
        """Default event method"""
        pass
