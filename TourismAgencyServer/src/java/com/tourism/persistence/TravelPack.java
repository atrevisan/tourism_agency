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
public class TravelPack implements Serializable{
   
    @XmlElement(name = "id")
    public int id;
    
    @XmlElement(name = "origin")
    public String origin; 
    
    @XmlElement(name = "destination")
    public String destination;
    
    @XmlElement(name = "departureDay")
    public int departureDay;
    
    @XmlElement(name = "departureMonth")
    public int departureMonth;
    
    @XmlElement(name = "departureYear")
    public int departureYear;
    
    @XmlElement(name = "arrivalDay")
    public int arrivalDay;
    
    @XmlElement(name = "arrivalMonth")
    public int arrivalMonth;
    
    @XmlElement(name = "arrivalYear")
    public int arrivalYear;
    
    @XmlElement(name = "numberOfRooms")
    public int numberOfRooms;
    
    @XmlElement(name = "isPromo")
    public boolean isPromo;
    
    @XmlElement(name = "guestAges")
    public int [] guestAges;
    
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