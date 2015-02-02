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
 * This class represents a tourism agency product
 * that is intended to be sold.
 * @author Allan
 */

@XmlType(name = "Product")
public class Product implements Serializable{
   
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
    
    @XmlElement(name = "guestAges")
    public int [] guestAges;
}