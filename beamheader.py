import sys
from astropy.io import fits
hdu1 = fits.open('regrid_12CO_specsmooth.fits')[0]
hdu1.header['BMAJ'] = 5.972e-3
hdu1.header['BMIN'] = 5.972e-3
hdu1.header['BPA'] = 0
#print hdu1.header
#sys.exit()
hdu1.writeto('beamheader_regrid_12CO_specsmooth.fits', output_verify='exception', clobber=True, checksum=False)

