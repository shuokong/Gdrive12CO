import numpy as np
from astropy import units as u
from spectral_cube import SpectralCube
from astropy.convolution import Gaussian1DKernel
import pyfits

#cube = SpectralCube.read('12CO_20170514_FOREST-BEARS_spheroidal_grid7.5_dV0.099kms_xyb_YS_nonan.fits')
#fwhm_factor = np.sqrt(8*np.log(2))
#current_resolution = 0.099 * u.km/u.s
#target_resolution = 0.25 * u.km/u.s
#pixel_scale = current_resolution
#gaussian_width = ((target_resolution**2 - current_resolution**2)**0.5 / pixel_scale / fwhm_factor)
#kernel = Gaussian1DKernel(gaussian_width)
#new_cube = cube.spectral_smooth(kernel)
#
#hdulist = pyfits.open('12CO_20170514_FOREST-BEARS_spheroidal_grid7.5_dV0.099kms_xyb_YS_nonan.fits')
#hdulist[0].data=new_cube.hdulist[0].data
#hdulist[0].header['RESTFREQ'] = 115.271204e9
#hdulist.writeto('12CO_specsmooth.fits',output_verify='exception',clobber=True,checksum=False)

#cube = SpectralCube.read('12CO_20170514_FOREST-BEARS_spheroidal_grid7.5_dV0.099kms_xyb_YS_nonan.fits')
#fwhm_factor = np.sqrt(8*np.log(2))
#current_resolution = 0.099 * u.km/u.s
#target_resolution = 0.2 * u.km/u.s
#pixel_scale = current_resolution
#gaussian_width = ((target_resolution**2 - current_resolution**2)**0.5 / pixel_scale / fwhm_factor)
#kernel = Gaussian1DKernel(gaussian_width)
#new_cube = cube.spectral_smooth(kernel)
#
#hdulist = pyfits.open('12CO_20170514_FOREST-BEARS_spheroidal_grid7.5_dV0.099kms_xyb_YS_nonan.fits')
#hdulist[0].data=new_cube.hdulist[0].data
#hdulist[0].header['RESTFREQ'] = 115.271204e9
#hdulist[0].header['BMAJ'] = 5.972e-3
#hdulist[0].header['BMIN'] = 5.972e-3
#hdulist[0].header['BPA'] = 0
#hdulist.writeto('12CO_specsmooth_0p2.fits',output_verify='exception',clobber=True,checksum=False)

cube = SpectralCube.read('products/12co_pix_2_Tmb.fits')
fwhm_factor = np.sqrt(8*np.log(2))
current_resolution = 0.25 * u.km/u.s
target_resolution = 0.5 * u.km/u.s
pixel_scale = current_resolution
gaussian_width = ((target_resolution**2 - current_resolution**2)**0.5 / pixel_scale / fwhm_factor)
kernel = Gaussian1DKernel(gaussian_width)
new_cube = cube.spectral_smooth(kernel)

hdulist = pyfits.open('products/12co_pix_2_Tmb.fits')
hdulist[0].data=new_cube.hdulist[0].data
hdulist.writeto('12co_pix_2_Tmb_0p5.fits',output_verify='exception',clobber=True,checksum=False)

