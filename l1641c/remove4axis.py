import pyfits

templatehdulist = pyfits.open('oriona_12CO_0603.casa.fits')
templatehdulist[0].header['CTYPE1'] = 'RA'
templatehdulist[0].header['CTYPE2'] = 'DEC'
templatehdulist[0].header['CTYPE3'] = 'VELO-LSR'
templatehdulist[0].header['RESTFREQ'] = 115.271204e9
templatehdulist.writeto('oriona_12CO_goodheader.fits',output_verify='exception',clobber=True,checksum=False)

