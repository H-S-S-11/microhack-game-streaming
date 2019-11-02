#include <inttypes.h>
#include <avr/io.h>

void kepyad_init_portC(){
    DDRC = 0x0F; //Upper four bits are inputs, lower are outputs
    
}
uint8_t keypad_read_portC(){
    
}