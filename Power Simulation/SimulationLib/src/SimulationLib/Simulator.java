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

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.lang.NumberFormatException;
import java.util.*;

public class Simulator {
    public final List<ApplianceInstance> applianceInstances;
    public final List<Appliance> appliances;
    private Dictionary<FuelType, Cost> costRates;

    public Simulator() {
        this.appliances = new ArrayList<Appliance>();
        this.applianceInstances = new ArrayList<ApplianceInstance>();
        this.costRates = new Hashtable<FuelType, Cost>();
    }
    
    public Simulator(String applianceFile, String costRateFile) {
        this();
        this.loadAppliancesFromCsv(applianceFile);
        this.loadCostRatesFromCsv(costRateFile);
    }
    
    private void loadAppliancesFromCsv(String filename) {
        List<String[]> data = readFromCsv(filename);
        Iterator<String[]> data_iter = data.iterator();
         
       while (data_iter.hasNext()) {
            String[] appliance_data = data_iter.next();
            
            String name = appliance_data[0];
            FuelType type = this.typeFromString(appliance_data[1]);
            try {
                Float powerRate = Float.parseFloat(appliance_data[2]);
                Appliance app = new Appliance(name, type, powerRate);
                appliances.add(app);
            } catch (NumberFormatException e) {
            }
        }
    }
    
    private void loadCostRatesFromCsv(String filename) {
        List<String[]> data = readFromCsv(filename);
        
        for (String[] costRateData: data) {
            FuelType type = this.typeFromString(costRateData[0]);
            System.out.println(costRateData[0] + ": " + type);
            try {
                Float ratePrice = Float.parseFloat(costRateData[1]);
                Cost cost = new Cost(ratePrice);
                this.costRates.put(type, cost);
            } catch (NumberFormatException e) {
            }
        }
    }
    
    private List<String[]> readFromCsv(String filename) {
        BufferedReader br = null;
        String line = "";
        String delimiter = ",";
        List<String[]> lines = new ArrayList<String[]>();
        
        try {
            br = new BufferedReader(new FileReader(filename));
            while ((line = br.readLine()) != null) {
                lines.add(line.split(delimiter));
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (br != null) {
                try {
                    br.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return lines;
        }
    }
    
    private static FuelType typeFromString(String type) {
        if (type.equals("Electricity")) {
            return FuelType.Electricity;
        } else if (type.equals("Gas")) {
            return FuelType.Gas;
        } else {
            return FuelType.Unknown;
        }
    }
    
    //
    
    public ApplianceInstance addAppliance(String name) {
        for (Appliance app: appliances) {
            if (app.name.equals(name)) {
                System.out.println("added: " + app);
                ApplianceInstance appInst = new ApplianceInstance(app);
                this.applianceInstances.add(appInst);
                return appInst;
            }
        }
        return null;
    }
    
    public void passHour(Integer incrementBy) {
        for (ApplianceInstance appInst: applianceInstances) {
            if (appInst.getIsOn()) {
                Appliance app = appInst.app;
                Cost cost = this.costRates.get(app.type);
                cost.totalUsage += app.powerRate * incrementBy * cost.costRate;    
            }
        }
    }
    
    public Float totalCostOf(FuelType type) {
        Cost cost = this.costRates.get(type);
        return cost.totalUsage * cost.costRate;
    }
    
    public Float totalUsageOf(FuelType type) {
        return this.costRates.get(type).totalUsage;
    }
}
