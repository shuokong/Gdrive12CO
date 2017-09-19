import numpy as np
import pyfits

def gapfill(x,y,data,patchr):
    patch = data[x-patchr:x+patchr+1,y-patchr:y+patchr+1]
    print 'from gapfill, patch shape',patch.shape
    return np.nanmean(patch)

hdulist = pyfits.open('12CO_20170514_FOREST-BEARS_spheroidal_grid7.5_dV0.099kms_xyb_YS.fits')
chan,dec,ra = hdulist[0].data.shape
#print chan,dec,ra
for c in range(chan):
    for d in range(dec):
        for r in range(ra):
            if np.isnan(hdulist[0].data[c,d,r]) and ((r > 180 and r < 715 and d > 606 and d < 1173) or (r > 178 and r < 560 and d > 253 and d < 609) or (r > 25 and r < 432 and d > 182 and d < 270)):
                newval = gapfill(d,r,hdulist[0].data[c,:,:],3)
                print 'c,d,r,newval',c,d,r,newval
                hdulist[0].data[c,d,r] = newval
                #ss=raw_input()
hdulist.writeto('12CO_20170514_FOREST-BEARS_spheroidal_grid7.5_dV0.099kms_xyb_YS_nonan.fits',output_verify='exception',clobber=True,checksum=False)
hdulist.close()

