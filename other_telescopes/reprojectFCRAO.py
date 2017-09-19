import sys
from astropy.io import fits
hdu1 = fits.open('FCRAO_OrionA_12co_xyv.fits')[0]
hdu1.header.rename_keyword('LINEFREQ','RESTFREQ')
#hdu1.header['CRVAL1'] = hdu1.header['CRVAL1'] + 0.0625393 
#hdu1.header['CRVAL2'] = hdu1.header['CRVAL2'] + 0.125198
#print hdu1.header
#sys.exit()
hdu1.data = hdu1.data / 0.45
hdu1.writeto('tmb_FCRAO_OrionA_12co_xyv.fits', output_verify='exception', overwrite=True, checksum=False)

