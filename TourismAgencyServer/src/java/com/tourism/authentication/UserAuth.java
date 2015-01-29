/*
 * Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
 * (c) 2015
 *
 * License: MIT
 */
package com.tourism.authentication;

/**
 * Perform authentication operation
 * @author Allan
 */
public class UserAuth {
    
    private final String username = "admin";
    private final String password = "admin";
    
    /**
    * Perform login. Check if the given username and
    * password match to the admin username and password.
    * 
    * @param username the login username.
    * @param password the login password.
    * @return true if the username and password match,
    *         false otherwize.
    */
    public boolean login(String username, String password) {
    
        if (this.username.equals(username) && this.password.equals(password) ) {
         
            return true;
        }
        
        return false;
    }
}
