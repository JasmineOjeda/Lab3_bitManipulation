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
tests = [ {'description': 'A:0 B:0 => C:0',
    'steps': [ {'inputs': [('PINA', 0x00), ('PINB', 0x00)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x00)],
    },
    {'description': 'A:0x01 B:0x02 => C:2',
    'steps': [ {'inputs': [('PINA', 0x01), ('PINB', 0x02)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x02)],
    },
    {'description': 'A:0xFF B:0xFF => C:16',
    'steps': [ {'inputs': [('PINA', 0xFF), ('PINB', 0xFF)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x10)],
    },
    {'description': 'A:0x03 B:0x05 => C:4',
    'steps': [ {'inputs': [('PINA', 0x03), ('PINB', 0x05)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x04)],
    },
    {'description': 'A:0xF0 B:0x0F => C:8',
    'steps': [ {'inputs': [('PINA', 0xF0), ('PINB', 0x0F)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x08)],
    },
    {'description': 'A:0xF1 B:0x31 => C:8',
    'steps': [ {'inputs': [('PINA', 0xF1), ('PINB', 0x31)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x08)],
    },
    {'description': 'A:0xBA B:0xCD => C:10',
    'steps': [ {'inputs': [('PINA', 0xBA), ('PINB', 0xCD)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x0A)],
    },
    {'description': 'A:0x88 B:0x44 => C:4',
    'steps': [ {'inputs': [('PINA', 0x88), ('PINB', 0x44)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x04)],
    },
    {'description': 'A:0x96 B:0xF7 => C:11',
    'steps': [ {'inputs': [('PINA', 0x96), ('PINB', 0xF7)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x0B)],
    },
    {'description': 'A:0x00 B:0xFF => C:8',
    'steps': [ {'inputs': [('PINA', 0x00), ('PINB', 0xFF)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x08)],
    },
    ]

# Optionally you can add a set of "watch" variables these need to be global or static and may need
# to be scoped at the function level (for static variables) if there are naming conflicts. The 
# variables listed here will display everytime you hit (and stop at) a breakpoint
