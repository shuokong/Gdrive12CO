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

########################
corenums, xw, yw, corevelocities, coresnr = np.loadtxt('GAScores_12CO_peak_velocities.txt',usecols=(0,1,2,3,4),unpack=True)
########################

bins = np.linspace(2.25, 15.25, num=27) # evenly distributed in linear space
print 'bins',bins
binsizes = np.array([bins[ind] - bins[ind-1] for ind in range(1,len(bins))]) 
bincenters = np.array([(bins[ind] + bins[ind-1])/2. for ind in range(1,len(bins))])
print 'binsizes',binsizes
print 'bincenters',bincenters

hist = np.histogram(corevelocities, bins=bins, range=None, normed=False, weights=None, density=None) 
raw_corecounts = hist[0]/binsizes 
print 'raw_corecounts', raw_corecounts
#raw_corecounts_error = np.sqrt(hist[0])/binsizes
raw_corecounts_error = hist[0]*0.

plotdata = {
           'panel1':{
                     #'line1':{'xdata':raw_xdata,'ydata':powerlaw(raw_xdata,raw_amp,raw_index),'linestyle':'k--','label':r'$\alpha='+mc.to_precision(abs(raw_index),2)+r'\pm '+mc.to_precision(abs(raw_indexErr),2)+r'$','title':''},
                     'errorbar1':{'xdata':bincenters,'ydata':raw_corecounts,'yerror':raw_corecounts_error,'linestyle':'steps-mid','label':'astrograph','title':'','color':'black'},
                     'xlim':(0,20.),'ylim':(0,1.e2),'xscale':'linear','yscale':'linear','xlabel':r'$\rm core~velocity~km~s^{-1}$','ylabel':r'$\rm probability$', 
                    },
           }
xpanels = 1
ypanels = 1

lletter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

pdfname = 'velocity_distribution_12CO.pdf'
p=plt.figure(figsize=(1+6*xpanels,6*ypanels))
plt.subplots_adjust(top=0.96,bottom=0.08,left=0.15,right=0.96)
for i in range(xpanels):
    for j in range(ypanels):
        panel = i*xpanels+j+1
        ax=p.add_subplot(ypanels,xpanels,panel)
        ax.set_xscale(plotdata['panel'+str(panel)]['xscale'])
        ax.set_yscale(plotdata['panel'+str(panel)]['yscale'])
        xmin,xmax = plotdata['panel'+str(panel)]['xlim']
        ax.set_xlim(xmin,xmax)
        ymin,ymax = plotdata['panel'+str(panel)]['ylim']
        ax.set_ylim(ymin,ymax)
        ax.text(0.05, 0.95,'('+lletter[panel-1]+')',horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
        ax.set_ylabel(plotdata['panel'+str(panel)]['ylabel'])
        ax.set_xlabel(plotdata['panel'+str(panel)]['xlabel'])
        #ax.set_title(r'$\rm F_{1.3mm}-\Sigma~(MIR~source~removed)$')
        for eerrorbar in filter(lambda x: x[:8] == 'errorbar', plotdata['panel'+str(panel)].keys()): 
            ax.errorbar(plotdata['panel'+str(panel)][eerrorbar]['xdata'], plotdata['panel'+str(panel)][eerrorbar]['ydata'], yerr=plotdata['panel'+str(panel)][eerrorbar]['yerror'], drawstyle=plotdata['panel'+str(panel)][eerrorbar]['linestyle'], color=plotdata['panel'+str(panel)][eerrorbar]['color']) 
        for lline in filter(lambda x: x[:4] == 'line', plotdata['panel'+str(panel)].keys()): 
            ax.plot(plotdata['panel'+str(panel)][lline]['xdata'], plotdata['panel'+str(panel)][lline]['ydata'], plotdata['panel'+str(panel)][lline]['linestyle'], label=plotdata['panel'+str(panel)][lline]['label'])
        ax.legend(frameon=False)
os.system('rm '+pdfname)
plt.savefig(pdfname)
os.system('open '+pdfname)
plt.close(p)
os.system('cp '+pdfname+os.path.expandvars(' /Users/shuokong/GoogleDrive/imagesSFE/'))


