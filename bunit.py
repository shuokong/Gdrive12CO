import sys
from astropy.io import fits
#hdu1 = fits.open('regrid_nro_jy.fits')[0]
#hdu1 = fits.open('nro_jy.fits')[0]
hdu1 = fits.open('cowide.fits')[0]
hdu1.header['BMAJ'] = 21.6/3600.
hdu1.header['BMIN'] = 21.6/3600.
hdu1.header['BPA'] = 0
hdu1.header['CTYPE1'] = 'RA'
hdu1.header['CTYPE2'] = 'DEC'
#print hdu1.header
#sys.exit()
#hdu1.writeto('regrid_nro_jy.fits', output_verify='exception', clobber=True, checksum=False)
#hdu1.writeto('nro_jy.fits', output_verify='exception', clobber=True, checksum=False)
hdu1.writeto('test.fits', output_verify='exception', clobber=True, checksum=False)

