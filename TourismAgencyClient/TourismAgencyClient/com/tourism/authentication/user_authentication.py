# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2015
#
# License: MIT

from com.tourism.webservice.webservice_handler import WebserviceHandler

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
        """Call the webservice handler method that handles authentication.
        
        Return
        -------
        result : boolean
            The result of the operation. If true user exists,
            otherwize user not registered.
        """

        handler = WebserviceHandler()
        result = handler.authenticate(self.username, self.password)

        return result 