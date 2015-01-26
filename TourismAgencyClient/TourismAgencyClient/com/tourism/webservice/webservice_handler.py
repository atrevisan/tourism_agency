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

    def register_travel_pack(self, origin, destination, departure_date, arrival_date, number_of_rooms, is_promo):
        """Perform a remote method call for registering a travel pack.
        
        Parameters
        ----------
        origin : string
            The place of origin of the travel pack.

        destination : string
            The place of detination of the travel pack.

        departure_date : tuple (int, int, int)
            Date display format (day, month, year) for
            the date of departure.

        arrival_date : tuple (int, int, int)
            Date display format (day, month, year) for
            the date of arrival.

        number_of_rooms : int
            Number of rooms for this travel package.

        is_promo : boolean
            If this package is promotional.
        """

        self.client.service.registerTravelPack(origin, destination, departure_date, arrival_date, number_of_rooms, is_promo)

