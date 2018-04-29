import sys
from astropy.io import fits
import numpy as np

#hdu3 = fits.open('peak_12co_pix_2_Tmb.fits')[0]
#
#peak12data = hdu3.data
#
### tex12.fits
#tex12data = 5.5 / np.log(1. + 5.5 / (peak12data + 0.82))
#tex12data[tex12data<=2.75] = np.nan
#hdu3.data = tex12data 
#hdu3.writeto('tex12.fits', output_verify='exception', overwrite=True, checksum=False)

#hdu3 = fits.open('peak_pixel6_convol18_mask_imfit_12co_pix_2_Tmb.fits')[0]
#
#peak12data = hdu3.data
#
### tex12.fits
#tex12data = 5.5 / np.log(1. + 5.5 / (peak12data + 0.82))
#tex12data[tex12data<=2.75] = np.nan
#hdu3.data = tex12data 
#hdu3.writeto('pixel6_convol18_tex12.fits', output_verify='exception', overwrite=True, checksum=False)

hdu3 = fits.open('peak_regrid_Stutz_convol18_mask_imfit_12co_pix_2_Tmb.fits')[0]
hdu4 = fits.open('carmanro_OrionA_all_spire250_nh_mask_corr_apex.fits')[0]

peak12data = hdu3.data
print peak12data.shape
print hdu4.data.shape
print peak12data[0,1445,0]

## tex12.fits
tex12data = 5.5 / np.log(1. + 5.5 / (peak12data + 0.82))
print tex12data[0,1445,0]
tex12data[tex12data<=2.75] = np.nan
print tex12data[0,1445,0]
hdu4.data = tex12data[0,:,:]
hdu4.writeto('regrid_Stutz_convol18_tex12.fits', output_verify='exception', overwrite=True, checksum=False)

