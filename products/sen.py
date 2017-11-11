import sys
from astropy.io import fits
import numpy as np
from scipy import signal

hdu1 = fits.open('mask_imfit_12co_pix_2_Tmb.fits')[0]
hdu2 = fits.open('combined_scalefactor_12co.sen.fits')[0]
#hdu1.header['BUNIT'] = 'K'
#print hdu1.header
print hdu1.data.shape
rmsdata = hdu1.data[0:1,:15,:,:]
print hdu2.data.shape
shape2 = hdu2.data.shape
print rmsdata.shape
#sys.exit()
np.nan_to_num(rmsdata,copy=False)
detrend_rmsdata = signal.detrend(rmsdata,axis=1,type='linear')
noise = np.nanstd(detrend_rmsdata,axis=1,keepdims=True)
repeat_noise = np.repeat(noise,shape2[1],axis=1)
repeat_noise[~(hdu2.data<2)] = np.nan
hdu2.data = repeat_noise

#for j in range(len(hdu2.data[0,0,:,0])):
#    for k in range(len(hdu2.data[0,0,0,:])):
##        if not ((j>3014 and j<3014+400 and k>1427 and k<1427+400) or (j>1303 and j<1303+400 and k>911 and k<911+400) or (j>760 and j<760+400 and k>818 and k<818+400)):
#        hdu2.data[0,:,j,k] = np.nanstd(rmsdata[:,j,k])
hdu2.writeto('12co_pix_2_Tmb_sens.fits', output_verify='exception', overwrite=True, checksum=False)

