from dateutil.parser import parse

from proto21_home.data.Car import Car
from proto21_home.viewmodels.base_viewmodel import ViewModelBase
from proto21_home.viewmodels.create_event_viewmodel import CreateEventViewModel


class UpdateEventViewModel( CreateEventViewModel ):
    def __init__(self, data_dict, event_id):
        super().__init__(data_dict)
        self.event_id = event_id

    def compute_details(self):

        event_id = self.data_dict.get('id')
        if not self.event_id:
            self.errors.append("No event ID specified.")
        if self.event_id != event_id:
            self.errors.append("Event ID mismatch.")

        super().compute_details()