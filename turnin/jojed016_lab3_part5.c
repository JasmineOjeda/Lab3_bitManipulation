/*	Author: Jasmine Ojeda jojed016@urc.edu
 *	Lab Section: 022
 *	Assignment: Lab 3  Exercise 5
 *	Exercise Description: Weight sensor
 *
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */
#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif

int main(void) {
    /* Insert DDR and PORT initializations */
    DDRD = 0x00; PORTA = 0xFF;
    DDRB = 0xFE; PORTB = 0x01;

    unsigned short tmp_D = 0x000;
    unsigned short tmp_B = 0x000;
    unsigned short weight = 0x000;

    /* Insert your solution below */
    while (1) {
        tmp_D = PIND;
	tmp_B = (PINB & 0x01);
        
        weight = (tmp_D << 1) | tmp_B;
        
	if (weight >= 70) {
            PORTB = 0x02;
        }
	else if ((weight > 5) & (weight < 70)) {
            PORTB = 0x04;
        }
	else {
            PORTB = 0x00;
        }
    }

    return 1;
}
