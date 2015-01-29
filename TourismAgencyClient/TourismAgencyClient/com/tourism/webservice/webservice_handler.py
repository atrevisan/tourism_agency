# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2015
#
# License: MIT

import os
from suds.client import Client
import pickle

class WebserviceHandler():
    """This class acts as an interface for the webservice calls."""

    def __init__(self):

        # get the webservice url
        with open(os.getcwd() + r"\com\tourism\webservice\webservice_url.pkl", 'rb') as input:
            url = pickle.loads(input.read())

        self.client = Client(url)

    def authenticate(self, username, password):
        """Perform the authentication remote method call to the webservice.
        
        Parameters
        ----------
        username : string
            Username registered on the server.

        password : string
            Password tied to the username.

        Return
        -------
        result : boolean
            The result of the operation. If true user exists,
            otherwize user not registered.
        """

        # call the server authenticate method
        result = self.client.service.authenticate(username, password)

        return result

    def register_travel_pack(self, origin, destination, departure_date, arrival_date, number_of_rooms, is_promo, guest_ages):
        """Perform a remote method call for registering a travel pack.
        
        Parameters
        ----------
        origin : string
            The place of origin of the travel pack.

        destination : string
            The place of detination of the travel pack.

        departure_date : tuple (int, int, int)
            Date display format (year, month, day) for
            the date of departure.

        arrival_date : tuple (int, int, int)
            Date display format (year, month, day) for
            the date of arrival.

        number_of_rooms : int
            Number of rooms for this travel package.

        is_promo : boolean
            If this package is promotional.

        guest_ages : list of int
            The ages of the maximun number of guests
            for this travel package.
        """

        self.client.service.registerTravelPack(origin, destination, departure_date[0], departure_date[1], departure_date[2],
                                               arrival_date[0], arrival_date[1], arrival_date[2], number_of_rooms, is_promo,
                                               guest_ages)

    def get_travel_packs(self):
        """Get all the available travel packs for purchase.
        
        Return
        -------
        travel_packs : list of TravelPacks
            Objects that represent a travel pack.
        """

        travel_packs = self.client.service.getTravelPacks()
        return travel_packs
