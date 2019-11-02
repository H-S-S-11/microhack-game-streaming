#include <inttypes.h>
#include <avr/io.h> 



void display_LED_portB(uint8_t number, uint8_t data_pin, uint8_t clk_pin);
void display_digit_portB(uint8_t segs, uint8_t digit, uint8_t data_pin, uint8_t clk_pin);
void display_string_portB(char *string, uint8_t digit_pins[4], uint8_t seg_pin, uint8_t clk_pin);