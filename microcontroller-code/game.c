#include <inttypes.h>
#include <avr/io.h>
#include <util/delay.h>
#include "game_displays.h"
#include "uart.h"

int main(){
    int red_d = 0;
    int red_cl = 1;
    DDRB |= _BV(PINB0);
    DDRB |= _BV(PINB1);
    PORTB = 0x00;

    //set up UART
    uart0_init (9600);
    uint16_t bytes_in_buffer;
    char recieved;

    while(1){
       
        bytes_in_buffer =  uart0_available();
       if(bytes_in_buffer){
           recieved = uart0_getc() - 48;
       }
        
        display_LED_portB(recieved, red_d, red_cl); 
    
    }
}