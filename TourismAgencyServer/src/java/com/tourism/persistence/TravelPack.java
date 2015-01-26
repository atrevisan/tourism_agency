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
    
    @XmlElement(name = "departureDate")
    public int[] departureDate;
    
    @XmlElement(name = "arrivalDate")
    public int[] arrivalDate;
    
    @XmlElement(name = "numberOfRooms")
    public int numberOfRooms;
    
    @XmlElement(name = "isPromo")
    public boolean isPromo;
    
    public TravelPack(int id,
                      String origin, 
                      String destination,
                      int[] departureDate,
                      int[] arrivalDate,
                      int numberOfRooms,
                      boolean isPromo) {
    
        this.id = id;
        this.origin = origin;
        this.destination = destination;
        this.departureDate = departureDate;
        this.arrivalDate = arrivalDate;
        this.numberOfRooms = numberOfRooms;
        this.isPromo = isPromo;
    }
}
