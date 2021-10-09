# Array of tests to run (in order)
# Each test contains
#   description - 
#   steps - A list of steps to perform, each step can have
#       inputs - A list of tuples for the inputs to apply at that step
#       *time - The time (in ms) to wait before continuing to the next step 
#           and before checking expected values for this step. The time should be a multiple of
#           the period of the system
#       *iterations - The number of clock ticks to wait (periods)
#       expected - The expected value at the end of this step (after the "time" has elapsed.) 
#           If this value is incorrect the test will fail early before completing.
#       * only one of these should be used
#   expected - The expected output (as a list of tuples) at the end of this test
# An example set of tests is shown below. It is important to note that these tests are not "unit tests" in 
# that they are not ran in isolation but in the order shown and the state of the device is not reset or 
# altered in between executions (unless preconditions are used).
tests = [ {'description': 'A:0x00 => B:0x00 C:0x00',
    'steps': [ {'inputs': [('PINA', 0x00)], 'iterations': 5 } ],
    'expected': [('PORTB', 0x00), ('PORTC', 0x00)],
    },
    {'description': 'A:0xFF => B:0x0F C:0xF0',
    'steps': [ {'inputs': [('PINA', 0xFF)], 'iterations': 5 } ],
    'expected': [('PORTB', 0x0F), ('PORTC', 0xF0)],
    },
    {'description': 'A:0xC7 => B:0x0C C:0x70',
    'steps': [ {'inputs': [('PINA', 0xC7)], 'iterations': 5 } ],
    'expected': [('PORTB', 0x0C), ('PORTC', 0x70)],
    },
    {'description': 'A:0x1D => B:0x01 C:0xD0',
    'steps': [ {'inputs': [('PINA', 0x1D)], 'iterations': 5 } ],
    'expected': [('PORTB', 0x01), ('PORTC', 0xD0)],
    },
    {'description': 'A:0x5A => B:0x05 C:0xA0',
    'steps': [ {'inputs': [('PINA', 0x5A)], 'iterations': 5 } ],
    'expected': [('PORTB', 0x05), ('PORTC', 0xA0)],
    },
    ]

# Optionally you can add a set of "watch" variables these need to be global or static and may need
# to be scoped at the function level (for static variables) if there are naming conflicts. The 
# variables listed here will display everytime you hit (and stop at) a breakpoint
