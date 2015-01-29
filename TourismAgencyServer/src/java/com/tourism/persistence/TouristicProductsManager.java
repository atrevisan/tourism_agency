/*
 * Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
 * (c) 2015
 *
 * License: MIT
 */
package com.tourism.persistence;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;


/**
 * This class manages the persistence of the 
 * travel packs, plane tickets and hosting facilities
 * products
 * 
 * @author Allan
 */
public class TouristicProductsManager {
    
    private final String travelPacksFileName = "travelPacks3.ser"; 
   
    /**
     * Use generics to save a list of objects. In this case they can be:
     * TravelPack, PlaneTicket or Hosting.
     * 
     * @param object is the new object that will be saved.
     * @param  fileName is location in the file system in wich
     * the list will be saved.
     */
    private <E> void saveObject(E object, String fileName) {
    
        try {
            
            FileInputStream inputStream = new FileInputStream(fileName);
            ObjectInputStream objectInputStream = new ObjectInputStream(inputStream);
            
            ArrayList<E> objectList = (ArrayList<E>) objectInputStream.readObject();
            
            // update the list
            objectList.add(object);
            
            FileOutputStream outputStream = new FileOutputStream(fileName);
            ObjectOutputStream objectOutputStream = new ObjectOutputStream(outputStream);
        
            // then save it again
            objectOutputStream.writeObject(objectList);
            
        } catch (FileNotFoundException e) {
            
            try { // in case the file not created yet
                
                FileOutputStream outputStream = new FileOutputStream(fileName);
                ObjectOutputStream objectOutputStream = new ObjectOutputStream(outputStream);
                
                ArrayList<E> objectList  = new ArrayList<>();
                objectList.add(object);
                objectOutputStream.writeObject(objectList);
                
            } catch (FileNotFoundException ee) {
                
                ee.printStackTrace();
            } catch (IOException ee) {
                
                ee.printStackTrace();
            }
            
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
    
    /**
     * Save a travel pack.
     * 
     * @param pack is the Travel pack to be saved.
    */
    public void saveTravelPack(TravelPack pack) {
    
        
        this.saveObject(pack, this.travelPacksFileName);
    }
    
    /**
     * Recover the registered travel packs.
     * 
     * @return travelPackList containing all 
     * the registered travel packs.
     */
    public ArrayList<TravelPack> getTravelPacks() {
    
        ArrayList<TravelPack> travelPackList = null;
        try {
            
            FileInputStream inputStream = new FileInputStream(this.travelPacksFileName);
            ObjectInputStream objectInputStream = new ObjectInputStream(inputStream);
            
            travelPackList = (ArrayList<TravelPack>) objectInputStream.readObject();
            
        } catch (FileNotFoundException e) {
            
            return null;
            
        } catch (IOException e) {
            
            e.printStackTrace();
            
        } catch (ClassNotFoundException e) {
            
            e.printStackTrace();
        
        } 
        
        return travelPackList;  
    }
    
    public ArrayList<TravelPack> getPromotionalTravelPacks() {
    
        return null;
    }
}
