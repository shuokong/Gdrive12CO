import sys
import pyfits
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy import optimize 
from matplotlib import rc
rc('text', usetex=True)
font = {'weight' : 'normal','size':20,'family':'sans-serif','sans-serif':['Helvetica']}
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

print 'reading fits files'
hdulist1=pyfits.open('lombardi_colorT_on_12co_header.fits') #for Tex
hdulist2=pyfits.open('pixel6_convol18_mom0_12co_pix_2_Tmb.fits') #for mom0
hdulist3=pyfits.open('stutz_on_12co_header.fits') #for newNICEST38.fits or newNICER38.fits

scidata1=hdulist1[0].data
scidata2=hdulist2[0].data
scidata3=hdulist3[0].data

print 'scidata1.shape', scidata1.shape
print 'scidata2.shape', scidata2.shape
print 'scidata3.shape', scidata3.shape

tex=scidata1[:,:]
mom0=scidata2[0,:,:]
new38=scidata3[:,:]/9.4e20/2.

lowav=0
highav=200
lowi=0
highi=1000
maxte=np.nanmax(tex)
minte=np.nanmin(tex)
print minte,maxte

regionfiles = [[[1,1115,852,1424],'north','north'],[[1,969,852,1115],'central','central'],[[1,539,852,969],'south','south'],[[1,1,852,539],'furthersouth','L1641']]

p=plt.figure(figsize=(7,20))
plt.subplots_adjust(top=0.97,bottom=0.04,left=0.14,right=0.88)
p.subplots_adjust(hspace=0.001)
for nn,ii in enumerate(regionfiles):
    ff,fname,region = ii
    x1,y1,x2,y2 = ff
    submo = mom0[y1:y2,x1:x2]
    subav = new38[y1:y2,x1:x2]
    subte = tex[y1:y2,x1:x2]
    nanpix = np.isnan(submo) & np.isnan(subav) & np.isnan(subte)
    submo = list(submo[~nanpix])
    subav = list(subav[~nanpix])
    subte = list(subte[~nanpix])
    subav.append(lowav-10.)
    submo.append(0.)
    subte.append(minte)
    subav.append(lowav-10.)
    submo.append(0.)
    subte.append(maxte)
    ax=p.add_subplot(len(regionfiles),1,nn+1)
    plt.scatter(subav,submo,s=5,c=subte,marker="o",edgecolors='none')
    ax.tick_params(axis='both',which='both',direction='in',top='on',labelsize=20)
    ax.text(0.1, 0.9, region,horizontalalignment='left',verticalalignment='center',transform = ax.transAxes,fontsize=20) 
    if nn+1 == 1:
        plt.title(r'$^{12}$CO(1-0)',fontsize=20)
        box = ax.get_position()
        ax.set_position([box.x0*1., box.y0, box.width, box.height])
        axColor = plt.axes([box.x0*1.005 + box.width * 1.005, box.y0, 0.015, box.height])
        cbar=plt.colorbar(cax = axColor, orientation="vertical")
        cbar.ax.get_yaxis().labelpad = 20
        cbar.set_label(r'$\rm T_{dust}~(K)$', rotation=270)
    ax.set_ylabel(r'$\rm W_{^{12}CO(1-0)}~(K~km~s^{-1})$')
    if nn+1 < len(regionfiles):
        plt.setp(ax.get_xticklabels(), visible=False)
    else:
        ax.set_xlabel(r'$\rm A_V~(mag)$')
    ax.set_xlim(lowav,highav) 
    ax.set_ylim(lowi,highi)

pdfname = 'multicolor_12co_NH_tdust.pdf'
os.system('rm '+pdfname)
plt.savefig(pdfname)
os.system('open '+pdfname)
os.system('cp '+pdfname+' ~/GoogleDrive/imagesSFE/')
plt.close(p)

