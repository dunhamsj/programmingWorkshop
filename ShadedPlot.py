#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

N  = 1000
x0 = -5.0
xf = 5.0

x = np.linspace( x0 , xf , N )
y = np.sin( x )

err1 = 0.1 * np.ones( N )
err2 = 0.2 * np.ones( N )
err3 = 0.3 * np.ones( N )

a = 0.1
c = 'b'
plt.plot( x , y , 'b-' , label = 'Data' )

plt.fill_between( x , y - err1 , y + err1 , color = c , alpha = a )
plt.fill_between( x , y - err2 , y + err2 , color = c , alpha = a )
plt.fill_between( x , y - err3 , y + err3 , color = c , alpha = a )

plt.xlabel( r'$x$' )
plt.ylabel( r'$\sin\left(x\right)$' )
plt.legend()
#plt.savefig( 'Errors.png' )
plt.show()
