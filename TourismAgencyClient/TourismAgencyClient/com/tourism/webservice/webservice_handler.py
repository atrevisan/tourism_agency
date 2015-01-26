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

    def register_travel_pack(self, origin, destination, departure_date, arrival_date, number_of_rooms):
        """"""

        self.client.register_travel_pack(origin, destination, departure_date, arrival_date, number_of_rooms)

