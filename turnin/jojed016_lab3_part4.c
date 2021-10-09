/*	Author: Jasmine Ojeda jojed016@urc.edu
 *	Lab Section: 022
 *	Assignment: Lab 3  Exercise 4
 *	Exercise Description: Output A's upper nibble to B's lower nibble,
 *	                      and A's lower nibble to C's upper nibble
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
    DDRA = 0x00; PORTA = 0xFF;

    DDRB = 0xFF; PORTB = 0x00;
    DDRC = 0xFF; PORTC = 0x00;

    unsigned char upper_A = 0x00;
    unsigned char lower_A = 0x00;

    /* Insert your solution below */
    while (1) {
        upper_A = PINA & 0xF0;
	lower_A = PINA & 0x0F;

	PORTB = upper_A >> 4;
	PORTC = lower_A << 4;
    }

    return 1;
}
