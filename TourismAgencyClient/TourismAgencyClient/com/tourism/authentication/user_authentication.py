# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2015
#
# License: MIT

import pickle
import os

from suds.client import Client


class UserAuth():
    """Check through the webservice if user exists.
    
    Parameters
    ----------
    username : string
        Username registered on the server.

    password : string
        Password tied to the username.
    """

    def __init__(self, username, password):
        
        self.username = username
        self.password = password

    def authenticate(self):
        """Perform the remote method call to the webservice.
        
        Return
        -------
        result : boolean
            The result of the operation. If true user exists,
            otherwize user not registered.
        """

        # get the webservice url
        with open(os.getcwd() + r"\com\tourism\authentication\webservice_url.pkl", 'rb') as input:
            url = pickle.loads(input.read())

        client = Client(url)

        # call the server authenticate method
        result = client.service.authenticate(self.username, self.password)
        
        return result 