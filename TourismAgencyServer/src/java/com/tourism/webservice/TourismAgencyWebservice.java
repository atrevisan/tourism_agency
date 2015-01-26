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
     * This is a sample web service operation
     */
    @WebMethod(operationName = "hello")
    public String hello(@WebParam(name = "name") String txt) {
        return "Hello " + txt + " !";
    }

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
        
        UserAuth userAuth = new UserAuth();
        
        return userAuth.login(username, password);
    }

    /**
     * Perform the registration of a travel pack. Only the admin
     * has permition to perform this operation.
     * 
     * @param origin is the place of departure for this travel pack.
     * @param destination is the place of destination for this travel pack.
     * @param departureDate is the (day, month, year) of departure.
     * @param arrivalDate is the (day, month, year) of arrival.
     * @param numberOfRooms is the number of rooms for the destination of this travel pack.
     * @param isPromo tells if this package is promotional.
     */
    @WebMethod(operationName = "registerTravelPack")
    @Oneway
    public void registerTravelPack(@WebParam(name = "origin") String origin, 
                                   @WebParam(name = "destination") String destination, 
                                   @WebParam(name = "departureDate") int[] departureDate, 
                                   @WebParam(name = "arrivalDate") int[] arrivalDate, 
                                   @WebParam(name = "numberOfRooms") int numberOfRooms,
                                   @WebParam(name = "isPromo") boolean isPromo) {
        
        TouristicProductsManager manager = new TouristicProductsManager();
        
        ArrayList<TravelPack> travelPacks = manager.getPromotionalTravelPacks();
        
        int travelPackID = travelPacks.get(travelPacks.size() - 1).id + 1;
        
        TravelPack pack = new TravelPack(travelPackID, origin, destination, 
                                         departureDate, arrivalDate, numberOfRooms, isPromo);
        
        manager.saveTravelPack(pack);
    }
}
