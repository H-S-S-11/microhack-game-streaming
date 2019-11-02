#include <inttypes.h>
#include <avr/io.h>

void init_uart0(void);
char get_ch(void);
void get_str(char *string);
void put_ch(char ch);
void put_str(char *str);
