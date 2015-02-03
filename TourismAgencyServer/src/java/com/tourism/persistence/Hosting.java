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
 * This class represents a tourism agency hosting 
 * facility that is intended to be sold.
 * @author Allan
 */

@XmlType(name = "Hosting")
public class Hosting extends Product implements Serializable {
    
    @XmlElement(name = "inputDay")
    public int inputDay;
    
    @XmlElement(name = "inputMonth")
    public int inputMonth;
    
    @XmlElement(name = "inputYear")
    public int inputYear;
    
    @XmlElement(name = "outputDay")
    public int outputDay;
    
    @XmlElement(name = "outputMonth")
    public int outputMonth;
    
    @XmlElement(name = "outputYear")
    public int outputYear;
    
    public Hosting(int id, 
                   String destination,
                   int inputDay,
                   int inputMonth,
                   int inputYear,
                   int outputDay,
                   int outputMonth,
                   int outputYear,
                   int numberOfRooms,
                   int [] guestAges) {
        
        this.id = id;
        this.destination = destination;
        this.inputDay = inputDay;
        this.inputMonth = inputMonth;
        this.inputYear = inputYear;
        this.outputDay = outputDay;
        this.outputMonth = outputMonth;
        this.outputYear = outputYear;
        this.numberOfRooms = numberOfRooms;
        this.guestAges = guestAges;
    }
}