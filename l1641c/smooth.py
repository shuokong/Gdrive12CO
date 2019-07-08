import numpy as np
from astropy import units as u
from spectral_cube import SpectralCube
from astropy.convolution import Gaussian1DKernel
import pyfits

cube = SpectralCube.read('oriona_12CO_goodheader.fits')
fwhm_factor = np.sqrt(8*np.log(2))
current_resolution = 0.1 * u.km/u.s
target_resolution = 0.25 * u.km/u.s
pixel_scale = current_resolution
gaussian_width = ((target_resolution**2 - current_resolution**2)**0.5 / pixel_scale / fwhm_factor)
kernel = Gaussian1DKernel(gaussian_width)
new_cube = cube.spectral_smooth(kernel)

hdulist = pyfits.open('oriona_12CO_goodheader.fits')
hdulist[0].data=new_cube.hdulist[0].data/0.44 # convert to Tmb
#hdulist[0].header['RESTFREQ'] = 115.271204e9
#hdulist[0].header['BMAJ'] = 5.444e-3
#hdulist[0].header['BMIN'] = 5.444e-3
#hdulist[0].header['BPA'] = 0
hdulist.writeto('12CO_specsmooth.fits',output_verify='exception',clobber=True,checksum=False)

