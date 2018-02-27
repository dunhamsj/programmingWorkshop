#!/usr/bin/python

##### http://docs.astropy.org/en/stable/io/fits/

from astropy.io import fits

fits_file = 'fits_sample.fits'

hdu_list = fits.open( fits_file )
print hdu_list.info()

header = hdu_list[0].header
print repr( header )

print header.keys()
print '\nDATE:     ' , header['DATE']
print 'TELESCOPE:' , header['TELESCOP']

'''
data = hdu_list[0].data
print data.shape

import matplotlib.pyplot as plt
plt.imshow( data , origin = 'lower', vmin = 0 , vmax = 1.0e-1 )
plt.show()
'''
