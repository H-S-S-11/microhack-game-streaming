#include <inttypes.h>
#include <avr/io.h> 



void display_LED_portB(uint8_t number, uint8_t pin);
void display_digit_portB(uint8_t segs, uint8_t digit, uint8_t pin);
void display_string_portB(char *string, )