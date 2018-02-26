import pyfits

templatehdulist = pyfits.open('pixel6_convol18_mask_imfit_12co_pix_2_Tmb.fits')
templatedata = templatehdulist[0].data[0,0,:,:]
templatehdulist[0].header['NAXIS'] = 2
del templatehdulist[0].header['CRPIX3']
del templatehdulist[0].header['CDELT3']
del templatehdulist[0].header['CRVAL3']
del templatehdulist[0].header['CTYPE3']
del templatehdulist[0].header['NAXIS3']
del templatehdulist[0].header['CRPIX4']
del templatehdulist[0].header['CDELT4']
del templatehdulist[0].header['CRVAL4']
del templatehdulist[0].header['CTYPE4']
del templatehdulist[0].header['NAXIS4']
pyfits.writeto('chan1_pixel6_convol18_mask_imfit_12co_pix_2_Tmb.fits',templatedata,templatehdulist[0].header,output_verify='exception',clobber=True,checksum=False)

