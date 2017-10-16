import aplpy
import os
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import sys

peak = 1
histogram = 0

#hdu1 = fits.open('peak_12co_pix_2_Tmb.fits')[0]
hdu1 = fits.open('subregion_peak_12co_pix_2_Tmb.fits')[0]

if peak == 1:
    xcenter=84
    ycenter=-6
    wid = 1.5
    hei = 2.4
    xpanels = 1
    ypanels = 1
    #fig=plt.figure(figsize=(5*xpanels*1.*(wid/(wid+hei))*10.,5*ypanels/1.1*(hei/(wid+hei))*10.))
    #ff = aplpy.FITSFigure(hdu1, figure=fig)
    ff = aplpy.FITSFigure(hdu1)
    #ff.recenter(xcenter,ycenter,width=wid,height=hei) 
    ff.set_theme('publication')
    #ff.set_system_latex(True)
    maxcolor = np.nanmax(hdu1.data)
    ff.show_colorscale(cmap='gist_heat', vmin=0, vmax=maxcolor, stretch='sqrt')
    ff.axis_labels.hide()
    ff.tick_labels.hide()
    ff.ticks.hide()
    #ff.show_regions('olay.reg')
    #ff.show_contour(mask_hdu, levels=1, colors='yellow', linewidths=0.1)
    #ff.add_colorbar() 
    #ff.colorbar.set_font(size=16)
    #ff.colorbar.set_pad(0.5)
    ff.set_tick_labels_font(size='large')
    ff.set_axis_labels_font(size='large')
    #ff.add_scalebar(0.0115) # degree for 1pc at 5kpc
    #ff.scalebar.set_corner('top right') 
    #ff.scalebar.set_label('1 pc (41")') 
    #ff.scalebar.set_font_size(16) 
    #ff.tick_labels.set_xformat('dd')
    #ff.tick_labels.set_yformat('dd')
    pdfname = 'application_peak_12co_pix_2_Tmb.pdf'
    os.system('rm '+pdfname)
    plt.savefig(pdfname,bbox_inches='tight')
    os.system('open '+pdfname)
    os.system('cp '+pdfname+os.path.expandvars(' /Users/shuokong/GoogleDrive/imagesCARMAOrion/'))

if histogram == 1:
    from matplotlib import rc
    rc('text', usetex=True)
    font = {'weight':'normal','size':12,'family':'sans-serif','sans-serif':['Helvetica']}
    rc('font', **font)
    
    print hdu1.data.shape
    #sys.exit()
    x = hdu1.data[~np.isnan(hdu1.data)]
    p=plt.figure(figsize=(7,6))
    fig, ax = plt.subplots(1,1)
    # the histogram of the data
    n, bins, patches = plt.hist(x, 100, normed=True, histtype='step', color='k')
    #print n,bins
    
    plt.xlabel(r'$T_{\rm peak,12}~\rm K$')
    plt.ylabel('probability density')
    #plt.xlim(0,20)
    ax.xaxis.set_tick_params(top='on',labeltop='on',direction='in')
    ax.yaxis.set_tick_params(direction='in')
    #plt.grid(True)
    pdfname = 'peak_12co_hist.pdf'
    os.system('rm '+pdfname)
    plt.savefig(pdfname,bbox_inches='tight')
    os.system('open '+pdfname)
    os.system('cp '+pdfname+os.path.expandvars(' /Users/shuokong/GoogleDrive/imagesCARMAOrion/'))
