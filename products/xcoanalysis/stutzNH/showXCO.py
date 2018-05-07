import aplpy
import os
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import sys
from matplotlib import rc
rc('text', usetex=True)
font = {'weight':'normal','size':12,'family':'sans-serif','sans-serif':['Helvetica']}
rc('font', **font)

hdu1 = fits.open('XCO.fits')[0]

xcenter=84
ycenter=-6
wid = 1.5
hei = 2.4
xpanels = 1
ypanels = 1
fig=plt.figure(figsize=(3*xpanels*1.1*(wid/(wid+hei))*10.,3*ypanels/1.1*(hei/(wid+hei))*10.))
ff = aplpy.FITSFigure(hdu1, figure=fig)
ff.recenter(xcenter,ycenter,width=wid,height=hei) 
ff.set_theme('publication')
#ff.set_system_latex(True)
maxcolor = np.nanmax(hdu1.data)
ff.show_colorscale(cmap='gist_heat', stretch='log')
ff.show_regions('olay4.reg')
#ff.show_contour(mask_hdu, levels=1, colors='yellow', linewidths=0.1)
ff.add_colorbar() 
ff.colorbar.set_font(size=12)
ff.colorbar.set_pad(0.5)
ff.colorbar.set_axis_label_text(r'$\rm cm^{-2}~(K~km~s^{-1})^{-1}$')
ff.set_tick_labels_font(size=12)
ff.set_axis_labels_font(size=12)
ff.add_scalebar(0.286,corner='right',pad=2) # degree for 2pc at 400 pc
ff.scalebar.set_label('2 pc') 
ff.scalebar.set_font_size(12) 
beamx = 83.41442439
beamy = -7.022846568
bmaj = 18./3600.
bmin = 18./3600.
beamangle = 0
ff.show_ellipses(beamx+1.2,beamy,bmaj,bmin,angle=beamangle-90,facecolor='black',edgecolor='black')
ff.add_label(beamx+1.0,beamy+2.0,r'$X_{\rm CO}$',size=12,weight='bold')
pdfname = 'XCO.pdf'

inset = 1
if inset == 1:
    from matplotlib import rc
    rc('text', usetex=True)
    font = {'weight' : 'normal','size':12,'family':'sans-serif','sans-serif':['Helvetica']}
    rc('font', **font)
    ax = fig.add_axes([0.58,0.16,0.21,0.1])
    hdu = fits.open('XCO.fits')[0]
    xcodata = hdu.data/1.e20
    xx = xcodata[~np.isnan(xcodata)]
    #xx = xxx[xxx<1.e2]
    x = xx[xx>0]
    # the histogram of the data
    n, bins, patches = plt.hist(x, 100, histtype='step', color='k')
    #print n,bins
    #plt.xscale('log')
    #plt.yscale('log')
    plt.xlabel(r'$X_{\rm CO}~(10^{20}~{\rm cm}^{-2}~{\rm (K~km~s^{-1})}^{-1})$')
    plt.ylabel('counts')
    plt.xlim(0,4.)
    plt.grid(True)

os.system('rm '+pdfname)
plt.savefig(pdfname,bbox_inches='tight')
os.system('open '+pdfname)
os.system('cp '+pdfname+os.path.expandvars(' /Users/shuokong/GoogleDrive/imagesSFE/'))

