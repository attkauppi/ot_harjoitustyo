package com.mycompany.unicafe;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;
//import com.mycompany.unicafe.Maksukortti;

public class MaksukorttiTest {

    Maksukortti kortti;
    
    public MaksukorttiTest() {
    }

    @Before
    public void setUp() {
        kortti = new Maksukortti(10);
    }

    @Test
    public void luotuKorttiOlemassa() {
        assertTrue(kortti!=null);      
    }
    
    @Test
    public void hello() {}
    
    @Test
    public void konstruktoriAsettaaOikein() {
        Maksukortti kortti = new Maksukortti(10);
        
        String vastaus = kortti.toString();
        System.out.println("vastaus: " + vastaus);
        assertEquals("saldo: 0.10", vastaus);
    }
    
    @Test
    public void syoEdullisestiVahentaaSaldoaOikein() {
        Maksukortti kortti = new Maksukortti(240);
        kortti.syoEdullisesti();
        assertEquals("saldo: 0.0", kortti.toString());
    }
    
    
}
    
//    @Test
//    public void konstruktoriAsettaaSaldonOikein() {
//    Maksukortti kortti = new Maksukortti(10);
//
//    String vastaus = kortti.toString();
//
//    assertEquals("Kortilla on rahaa 10.0 euroa", vastaus);

