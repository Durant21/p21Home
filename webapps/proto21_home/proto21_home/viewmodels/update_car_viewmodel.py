from dateutil.parser import parse

from proto21_home.data.Car import Car
from proto21_home.viewmodels.base_viewmodel import ViewModelBase
from proto21_home.viewmodels.create_car_viewmodel import CreateCarViewModel


class UpdateCarViewModel( CreateCarViewModel ):
    def __init__(self, data_dict, car_id):
        super().__init__(data_dict)
        self.car_id = car_id

    def compute_details(self):

        car_id = self.data_dict.get('id')
        if not self.car_id:
            self.errors.append("No car ID specified.")
        if self.car_id != car_id:
            self.errors.append("Car ID mismatch.")

        super().compute_details()