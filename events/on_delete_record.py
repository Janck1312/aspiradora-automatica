from app_enums.events_enum import EventsEnum
from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty

class onDeleteRecord(EventDispatcher):
    """This class define the delete record event"""
    delete_record = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        self.register_event_type(EventsEnum.on_delete_record)
        super(onDeleteRecord, self).__init__(**kwargs)

    def on_delete_record(self, *args):
        """Default event method"""
        pass