import sys
from astropy.io import fits
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

regionfiles = [['north_sen_gt2_12co_pix_2_Tmb.fits','north','north'],['central_sen_gt2_12co_pix_2_Tmb.fits','central','central'],['south_sen_gt2_12co_pix_2_Tmb.fits','south','south'],['furthersouth_sen_gt2_12co_pix_2_Tmb.fits','furthersouth','futher south']]

p=plt.figure(figsize=(6,18))
plt.subplots_adjust(top=0.99,bottom=0.03,left=0.11,right=0.97)
p.subplots_adjust(hspace=0.001)
for nn,ii in enumerate(regionfiles):
    ff,fname,region = ii
    hdu1 = fits.open(ff)[0]
    crpix3 = hdu1.header['CRPIX3']
    cdelt3 = hdu1.header['CDELT3']
    crval3 = hdu1.header['CRVAL3']
    coldensdata = hdu1.data[0,:,:,:]
    print coldensdata.shape
    n1,n2,n3 = coldensdata.shape
    spectrum = np.nanmean(coldensdata,axis=(1,2))
    print spectrum.shape
    velocity = [(crval3+cdelt3*((i+1)-crpix3))/1.e3 for i in range(n1)]
    #sys.exit()
    ax=p.add_subplot(len(regionfiles),1,nn+1)
    ax.plot(velocity, spectrum, 'k-') 
    ax.tick_params(axis='both',which='both',direction='in',top='on')
    ax.text(0.1, 0.9, region,horizontalalignment='left',verticalalignment='center',transform = ax.transAxes,fontsize=12) 
    #ax.vlines(3.*rmscoremass,1,1e4,linestyles='dotted') 
    plt.ylabel(r'$T_{\rm mb}\rm (K)$')
    #h = plt.ylabel(r'$\rm \frac{d\tilde{N}}{\tilde{N}dlog(N/N_0)}$')
    #h.set_rotation(0)
    if nn+1 < len(regionfiles):
        plt.setp(ax.get_xticklabels(), visible=False)
    else:
        plt.xlabel(r'$v_{\rm LSR}\rm (km~s^{-1})$')
    #plt.xscale('log') 
    plt.xlim(0,20.) 
    #plt.yscale('log') 

pdfname = 'averspec.pdf'
os.system('rm '+pdfname)
plt.savefig(pdfname)
os.system('open '+pdfname)
os.system('cp '+pdfname+os.path.expandvars(' /Users/shuokong/GoogleDrive/imagesCARMAOrion/'))
plt.close(p)

