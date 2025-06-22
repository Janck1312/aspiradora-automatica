from app_enums.events_enum import EventsEnum
from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty


class onEditRecord(EventDispatcher):
    """This class define the edit record event"""
    delete_record = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        self.register_event_type(EventsEnum.on_edit_record)
        super(onEditRecord, self).__init__(**kwargs)

    def on_edit_record(self, *args):
        """Default event method"""
        pass
