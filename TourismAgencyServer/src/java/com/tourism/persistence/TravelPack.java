/*
 * Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
 * (c) 2015
 *
 * License: MIT
 */
package com.tourism.persistence;

import java.io.Serializable;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlType;

/**
 * This class represents a tourism agency travel
 * package that is intended to be sold.
 * @author Allan
 */

@XmlType(name = "TravelPack")
public class TravelPack extends Product implements Serializable {
   
    @XmlElement(name = "isPromo")
    public boolean isPromo;
    
    public TravelPack(int id,
                      String origin, 
                      String destination,
                      int departureDay,
                      int departureMonth,
                      int departureYear,
                      int arrivalDay,
                      int arrivalMonth,
                      int arrivalYear,
                      int numberOfRooms,
                      boolean isPromo,
                      int [] guestAges) {
        
        this.id = id;
        this.origin = origin;
        this.destination = destination;
        this.departureDay = departureDay;
        this.departureMonth = departureMonth;
        this.departureYear = departureYear;
        this.arrivalDay = arrivalDay;
        this.arrivalMonth = arrivalMonth;
        this.arrivalYear = arrivalYear;
        this.numberOfRooms = numberOfRooms;
        this.isPromo = isPromo;
        this.guestAges = guestAges;
    }
}