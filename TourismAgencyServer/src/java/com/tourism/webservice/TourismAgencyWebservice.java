/*
 * Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
 * (c) 2015
 *
 * License: MIT
 */
package com.tourism.webservice;

import javax.jws.WebService;
import javax.jws.WebMethod;
import javax.jws.WebParam;

import com.tourism.authentication.UserAuth;
import com.tourism.persistence.TouristicProductsManager;
import com.tourism.persistence.TravelPack;
import java.util.ArrayList;
import javax.jws.Oneway;


/**
 *
 * @author Allan
 */
@WebService(serviceName = "TourismAgencyWebservice")
public class TourismAgencyWebservice {

    
    /**
     * Test if the username and password provided by the client
     * belong to the admin.
     * 
     * @param username the given username.
     * @param  password the given password.
     * @return return true to the client if the user provided
     *         correct username and password, false otherwize.
     */
    @WebMethod(operationName = "authenticate")
    public boolean authenticate(@WebParam(name = "username") String username, 
                                @WebParam(name = "password") String password) {
        
        System.out.println("authenticating");
        
        UserAuth userAuth = new UserAuth();
        
        boolean result = userAuth.login(username, password);
        
        return result;
    }

    /**
     * Perform the registration of a travel pack. Only the admin
     * has permition to perform this operation.
     * 
     * @param origin is the place of departure for this travel pack.
     * @param destination is the place of destination for this travel pack.
     * @param departureDay is the day of departure.
     * @param departureMonth is the month of departure.
     * @param departureYear is the year of departure.
     * @param arrivalDay is the day of arrival.
     * @param arrivalMonth is the month of arrival.
     * @param arrivalYear is the year of arrival.
     * @param numberOfRooms is the number of rooms for the destination of this travel pack.
     * @param isPromo tells if this package is promotional.
     * @param guestAges of the maximun nuber of guests that can be hosted at the destination.
     */
    
    @WebMethod(operationName = "registerTravelPack")
    @Oneway
    public void registerTravelPack(@WebParam(name = "origin") String origin, 
                                   @WebParam(name = "destination") String destination, 
                                   @WebParam(name = "departureYear") int departureYear,
                                   @WebParam(name = "departureMonth") int departureMonth,
                                   @WebParam(name = "departureDay") int departureDay,
                                   @WebParam(name = "arrivalYear") int arrivalYear,
                                   @WebParam(name = "arrivalMonth") int arrivalMonth,
                                   @WebParam(name = "arrivalDay") int arrivalDay,
                                   @WebParam(name = "numberOfRooms") int numberOfRooms,
                                   @WebParam(name = "isPromo") boolean isPromo,
                                   @WebParam(name = "guestAges") int [] guestAges) {
        
        System.out.println("Registering Travel pack");
        
        TouristicProductsManager manager = new TouristicProductsManager();
        ArrayList<TravelPack> travelPacks = manager.getTravelPacks();
        
        int travelPackID;
        
        if (travelPacks == null)
                travelPackID = 1;
        else
            travelPackID = travelPacks.get(travelPacks.size() - 1).id + 1;
        
        TravelPack pack = new TravelPack(travelPackID, 
                                         origin,
                                         destination, 
                                         departureDay,
                                         departureMonth,
                                         departureYear,
                                         arrivalDay,
                                         arrivalMonth,
                                         arrivalYear, 
                                         numberOfRooms, 
                                         isPromo,
                                         guestAges);
        
        manager.saveTravelPack(pack);
    }

    /**
     * Return all the registered travel packs to the client.
     * 
     * @return travelPacks available for purchase
     */
    @WebMethod(operationName = "getTravelPacks")
    public TravelPack[] getTravelPacks() {
       
        System.out.println("Getting travel packs");
        
        TouristicProductsManager manager = new TouristicProductsManager();
        ArrayList<TravelPack> travelPacks = manager.getTravelPacks();
        
        TravelPack[] travelPackArray = new TravelPack[travelPacks.size()];
        
        return travelPacks.toArray(travelPackArray);
    }
}
