#include <inttypes.h>
#include <avr/io.h>
#include <util/delay.h>
#include "keypad_read.h"

#include "uart.h"

void keypad_init_portA(){
    DDRA |= 0x0f; //Upper four bits are inputs, lower are outputs
    MCUCR &= ~_BV(PUD);
    DDRA &= 0x0f;
    PORTA |= 0x00; //no pull ups on inputs, outputs low
}

void keypad_read_portA(){
    uint8_t x, y, pin_state;
    uint8_t key = 0x10; //default if no value read
    uint8_t masked_state;

    for (x=0; x<4; x++){
        //Set X pin high and see if any Y pins are pulled high
        PORTA |= _BV(x);
        _delay_ms(10);           
        pin_state = PINA;
        
        

        for(y=4; y<8; y++){
            masked_state = pin_state & _BV(y);
            if(masked_state != 0){
                  
                uart0_putch('<') ;  
                uart0_putc(x + '0');
                uart0_putc(y - 4 + '0');
                
            }
        }
        PORTA = 0x00;
    }
}