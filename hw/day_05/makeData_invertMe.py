#!/usr/bin/env python3

import numpy as np

data = np.linspace( -1.0, +1.0, 101 )

with open( '../../data/invertMe.dat', 'w' ) as fout:

    fout.write( 'x\n' )

    for i in range( data.shape[0] ):
        fout.write( str( data[i] ) + '\n' )
