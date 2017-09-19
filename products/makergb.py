import numpy as np
import os
import sys
import math
import aplpy
import pyfits
import sys
import matplotlib.pyplot as plt

#templatehdulist = pyfits.open('ds9.fits')
#templatedata = templatehdulist[0].data
#channelhdulist = pyfits.open('13co_pix_2.cm.fits')
#channeldata = channelhdulist[0].data
#print templatedata.shape,channeldata.shape 
#
#stokes,channels,ymax,xmax = channeldata.shape
#
#channelstart=1 # start from which channel, note the different starting index. tbd
#currentchannel=channelstart
#
#for i in range(channels):
#    templatedata[:,:]=channeldata[0,currentchannel-1,:,:]
#    templatehdulist.writeto('channels_13co_pix_2/13co_channel_'+str(currentchannel)+'.fits',output_verify='exception',clobber=True,checksum=False) # use this as template to output every single channel
#    currentchannel = currentchannel + 1
#
#templatehdulist.close()
#channelhdulist.close()
#sys.exit()

channelstart = 2
channelend = 149

deltv = 0.11 # km/s
vref = 0.251 # km/s
refpix = 1

for i in range(channelstart,channelend+1):
    vgreen = vref + (i-refpix) * deltv
    vblue = vgreen - deltv
    vred = vgreen + deltv
    aplpy.rgb.sk_make_rgb_image(['channels_13co_pix_2/13co_channel_'+str(i+1)+'.fits','channels_13co_pix_2/13co_channel_'+str(i)+'.fits','channels_13co_pix_2/13co_channel_'+str(i-1)+'.fits'], 'channels_13co_pix_2/channel'+str(i).zfill(3)+'.png',str(vblue),str(vgreen),str(vred))
    #os.system('open channels_13co_pix_2/channel'+str(i).zfill(3)+'.png')

