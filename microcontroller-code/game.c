#include <inttypes.h>
#include <avr/io.h>
#include <util/delay.h>
#include "game_displays.h"
#include "uart.h"
#include "keypad_read.h"

int main(){
    int red_d = 0;
    int red_cl = 1;
    DDRB |= _BV(PINB0);
    DDRB |= _BV(PINB1);
    DDRB |= _BV(PINB2);
    PORTB = 0x00;

    //set up UART
    uart0_init (UART_BAUD_SELECT(9600, 12000000));
    keypad_init_portA();

    uint16_t bytes_in_buffer;
    char recieved = 0;
    uint8_t health = 0;
    uint8_t segments = 0;

    while(1){

        bytes_in_buffer =  uart0_available();
        if(bytes_in_buffer){
            recieved = uart0_getc();
            //uart0_putc(recieved);
            if((0x30 <= recieved) && (recieved <= 0x53)){
            health = recieved - 0x30;
            }
       }
        
        keypad_read_portA();
        
        display_LED_portB(health, red_d, red_cl); 
        display_digit_portB(segments, 4, 2, 3);
        segments++;

        _delay_ms(16);
    
    }
}