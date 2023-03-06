from flightapp.models import AirlineCompany 
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

airline_handler = logging.FileHandler('airline.log')
airline_handler.setFormatter(formatter)

logger.addHandler(airline_handler)


class AirlineDal():
    def __init__(self):
        super().__init__()


    def get_all_airlines(self):
        airlines = AirlineCompany.objects.all()
        logger.info('added')
        return airlines
    
