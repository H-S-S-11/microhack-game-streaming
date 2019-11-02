#include <inttypes.h>
#include <avr/io.h>
#include <util/delay.h>
#include "game_displays.h"

int main(){
    int red_d = 0;
    int red_cl = 1;
    DDRB |= _BV(PINB0);
    DDRB |= _BV(PINB1);
    PORTB = 0x00;

    while(1){
        /*
    PORTB |= _BV(PINB0);
    _delay_us(1);
    PORTB &= ~_BV(PINB1);
    PORTB |= _BV(PINB1);
    _delay_us(1);
    PORTB &= ~_BV(PINB1);
    _delay_ms(1000);

    PORTB &= ~_BV(PINB0);
    _delay_us(1);
    PORTB &= ~_BV(PINB1);
    PORTB |= _BV(PINB1);
    _delay_us(1);
    PORTB &= ~_BV(PINB1);
    _delay_ms(1000);
    */
        int i;
        for (i = 0; i<6; i++){
            display_LED_portB(i, red_d, red_cl);
            _delay_ms(1000);
        }
    
    }
}