package SimulationLib;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author dyh1g19
 */
public class Cost {
    public final Float costRate;
    public Float totalUsage;
    
    public Cost(Float rate) {
        this.costRate = rate;
        this.totalUsage = 0.0f;
    }
}
