import sys
from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename


#hdu1 = fits.open('chan1_pixel6_convol18_mask_imfit_12co_pix_2_Tmb.fits')[0]
#hdu2 = fits.open('../../OrionAdust/herschelAmelia/OrionA_all_spire250_nh_mask_corr_apex.fits')[0]
#from reproject import reproject_exact
#array, footprint = reproject_exact(hdu2, hdu1.header)
#fits.writeto('stutz_on_12co_header.fits', array, hdu1.header, clobber=True)

#hdu1 = fits.open('chan1_pixel6_convol18_mask_imfit_12co_pix_2_Tmb.fits')[0]
#hdu2 = fits.open('../../OrionAdust/lombardi_planck_herschel_plane3_colorT.fits')[0]
#from reproject import reproject_exact
#array, footprint = reproject_exact(hdu2, hdu1.header)
#fits.writeto('lombardi_colorT_on_12co_header.fits', array, hdu1.header, clobber=True)

#hdu1 = fits.open('chan1_pixel6_convol18_mask_imfit_12co_pix_2_Tmb.fits')[0]
#hdu2 = fits.open('../../OrionAdust/lombardi_planck_herschel_plane4_colorTerror.fits')[0]
#from reproject import reproject_exact
#array, footprint = reproject_exact(hdu2, hdu1.header)
#fits.writeto('lombardi_colorTerror_on_12co_header.fits', array, hdu1.header, clobber=True)

hdu1 = fits.open('carmanro_OrionA_all_spire250_nh_mask_corr_apex.fits')[0]
hdu2 = fits.open('../../OrionAdust/lombardi_planck_herschel_plane3_colorT.fits')[0]
from reproject import reproject_exact
array, footprint = reproject_exact(hdu2, hdu1.header)
fits.writeto('lombardi_colorT_on_Stutz_header.fits', array, hdu1.header, clobber=True)

