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
}
