import sys
from astropy.io import fits
import numpy as np
from scipy import signal

def beampixel(bmaj,bmin,bpa,corecenter,cellsize,beamfraction=1.): # bmaj, bmin, cellsize in arcsec, corecenter = [pixelx, pixely], input bpa in degree
    pixellist = []
    rotation = float(bpa)/180.*np.pi
    cosa = np.cos(rotation)
    sina = np.sin(rotation)
    squareradius = int(bmaj/cellsize) # define a search domain first, make it twice bmaj
    xcenter,ycenter = corecenter
    semimajor = bmaj/2./cellsize*beamfraction**0.5
    semiminor = bmin/2./cellsize*beamfraction**0.5 
    for x in range(xcenter-squareradius,xcenter+squareradius+1):
        for y in range(ycenter-squareradius,ycenter+squareradius+1):
            if ((x-xcenter)*cosa+(y-ycenter)*sina)**2/semimajor**2 + ((x-xcenter)*sina-(y-ycenter)*cosa)**2/semiminor**2 < 1.:
                pixellist.append([x,y])
    return pixellist

hdu1 = fits.open('mask_imfit_12co_pix_2_Tmb.fits')[0]
hdu2 = fits.open('combined_scalefactor_12co.sen.fits')[0]
#hdu1.header['BUNIT'] = 'K'
#print hdu1.header
print hdu1.data.shape
rmsdata = hdu1.data[0:1,:10,:,:]
print hdu2.data.shape
shape2 = hdu2.data.shape
print rmsdata.shape
#sys.exit()
#np.nan_to_num(rmsdata,copy=False)
#detrend_rmsdata = signal.detrend(rmsdata,axis=1,type='linear')
#noise = np.nanstd(detrend_rmsdata,axis=1,keepdims=True)
noise = np.nanstd(rmsdata,axis=1,keepdims=True)
with open('ds9.reg') as f:
    content = f.readlines()
pixlists = []
for line in content:
    if '(' in line and ')' in line:
        coordinates = line.split('(')[1].split(')')[0].split(',')
        x,y,r = [int(float(item)) for item in coordinates]
        pixlist = beampixel(r*2.,r*2.,0,[x,y],1)
        doublepixlist = beampixel(r*4.,r*4.,0,[x,y],1)
        annuluspixlist = np.array([item for item in doublepixlist if item not in pixlist])
        annulusmean = np.nanmean(noise[0,0,annuluspixlist[:,1],annuluspixlist[:,0]])
        noise[0,0,np.array(pixlist)[:,1],np.array(pixlist)[:,0]] = annulusmean
repeat_noise = np.repeat(noise,shape2[1],axis=1)
repeat_noise[~(hdu2.data<2)] = np.nan
hdu2.data = repeat_noise

#for j in range(len(hdu2.data[0,0,:,0])):
#    for k in range(len(hdu2.data[0,0,0,:])):
##        if not ((j>3014 and j<3014+400 and k>1427 and k<1427+400) or (j>1303 and j<1303+400 and k>911 and k<911+400) or (j>760 and j<760+400 and k>818 and k<818+400)):
#        hdu2.data[0,:,j,k] = np.nanstd(rmsdata[:,j,k])
hdu2.writeto('12co_pix_2_Tmb_sens.fits', output_verify='exception', overwrite=True, checksum=False)

