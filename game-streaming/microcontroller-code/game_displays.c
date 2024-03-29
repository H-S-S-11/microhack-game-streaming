#include <inttypes.h>
#include <avr/io.h>
#include <util/delay.h>
#include "game_displays.h"

const uint8_t segments[10] = {0xfc, 0x60, 0xc6, 0xf2,
        0x66, 0xb6, 0xbd, 0xd0, 0xfe, 0xd6  };

void display_LED_portB(uint8_t number, uint8_t data_pin, uint8_t clk_pin){
        int i;
        //Write number 1s followed by 5-number 0s
        PORTB |= _BV(data_pin);
        for(i=0; i<number; i++){
                _delay_us(1);
                PORTB &= ~_BV(clk_pin);
                PORTB |= _BV(clk_pin);
                _delay_us(1);
                PORTB &= ~_BV(clk_pin);
        }

        PORTB &= ~_BV(data_pin);
        while(i<5){
                _delay_us(1);
                PORTB &= ~_BV(clk_pin);
                PORTB |= _BV(clk_pin);
                _delay_us(1);
                PORTB &= ~_BV(clk_pin);       
                i++;
        }
}

void display_digit_portB(uint8_t segs, uint8_t digit, uint8_t data_pin, uint8_t clk_pin){
        PORTB |= _BV(digit);
        int i;
        for(i=0; i<8; i++){
                if (segs & _BV(i)){
                        PORTB |= _BV(data_pin);
                }     
                else {
                        PORTB &= ~_BV(data_pin);
                } 
                _delay_us(1);
                PORTB &= ~_BV(clk_pin);
                PORTB |= _BV(clk_pin);
                _delay_us(1);
                PORTB &= ~_BV(clk_pin);       
        }
        PORTB &= ~_BV(digit); //digit pin sinks LED current so must be low
}

void display_string_portB(char string[4], uint8_t digit_pins[4], uint8_t seg_pin, uint8_t clk_pin){

}