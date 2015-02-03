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
import java.util.logging.Level;
import java.util.logging.Logger;


/**
 * This class manages the persistence of the 
 * travel packs, plane tickets and hosting facilities
 * i.e the tourism agency products.
 * 
 * @author Allan
 */
public class TouristicProductsManager {
    
    private final String travelPacksFileName = "travelPacks4.ser";
    private final String planeTicketsFileName = "planeTickets.ser";
    private final String hostsFileName = "hosts.ser";
    
    /**
     * Save a list of products. They can be:
     * TravelPack, PlaneTicket or Hosting.
     * 
     * @param product is the new Product that will be saved.
     * @param  fileName is location in the file system in wich
     *                  the list will be saved.
     */
    private void saveProduct(Product product, String fileName) {
    
        try {
            
            FileInputStream inputStream = new FileInputStream(fileName);
            ObjectInputStream objectInputStream = new ObjectInputStream(inputStream);
            
            ArrayList<Product> productsList = (ArrayList<Product>) objectInputStream.readObject();
            
            // update the list
            productsList.add(product);
            
            FileOutputStream outputStream = new FileOutputStream(fileName);
            ObjectOutputStream objectOutputStream = new ObjectOutputStream(outputStream);
        
            // then save it again
            objectOutputStream.writeObject(productsList);
            
        } catch (FileNotFoundException e) {
            
            try { // in case the file not created yet
                
                FileOutputStream outputStream = new FileOutputStream(fileName);
                ObjectOutputStream objectOutputStream = new ObjectOutputStream(outputStream);
                
                ArrayList<Product> productsList  = new ArrayList<>();
                productsList.add(product);
                objectOutputStream.writeObject(productsList);
                
            } catch (FileNotFoundException ee) {
            } catch (IOException ee) {
            }
            
        } catch (IOException | ClassNotFoundException e) {
        }
    }
    
    /**
     * Delete a product from the file system.
     * 
     * @param productID is the id of the product that will be deleted.
     * @param fileName is the file system location of the file containning
     *                 products.
     * 
     * @return true if the product was found, false otherwize.
     */
    private boolean deleteProduct(int productID, String fileName) {
    
        ArrayList<Product> products = this.getProducts(fileName);
        
        for (Product product : products) {
        
            if (product.id == productID) {
            
                products.remove(product);
                
                try {
            
                    FileOutputStream outputStream = new FileOutputStream(fileName);
                    ObjectOutputStream objectOutputStream = new ObjectOutputStream(outputStream);
        
                    objectOutputStream.writeObject(products);
            
                } catch (IOException ex) {
                    Logger.getLogger(TouristicProductsManager.class.getName()).log(Level.SEVERE, null, ex);
                } finally{
                    return true;
                }
            }       
        }
        
        return false;
    }
    
     /**
     * Recover an array list of products from the file system. They
     * can be TravelPack, PlaneTicket or Hosting.
     * 
     * @param fileName of the list of products that will be recovered.
     * 
     * @return productsList containning one kind of touristic
     *         product.
     */
    private ArrayList<Product> getProducts(String fileName) {
    
        ArrayList<Product> productsList = null;
        try {
            
            FileInputStream inputStream = new FileInputStream(fileName);
            ObjectInputStream objectInputStream = new ObjectInputStream(inputStream);
            
            productsList = (ArrayList<Product>) objectInputStream.readObject();
            
        } catch (FileNotFoundException e) {
        } catch (IOException | ClassNotFoundException e) {
        } finally{        
            return productsList; 
        }
    }
    
    /**
     * Save a travel pack.
     * 
     * @param pack is the Travel pack to be saved.
    */
    public void saveTravelPack(TravelPack pack) {
        
        this.saveProduct(pack, this.travelPacksFileName);
    }
    
    /**
     * Remove a product from the filesystem
     * @param travelPackid is the id of the travel pack that will 
     *                     be deleted.
     * @return true if the product exists, false otherwize.
     */
    public boolean deleteTravelPack(int travelPackid) {
    
        return this.deleteProduct(travelPackid, this.travelPacksFileName);
    }
    
     /**
     * Recover the registered travel packs.
     * 
     * @return travelPackList containing all 
     * the registered travel packs.
     */
    public ArrayList<TravelPack> getTravelPacks() {
    
        ArrayList<Product> products = this.getProducts(this.travelPacksFileName);
        
        if(products == null)
            return null;
        
        ArrayList<TravelPack> travelPacks = this.copy(products, TravelPack.class);
        
        return travelPacks;
    }
    
     /**
     * Filter the promotional travel packs.
     * @return result are the travelPacks filtered.
     */
    public ArrayList<TravelPack> getPromotionalTravelPacks() {
    
        ArrayList<TravelPack> travelPacks = this.getTravelPacks();
        ArrayList<TravelPack> result = new ArrayList<>();
        
        for (TravelPack travelPack : travelPacks) {
        
            if (travelPack.isPromo)
                result.add(travelPack);
        }
        
        return result;
    }
    
    /**
    * Save a plane ticket.
    * 
    * @param planeTicket is the plane ticket that will be saved.
    */
    public void savePlaneTicket(PlaneTicket planeTicket) {
        
        this.saveProduct(planeTicket, this.planeTicketsFileName);
    }
    
     /**
     * Recover the registered plane tickets.
     * 
     * @return planeTickets containing all 
     * the registered plane tickets.
     */
    public ArrayList<PlaneTicket> getPlaneTickets() {
    
        ArrayList<Product> products = this.getProducts(this.planeTicketsFileName);
        
        if(products == null)
            return null;
        
        ArrayList<PlaneTicket> planeTickets = this.copy(products, PlaneTicket.class);
        
        return planeTickets;
    }

    /**
     * Remove a product from the filesystem
     * @param planeTicketID is the id of the plane ticket that will 
     *                     be deleted.
     * @return true if the product exists, false otherwize.
     */
    public boolean deletePlaneTicket(int planeTicketID) {
    
        return this.deleteProduct(planeTicketID, this.planeTicketsFileName);
    }
    
    /**
    * Save a hosting facility.
    * 
    * @param host is the hosting facility that will be saved.
    */
    public void saveHosting(Hosting host) {
        
        this.saveProduct(host, this.hostsFileName);
    }
    
    /**
     * Recover the registered hosts.
     * 
     * @return hosts containing all 
     *         the registered hosting facilities.
     */
    public ArrayList<Hosting> getHosts() {
    
        ArrayList<Product> products = this.getProducts(this.hostsFileName);
        
        if(products == null)
            return null;
        
        ArrayList<Hosting> hosts = this.copy(products, Hosting.class);
        
        return hosts;
    }
    
    /**
     * Cast an ArrayList of Products to the corresponding product type.
     * 
     * @param products are the objects that will be cast.
     * @param type is the type to wich the products will be cast.
     * @return result is the ArrayList with the right type of objects.
     */
    private <E> ArrayList<E> copy(ArrayList<Product> products, Class<E> type) {
    
        ArrayList<E> result = new ArrayList<>();
        
        for(Product prod : products) 
            
            result.add(type.cast(prod));
         
        return result;
    }
}
