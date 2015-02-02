/*
 * Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
 * (c) 2015
 *
 * License: MIT
 */
package com.tourism.payment;

/**
 * Deals with the credit card number verifying and number of installments.
 * This class is just a mock up.
 * 
 * @author Allan
 */
public class PaymentProcessor {
   
    /**
     * process a payment request. Verify the credit card number
     * and charge the payment installments.
     * 
     * @param creditCardNumber is the credit card  information supplyed by the client
     *                         side.
     * 
     * @param numberOfInstallments is the total number of charges for this product.
     * 
     * @return true if everything ok, false otherwize.
     */
    public boolean processPayment(int creditCardNumber, int numberOfInstallments) {
    
        System.out.println("Number of installments: " + numberOfInstallments);
        
        if (creditCardNumber == 1234)
            return true;
        else
            return false;
    }
}
