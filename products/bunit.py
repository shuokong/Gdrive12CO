import sys
from astropy.io import fits
hdu1 = fits.open('12co_pix_2_Tmb.fits')[0]
hdu1.header['BUNIT'] = 'K'
#print hdu1.header
#sys.exit()
hdu1.writeto('test.fits', output_verify='exception', clobber=True, checksum=False)

