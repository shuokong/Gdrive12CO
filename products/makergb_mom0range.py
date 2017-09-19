import numpy as np
import os
import sys
import math
import aplpy
import pyfits
import sys
import matplotlib.pyplot as plt

#for mom0range in ['mom0_35_41_12co_pix_2_tmb.fits', 'mom0_42_48_12co_pix_2_tmb.fits', 'mom0_49_55_12co_pix_2_tmb.fits', 'mom0_56_62_12co_pix_2_Tmb.fits']:
#    hdulist = pyfits.open(mom0range)
#    hdulist[0].data = hdulist[0].data[0,:,:]
#    hdulist[0].header['NAXIS'] = 2
#    #del hdulist[0].header['NAXIS3']
#    del hdulist[0].header['CRPIX3']
#    del hdulist[0].header['CDELT3']
#    del hdulist[0].header['CRVAL3']
#    del hdulist[0].header['CTYPE3']
#    hdulist.writeto('test.fits',output_verify='exception',clobber=True,checksum=False) 
#    hdulist.close()
#    os.system('mv test.fits '+mom0range)
#sys.exit()

#vblue = '(6.56,8.06)'
#vgreen = '(8.31,9.81)'
#vred = '(10.06,11.56)'
#aplpy.rgb.sk_make_rgb_image(list(reversed(['mom0_35_41_12co_pix_2_tmb.fits', 'mom0_42_48_12co_pix_2_tmb.fits', 'mom0_49_55_12co_pix_2_tmb.fits'])), '12mom0range1.png',str(vblue),str(vgreen),str(vred))
#
#vblue  = '(8.31,9.81)'
#vgreen = '(10.06,11.56)'
#vred   = '(11.81,13.31)'
#aplpy.rgb.sk_make_rgb_image(list(reversed(['mom0_42_48_12co_pix_2_Tmb.fits', 'mom0_49_55_12co_pix_2_Tmb.fits', 'mom0_56_62_12co_pix_2_Tmb.fits'])), '12mom0range2.png',str(vblue),str(vgreen),str(vred))
#
#os.system('cp 12mom0range1.png 12mom0range2.png'+os.path.expandvars(' /Users/shuokong/GoogleDrive/imagesCARMAOrion/'))

#for mom0range in ['mom0_28_37_12co_pix_2_tmb.fits', 'mom0_38_47_12co_pix_2_tmb.fits', 'mom0_48_57_12co_pix_2_tmb.fits']:
#    hdulist = pyfits.open(mom0range)
#    hdulist[0].data = hdulist[0].data[0,:,:]
#    hdulist[0].header['NAXIS'] = 2
#    #del hdulist[0].header['NAXIS3']
#    del hdulist[0].header['CRPIX3']
#    del hdulist[0].header['CDELT3']
#    del hdulist[0].header['CRVAL3']
#    del hdulist[0].header['CTYPE3']
#    hdulist.writeto('test.fits',output_verify='exception',clobber=True,checksum=False) 
#    hdulist.close()
#    os.system('mv test.fits '+mom0range)
#sys.exit()

vblue = '(4.81,7.06)'
vgreen = '(7.31,9.56)'
vred = '(9.81,12.06)'
#aplpy.make_rgb_cube(list(reversed(['mom0_28_37_12co_pix_2_tmb.fits', 'mom0_38_47_12co_pix_2_tmb.fits', 'mom0_48_57_12co_pix_2_tmb.fits'])), 'mom0_rgb_cube.fits')
#aplpy.make_rgb_image('mom0_rgb_cube.fits', 'mom0_rgb_cube.png')
#aplpy.rgb.sk_make_rgb_image(list(reversed(['mom0_28_37_12co_pix_2_tmb.fits', 'mom0_38_47_12co_pix_2_tmb.fits', 'mom0_48_57_12co_pix_2_tmb.fits'])), '12mom0range.png',str(vblue),str(vgreen),str(vred))

ff = aplpy.FITSFigure('mom0_rgb_cube_2d.fits')
#ff.set_theme('publication')
ff.show_rgb('mom0_rgb_cube.png')
ff.ticks.set_color('black')
ff.tick_labels.set_font(size=8)
ff.add_label(83.6,-6.84,vblue,color='b')
ff.add_label(83.6,-6.84-0.05,vgreen,color='g')
ff.add_label(83.6,-6.84-0.05*2.,vred,color='r')
pdfname = '12mom0range.pdf'
os.system('rm '+pdfname)
plt.savefig(pdfname,bbox_inches='tight')
os.system('open '+pdfname)
os.system('cp '+pdfname+os.path.expandvars(' /Users/shuokong/GoogleDrive/imagesCARMAOrion/'))
