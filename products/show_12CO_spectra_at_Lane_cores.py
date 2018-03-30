import sys
from astropy.io import fits
from astropy.coordinates import SkyCoord
import astropy.wcs as wcs
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy import optimize 
from matplotlib import rc
rc('text', usetex=True)
font = {'weight' : 'normal','size':12,'family':'sans-serif','sans-serif':['Helvetica']}
rc('font', **font)

gaussian = lambda x, mmu, ssigma: 1. / (2.*np.pi*ssigma**2)**0.5 * np.exp(-(x-mmu)**2 / (2*ssigma**2))

def gaussian_fit(xdata,ydata,yerr,pinit): # xdata,ydata,yerr n-element arrays, pinit two-element list
    
    logx = xdata
    logy = ydata
    logyerr = yerr
    
#    # define our (line) fitting function
#    fitfunc = lambda p, x: 1. / (2.*np.pi*p[1]**2)**0.5 * np.exp(-(x-p[0])**2 / (2*p[1]**2))
#    errfunc = lambda p, x, y, err: (y - fitfunc(p, x)) / err
#    
#    # pinit = [1.0, -1.0]
#    out = optimize.leastsq(errfunc, pinit, args=(logx, logy, logyerr), full_output=1)
#    pfinal = out[0]
#    covar = out[1]

    popt,pcov = optimize.curve_fit(gaussian,logx,logy,p0=pinit)
    pfinal = popt 
    covar = pcov 

    print pfinal
    print covar
    
    sigma = pfinal[1]
    mu = pfinal[0]
    
    sigmaErr =  np.sqrt( covar[1][1] )
    muErr =  np.sqrt( covar[0][0] ) 
     
    return mu,muErr,sigma,sigmaErr

imagein = 'mask_imfit_12co_pix_2_Tmb.fits'
hdulist = fits.open(imagein)
print hdulist[0].data.shape
#sys.exit()
data = hdulist[0].data[0,:,:,:]
datarms = 0.86 # K data paper table 2
header = hdulist[0].header
crpix3 = header['CRPIX3']
cdelt3 = header['CDELT3']
crval3 = header['CRVAL3']
bmaj = 8. # header['BMAJ']*3600. # in arcsec
bmin = 8. # header['BMIN']*3600. # in arcsec
bpa = 0. # header['BPA']
cellsize = 2. # abs(header['CDELT1']*3600.) # in arcsec
n1,n2,n3 = data.shape
w = wcs.WCS(header)
hdulist.close()

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

########################
corenums, xw, yw = np.loadtxt('/Users/shuokong/GoogleDrive/OrionAdust/Lane2016/Getsources_cores_degree.txt',usecols=(0,1,2),unpack=True)
worldcoord = np.stack((xw,yw,np.zeros_like(xw),np.zeros_like(xw)),axis=1)
pixcoord = w.all_world2pix(worldcoord,1) # FITS standard uses 1
x = pixcoord[:,0]
y = pixcoord[:,1]

ypanels = 1
coregroups = []
coresubgroup = []
corenum = 1
for n,i in enumerate(corenums):
    if int(x[n]) < 0 or int(x[n]) > n3 or int(y[n]) < 0 or int(y[n]) > n2: continue
    corecenter = [int(x[n]),int(y[n])]
    corei = beampixel(bmaj,bmin,bpa,corecenter,cellsize,beamfraction=1.)
    coresubgroup.append([corei,corenums[n],n]) 
    if corenum % ypanels == 0: 
        coregroups.append(coresubgroup) 
        coresubgroup = [] 
    corenum = corenum + 1
if len(coresubgroup) > 0:
    coregroups.append(coresubgroup) 
########################

corevelocities = []
coresnr = []
subcorenums = []
subxw = []
subyw = []
os.system('rm -r Lane_cores_spectra')
os.system('mkdir Lane_cores_spectra')
for counter,coresubgroup in enumerate(coregroups):
    print counter
    p=plt.figure(figsize=(6,6*ypanels))
    plt.subplots_adjust(top=0.94,bottom=0.12,left=0.12,right=0.97)
    p.subplots_adjust(hspace=0.001)
    for nn,ii in enumerate(coresubgroup):
        ymin = 0
        ymax = 0
        ff,corenum,rank = ii
        corei = np.array(ff) 
        region = str(int(corenum)) 
        subcorenums.append(int(corenum))
        subxw.append(xw[rank])
        subyw.append(yw[rank])
        temp = data[:,corei[:,1],corei[:,0]] 
        spectrum = np.nanmean(temp,axis=(1))
        if np.nanmin(spectrum) < ymin: ymin = np.nanmin(spectrum)
        if np.nanmax(spectrum) > ymax: ymax = np.nanmax(spectrum)
        peakind = np.argmax(spectrum)
        velocity = [(crval3+cdelt3*((i+1)-crpix3))/1.e3 for i in range(n1)]
        corevelocities.append(velocity[peakind])
        snr = spectrum[peakind]/datarms
        coresnr.append(snr)
        ax=p.add_subplot(ypanels,1,nn+1)
        ax.plot(velocity, spectrum, 'k-') 
        ax.tick_params(axis='both',which='both',direction='in',top='on',labelsize=20)
        ax.text(0.1, 0.9, region,horizontalalignment='left',verticalalignment='center',transform = ax.transAxes,fontsize=20) 
        if nn+1 == 1:
            plt.title(r'$^{12}$CO(1-0)',fontsize=20)
        #ax.vlines(3.*rmscoremass,1,1e4,linestyles='dotted') 
        plt.ylabel(r'$T_{\rm mb}\rm (K)$',fontsize=20)
        #h = plt.ylabel(r'$\rm \frac{d\tilde{N}}{\tilde{N}dlog(N/N_0)}$')
        #h.set_rotation(0)
        if nn+1 < len(coresubgroup):
            plt.setp(ax.get_xticklabels(), visible=False)
        else:
            plt.xlabel(r'$v_{\rm LSR}\rm (km~s^{-1})$',fontsize=20)
        #plt.xscale('log') 
        #plt.yscale('log') 
        plt.xlim(0,20.) 
        ax.set_ylim(ymin,ymax)
        ax.vlines(velocity[peakind],ymin,ymax,linestyle='dashed')
        ax.text(velocity[peakind]+0.8, ymax*0.9, '%.1f' % velocity[peakind] +','+'%.1f' % snr,horizontalalignment='left',verticalalignment='center',fontsize=20)
    pdfname = 'Lane_cores_spectra/averspec12number'+str(region)+'.pdf'
    os.system('rm '+pdfname)
    plt.savefig(pdfname)
    #os.system('open '+pdfname)
    #os.system('cp '+pdfname+os.path.expandvars(' /Users/shuokong/GoogleDrive/imagesCARMAOrion/'))
    plt.close(p)

savetxtarr = np.stack((subcorenums,subxw,subyw,corevelocities,coresnr),axis=1)
np.savetxt('Lane_cores_spectra/Getsources_cores_12CO_peak_velocities.txt',savetxtarr,fmt='%3d %20.5f %20.5f %10.2f %5.1f')
