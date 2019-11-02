package energysimulator;

/**
 *
 * @author kieran
 */

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Calendar;

public class Timer
{
    
    private static final DateFormat dateFormat = new SimpleDateFormat("HH:mm:ss");
   
    
    public static int startTimer(){
        Calendar calendar = Calendar.getInstance();
        String dateTime = dateFormat.format(calendar.getTime());
    
        String[] timeArray = dateTime.split("");
        String hour1 = timeArray[0]; 
        String hour2 = timeArray[1];
        String hourComplete = hour1 + hour2;
        int hour = Integer.parseInt(hourComplete);
        int count = 0;
        Boolean isOn = true;
        do{
            try{
               Thread.sleep(6000);
            }
            catch(InterruptedException ex){
                Thread.currentThread().interrupt();
            }
            if (hour > 23){
                String hourString = "00";
                String[] hourCompleteStringArray = hourString.split("");
                timeArray[0] = hourCompleteStringArray[0];
                timeArray[1] = hourCompleteStringArray[1];
                hour = 0;
            } else{
                String hourString = Integer.toString(hour);
                String[] hourCompleteStringArray = hourString.split("");
                if (hourCompleteStringArray.length == 2){
                    timeArray[0] = hourCompleteStringArray[0];
                    timeArray[1] = hourCompleteStringArray[1];
                } else if (hourCompleteStringArray.length == 1){
                    timeArray[0] = "0";
                    timeArray[1] = hourCompleteStringArray[0];
                }
            }
            String time = "";
            for(String item: timeArray){
                time = time + item;
            }
            if (hour == 0){
                hour = 1;
            } else{
                hour = hour + 1;
            }
            count = count + 1;
            return count;
        }while (isOn == false);
        
    }
}
