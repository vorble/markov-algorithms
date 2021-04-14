# addition.py
#
# This script implements a Markov algorithm which can add two binary numbers.
# Input is given as an argument to the script on the command line:
#
#   python3 addition.py 1110+101101=
#
# where the input must be of the form:
#
# * One binary number
# * An addition sign
# * The other binary number
# * An equal sign

import sys
import re
import markov

rules = [
    # Left-shuttle digits across digits with <
    ('00<', '0<0'),
    ('10<', '0<1'),
    ('01<', '1<0'),
    ('11<', '1<1'),

    # Mark digit as held in place with : after left-shuttle
    ('0<', '0:'),
    ('1<', '1:'),

    # Digits left of = get left-shuttled with <
    ('0=', '0<='),
    ('1=', '1<='),

    # = turns to * to start arithmetic
    ('=', '*'),

    # Held digits are now in the correct position, drop :
    (':', ''),

    # Right-shuttle digits across digits with >
    # and right-shuttle across *, but stop after
    ('>00', '0>0'),
    ('>01', '1>0'),
    ('>10', '0>1'),
    ('>11', '1>1'),
    ('>20', '0>2'),
    ('>21', '1>2'),
    ('>0*', '*0'),
    ('>1*', '*1'),
    ('>2*', '*2'),

    # Perform binary addition (2 denotes carry), marking new
    # digit with > to be right-shuttled
    ('0+0', '+>0'),
    ('0+1', '+>1'),
    ('1+0', '+>1'),
    ('1+1', '+>2'),
    ('+0', '+>0'),
    ('+1', '+>1'),
    ('0+', '+>0'),
    ('1+', '+>1'),

    # Cleanup leftover symbols
    ('+*', ''),

    # Apply carry
    ('02', '10'),
    ('12', '20'),
    ('2', '10'),
]

for data in sys.argv[1:]:
    if re.compile('^[01]+\+[01]+=$').match(data):
        markov.animate(rules, data)
    else:
        print('Bad Input: ' + data)
    print()
