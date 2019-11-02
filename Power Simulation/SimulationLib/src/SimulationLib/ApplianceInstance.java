/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package SimulationLib;

/**
 *
 * @author dyh1g19
 */
public class ApplianceInstance {
    public Appliance app;
    private boolean isOn;
    
    public ApplianceInstance(Appliance app) {
        this.app = app;
        this.isOn = false;
    }
    
    public void invertState() {
        this.isOn = !this.isOn;
    }
    
    public boolean getIsOn() {
        return this.isOn;
    }
}
