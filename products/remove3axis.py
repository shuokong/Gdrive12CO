import pyfits

templatehdulist = pyfits.open('mom0_regrid_Stutz_convol18_mask_imfit_12co_pix_2_Tmb.fits')
templatedata = templatehdulist[0].data[0,:,:]
templatehdulist[0].header['NAXIS'] = 2
del templatehdulist[0].header['CRPIX3']
del templatehdulist[0].header['CDELT3']
del templatehdulist[0].header['CRVAL3']
del templatehdulist[0].header['CTYPE3']
del templatehdulist[0].header['NAXIS3']
pyfits.writeto('novelocity_mom0_regrid_Stutz_convol18_mask_imfit_12co_pix_2_Tmb.fits',templatedata,templatehdulist[0].header,output_verify='exception',clobber=True,checksum=False)

