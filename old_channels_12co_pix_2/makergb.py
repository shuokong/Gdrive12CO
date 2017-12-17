import numpy as np
import os
import sys
import math
import aplpy
import pyfits
import sys
import matplotlib.pyplot as plt

#templatehdulist = pyfits.open('../products/chan1_mask_imfit_12co_pix_2_Tmb.fits')
#templatedata = templatehdulist[0].data[0,0,:,:]
#templatehdulist[0].header['NAXIS'] = 2
#del templatehdulist[0].header['CRPIX3']
#del templatehdulist[0].header['CDELT3']
#del templatehdulist[0].header['CRVAL3']
#del templatehdulist[0].header['CTYPE3']
#del templatehdulist[0].header['NAXIS3']
#del templatehdulist[0].header['CRPIX4']
#del templatehdulist[0].header['CDELT4']
#del templatehdulist[0].header['CRVAL4']
#del templatehdulist[0].header['CTYPE4']
#del templatehdulist[0].header['NAXIS4']
#channelhdulist = pyfits.open('../products/mask_imfit_12co_pix_2_Tmb.fits')
#channeldata = channelhdulist[0].data
#print templatedata.shape#,templatehdulist[0].header
#print channeldata.shape#,channelhdulist[0].header
#
#stokes,channels,ymax,xmax = channeldata.shape
#
#channelstart=1 # start from which channel, note the different starting index. tbd
#currentchannel=channelstart
#
#for i in range(channels):
#    templatedata[:,:]=channeldata[0,currentchannel-1,:,:]
#    pyfits.writeto('12co_channel_'+str(currentchannel)+'.fits',templatedata,templatehdulist[0].header,output_verify='exception',clobber=True,checksum=False) # use this as template to output every single channel
#    currentchannel = currentchannel + 1
#
#templatehdulist.close()
#channelhdulist.close()
#sys.exit()

channelstart = 2
channelend = 85

deltv = 0.25 # km/s
vref = -1.939 # km/s
refpix = 1

for i in range(channelstart,channelend+1):
    vgreen = vref + (i-refpix) * deltv
    vblue = vgreen - deltv
    vred = vgreen + deltv
    aplpy.rgb.sk_make_rgb_image(['12co_channel_'+str(i+1)+'.fits','12co_channel_'+str(i)+'.fits','12co_channel_'+str(i-1)+'.fits'], 'channel'+str(i).zfill(3)+'.png',str(vblue),str(vgreen),str(vred))
    #os.system('open channels_12co_pix_2/channel'+str(i).zfill(3)+'.png')

