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

    def buy_travel_package(self,
                           credit_card_number,
                           number_of_installments,
                           chosen_package_id):
        """Request a package purchase.
        
        The client credit card number will be checked on the server
        and if it is everything ok it will perform the purchase, ie:
        remove the package from the server.

        Parameters
        ----------
        credit_card_number : int
            The credit card of the customer.

        number_of_installments : int
            The total number of payments for this
            touristic travel package.

        chosen_package_id : int
            A single sequencial identifier that
            makes possible locate this package on 
            the server.

        Returns
        --------
        result : boolean
            True if the operation succeded, False otherwize.
        """

        result = self.client.service.buyTravelPackage(credit_card_number,
                                                      number_of_installments,
                                                      chosen_package_id)

        return result

    def register_plane_ticket(self,
                              origin, 
                              destination, 
                              departure_date, 
                              arrival_date, 
                              number_of_rooms, 
                              only_departure,
                              guest_ages):
        """Perform a remote method call for registering a plane ticket.
        
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

        only_departure : boolean
            If this plane ticket is only for departure
            or is round trip.

        guest_ages : list of int
            The ages of the maximun number of guests
            for this travel package.
        """

        self.client.service.registerPlaneTicket(origin, destination, departure_date[0], departure_date[1], departure_date[2],
                                               arrival_date[0], arrival_date[1], arrival_date[2], number_of_rooms, only_departure,
                                               guest_ages)

    def get_plane_tickets(self):
        """Get all the available plane tickets for purchase.
        
        Return
        -------
        plane_tickets : list of PlaneTicket
            Objects that represent a plane ticket.
        """

        plane_tickets = self.client.service.getPlaneTickets()
        return plane_tickets

    def buy_plane_ticket(self,
                         credit_card_number,
                         number_of_installments,
                         chosen_plane_ticket_id):
        """Request a plane ticket purchase.
        
        The client credit card number will be checked on the server
        and if it is everything ok it will perform the purchase, ie:
        remove the plane ticket from the server.

        Parameters
        ----------
        credit_card_number : int
            The credit card of the customer.

        number_of_installments : int
            The total number of payments for this
            touristic plane ticket.

        chosen_plane_ticket_id : int
            A single sequencial identifier that
            makes possible locate this plane ticket on 
            the server.

        Returns
        --------
        result : boolean
            True if the operation succeded, False otherwize.
        """

        result = self.client.service.buyPlaneTicket(credit_card_number,
                                                    number_of_installments,
                                                    chosen_plane_ticket_id)

        return result

    def register_hosting(self,
                         destination, 
                         input_date, 
                         output_date, 
                         number_of_rooms, 
                         guest_ages):
        """Perform a remote method call for registering a hosting.
        
        Parameters
        ----------
        destination : string
            The place where the hosting is located.

        input_date : tuple (int, int, int)
            Date display format (year, month, day) for
            the date of input.

        output_date : tuple (int, int, int)
            Date display format (year, month, day) for
            the date of output.

        number_of_rooms : int
            Number of rooms for this travel package.

        guest_ages : list of int
            The ages of the maximun number of guests
            for this travel package.
        """

        self.client.service.registerHosting(destination, input_date[0], input_date[1], input_date[2],
                                            output_date[0], output_date[1], output_date[2], number_of_rooms, guest_ages)

    def get_hosts(self):
        """Get all the available hosting facilities for purchase.
        
        Return
        -------
        hosts : list of Hosting
            Objects that represent a hosting facility.
        """

        hosts = self.client.service.getHosts()
        return hosts

    def buy_hosting(self, 
                    credit_card_number,
                    number_of_installments,
                    chosen_hosting_id):
        """Request a hosting facility purchase.
        
        The client credit card number will be checked on the server
        and if it is everything ok it will perform the purchase, ie:
        remove the hosting product from the server.

        Parameters
        ----------
        credit_card_number : int
            The credit card of the customer.

        number_of_installments : int
            The total number of payments for this
            hosting facility.

        chosen_hosting_id : int
            A single sequencial identifier that
            makes possible to locate this hosting product on 
            the server.

        Returns
        --------
        result : boolean
            True if the operation succeded, False otherwize.
        """

        result = self.client.service.buyHosting(credit_card_number,
                                                number_of_installments,
                                                chosen_hosting_id)

        return result