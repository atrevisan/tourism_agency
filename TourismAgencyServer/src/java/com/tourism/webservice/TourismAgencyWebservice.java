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
import com.tourism.payment.PaymentProcessor;
import com.tourism.persistence.Hosting;
import com.tourism.persistence.PlaneTicket;
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
        else{
           
            if (travelPacks.size() > 0)
                travelPackID = travelPacks.get(travelPacks.size() - 1).id + 1;
            else
                travelPackID = 1;
        }
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

    /**
     * Perform the selling operation: check payment and if everything ok
     * delete the product.
     * 
     * @param creditCardNumber is used to check the authenticity of the
     *                         customer.
     * @param numberOfInstallments is used to control the number of payments
     *                             the customer will make.
     * @param packageId is used to find this product and then delete it.
     * 
     * @return true if the operation succeded, false otherwize.
     */
    @WebMethod(operationName = "buyTravelPackage")
    public boolean buyTravelPackage(@WebParam(name = "creditCardNumber") int creditCardNumber, 
                                    @WebParam(name = "numberOfInstallments") int numberOfInstallments, 
                                    @WebParam(name = "packageId") int packageId) {
        
        System.out.println("Performing travel package purchase.");
        
        PaymentProcessor processor = new PaymentProcessor();
        
        boolean paymentOk = processor.processPayment(creditCardNumber, numberOfInstallments);
        
        if (paymentOk){
        
            TouristicProductsManager manager = new TouristicProductsManager();
            return manager.deleteTravelPack(packageId);
        }
        
        return false;
    }

    /**
     * Perform the registration of a plane ticket. Only the admin
     * has permition to perform this operation.
     * 
     * @param origin is the place of departure for this plane ticket.
     * @param destination is the place of destination for this plane ticket.
     * @param departureDay is the day of departure.
     * @param departureMonth is the month of departure.
     * @param departureYear is the year of departure.
     * @param arrivalDay is the day of arrival.
     * @param arrivalMonth is the month of arrival.
     * @param arrivalYear is the year of arrival.
     * @param numberOfRooms is the number of rooms for the destination of this 
     *                      plane ticket.
     * @param onlyDeparture tells if this plane ticket is departure only or roundtrip.
     * @param guestAges of the maximun nuber of guests that can be hosted at the destination.
     */
    @WebMethod(operationName = "registerPlaneTicket")
    @Oneway
    public void registerPlaneTicket(@WebParam(name = "origin") String origin, 
                                    @WebParam(name = "destination") String destination, 
                                    @WebParam(name = "departureYear") int departureYear,
                                    @WebParam(name = "departureMonth") int departureMonth,
                                    @WebParam(name = "departureDay") int departureDay,
                                    @WebParam(name = "arrivalYear") int arrivalYear,
                                    @WebParam(name = "arrivalMonth") int arrivalMonth,
                                    @WebParam(name = "arrivalDay") int arrivalDay,
                                    @WebParam(name = "numberOfRooms") int numberOfRooms,
                                    @WebParam(name = "onlyDeparture") boolean onlyDeparture,
                                    @WebParam(name = "guestAges") int [] guestAges) {
        
        System.out.println("Registering Plane ticket");
        
        TouristicProductsManager manager = new TouristicProductsManager();
        ArrayList<PlaneTicket> planeTickets = manager.getPlaneTickets();
        
        int planeTicketID;
        
        if (planeTickets == null)
                planeTicketID = 1;
        else{
           
            if (planeTickets.size() > 0)
                planeTicketID = planeTickets.get(planeTickets.size() - 1).id + 1;
            else
                planeTicketID = 1;
        }
        PlaneTicket planeTicket = new PlaneTicket(planeTicketID, 
                                                  origin,
                                                  destination, 
                                                  departureDay,
                                                  departureMonth,
                                                  departureYear,
                                                  arrivalDay,
                                                  arrivalMonth,
                                                  arrivalYear, 
                                                  numberOfRooms, 
                                                  onlyDeparture,
                                                  guestAges);
        
        manager.savePlaneTicket(planeTicket);
    }
    
    /**
     * Return all the registered plane tickets to the client.
     * 
     * @return planeTickets available for purchase
     */
    @WebMethod(operationName = "getPlaneTickets")
    public PlaneTicket[] getPlaneTickets() {
       
        System.out.println("Getting plane tickets");
        
        TouristicProductsManager manager = new TouristicProductsManager();
        ArrayList<PlaneTicket> planeTickets = manager.getPlaneTickets();
        
        PlaneTicket[] planeTicketsArray = new PlaneTicket[planeTickets.size()];
        
        return planeTickets.toArray(planeTicketsArray);
    }
    
     /**
     * Perform the selling operation: check payment and if everything ok
     * delete the product.
     * 
     * @param creditCardNumber is used to check the authenticity of the
     *                         customer.
     * @param numberOfInstallments is used to control the number of payments
     *                             the customer will make.
     * @param planeTicketID is used to find this product and then delete it.
     * 
     * @return true if the operation succeded, false otherwize.
     */
    @WebMethod(operationName = "buyPlaneTicket")
    public boolean buyPlaneTicket(@WebParam(name = "creditCardNumber") int creditCardNumber, 
                                  @WebParam(name = "numberOfInstallments") int numberOfInstallments, 
                                  @WebParam(name = "planeTicketID") int planeTicketID) {
        
        System.out.println("Performing plane ticket purchase.");
        
        PaymentProcessor processor = new PaymentProcessor();
        
        boolean paymentOk = processor.processPayment(creditCardNumber, numberOfInstallments);
        
        if (paymentOk){
        
            TouristicProductsManager manager = new TouristicProductsManager();
            return manager.deletePlaneTicket(planeTicketID);
        }
        
        return false;
    }
    
    /**
     * Perform the registration of a hosting facility. Only the admin
     * has permition to perform this operation.
     * 
     * @param destination is the place of destination for this hosting facility.
     * @param inputDay is the day of input.
     * @param inputMonth is the month of input.
     * @param inputYear is the year of input.
     * @param outputDay is the day of output.
     * @param outputMonth is the month of output.
     * @param outputYear is the year of output.
     * @param numberOfRooms is the number of rooms for the hosting.
     * @param guestAges of the maximun nuber of guests that can be hosted.
     */
    @WebMethod(operationName = "registerHosting")
    @Oneway
    public void registerHosting(@WebParam(name = "destination") String destination, 
                                @WebParam(name = "inputYear") int inputYear,
                                @WebParam(name = "inputMonth") int inputMonth,
                                @WebParam(name = "inputDay") int inputDay,
                                @WebParam(name = "outputYear") int outputYear,
                                @WebParam(name = "outputMonth") int outputMonth,
                                @WebParam(name = "outputDay") int outputDay,
                                @WebParam(name = "numberOfRooms") int numberOfRooms,
                                @WebParam(name = "guestAges") int [] guestAges) {
        
        System.out.println("Registering hosting");
        
        TouristicProductsManager manager = new TouristicProductsManager();
        ArrayList<Hosting> hosts = manager.getHosts();
        
        int hostID;
        
        if (hosts == null)
                hostID = 1;
        else{
           
            if (hosts.size() > 0)
                hostID = hosts.get(hosts.size() - 1).id + 1;
            else
                hostID = 1;
        }
        
        Hosting host = new Hosting(hostID, 
                                   destination, 
                                   inputDay,
                                   inputMonth,
                                   inputYear,
                                   outputDay,
                                   outputMonth,
                                   outputYear, 
                                   numberOfRooms, 
                                   guestAges);
        
        manager.saveHosting(host);
    }
    
    /**
     * Return all the registered hosting facilities to the client.
     * 
     * @return hosts available for purchase
     */
    @WebMethod(operationName = "getHosts")
    public Hosting[] getHosts() {
       
        System.out.println("Getting hosts");
        
        TouristicProductsManager manager = new TouristicProductsManager();
        ArrayList<Hosting> hosts = manager.getHosts();
        
        Hosting[] hostsArray = new Hosting[hosts.size()];
        
        return hosts.toArray(hostsArray);
    }
    
     /**
     * Perform the selling operation: check payment and if everything ok
     * delete the product.
     * 
     * @param creditCardNumber is used to check the authenticity of the
     *                         customer.
     * @param numberOfInstallments is used to control the number of payments
     *                             the customer will make.
     * @param hostingID is used to find this product and then delete it.
     * 
     * @return true if the operation succeded, false otherwize.
     */
    @WebMethod(operationName = "buyHosting")
    public boolean buyHosting(@WebParam(name = "creditCardNumber") int creditCardNumber, 
                              @WebParam(name = "numberOfInstallments") int numberOfInstallments, 
                              @WebParam(name = "hostingID") int hostingID) {
        
        System.out.println("Performing hosting purchase.");
        
        PaymentProcessor processor = new PaymentProcessor();
        
        boolean paymentOk = processor.processPayment(creditCardNumber, numberOfInstallments);
        
        if (paymentOk){
        
            TouristicProductsManager manager = new TouristicProductsManager();
            return manager.deleteHosting(hostingID);
        }
        
        return false;
    }
}