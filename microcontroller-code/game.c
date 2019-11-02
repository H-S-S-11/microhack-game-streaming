#include <inttypes.h>
#include <avr/io.h>
#include <avr/utils.h>
#include "game_displays.h"

int main(){
    int red_d = 0;
    int red_cl = 1;
    DDRB |= _BV(PINB0);
    display_LED_portB(5, red_d, red_cl);
}