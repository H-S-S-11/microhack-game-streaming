#include <inttypes.h>
#include <avr/io.h>
#include <util/delay.h>
#include "keypad_read.h"

#include "uart.h"

void keypad_init_portA(){
    DDRA |= 0x0f; //Upper four bits are inputs, lower are outputs
    DDRA &= 0x0f;
    PORTA |= 0x0f; //no pull ups on inputs, outputs high
}

uint8_t keypad_read_portA(){
    uint8_t x, y, pin_state;
    uint8_t key = 0x10; //default if no value read
    uint8_t masked_state;

    for (x=0; x<4; x++){
        //Set X pin low and see if any Y pins are pulled low
        PORTA &= ~_BV(x);
        _delay_ms(10);           
        pin_state = PINA;
        
        /*
        int i;
        for (i=7;i>=0;i--){
            uart0_putc( ((pin_state >> i) & 0x01 )+ '0' );
        }
        uart0_putc(' ');
        */

        for(y=4; y<8; y++){
            _delay_ms(500);
            masked_state = pin_state & _BV(y);
            if(masked_state == 0){
                switch(x){
                    case 0:
                        switch(y){
                            case 4:
                                key = 1;
            
                            case 5:
                                key = 4;
                            case 6:
                                key = 7;
                            case 7:
                                key = 0x0a;
                            }

                    case 1:
                        switch(y){
                            case 4:
                                key = 2;
                            case 5:
                                key = 5;
                            case 6:
                                key = 8;
                            case 7:
                                key = 0;
                            }

                    case 2:
                        switch(y){
                            case 4:
                                key = 3;
                            case 5:
                                key = 6;
                            case 6:
                                key = 9;
                            case 7:
                                key = 0x0b;
                            }

                    case 3:
                        switch(y){
                            case 4:
                                key = 0x0f;
                            case 5:
                                key = 0x0e;
                            case 6:
                                key = 0x0d;
                            case 7:
                                key = 0x0c;
                            }                
                }
            uart0_putc(x + '0');
            uart0_putc(y + '0');
            
            }
        }
        PORTA = 0xff;
    }

    return key;

}