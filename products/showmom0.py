import aplpy
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

pvra = [83.52329236,83.57316692,83.62030445,83.66706130,83.71382045,83.75252857,83.79620141,83.82111418,83.84564682,83.86251383,83.86210348,83.85289673,83.84292146,83.82604083,83.80992492,83.80935538,83.80014058,83.79092437,83.77326557,83.76327770,83.74561138,83.73638688,83.73637222,83.74557319,83.75323795,83.77088618,83.79621755,83.82001665,83.84612392,83.87838040]
pvdec = [-4.876200218,-4.879461026,-4.897820323,-4.915411506,-4.93299871,-4.965857804,-4.99067018,-5.033833723,-5.076613716,-5.123974925,-5.173573767,-5.222459592,-5.271344718,-5.318700697,-5.36452826,-5.412955261,-5.461988054,-5.510106789,-5.555931851,-5.605577113,-5.6519109,-5.701555547,-5.752730272,-5.801156183,-5.84927762,-5.897401317,-5.940943148,-5.986011267,-6.029551074,-6.068507208]
pvline = np.array([pvra,pvdec])

hdu1 = fits.open('mom0_12co_pix_2_Tmb.fits')[0]

mom0 = 1
histogram = 0

if mom0 == 1:
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
    mincolor = 0.001
    ff.show_colorscale(cmap='afmhot', pmin=0.25, vmax=1000, stretch='sqrt')
    #ff.show_regions('olay.reg')
    ff.show_regions('olay1.reg')
    #ff.show_contour(mask_hdu, levels=1, colors='yellow', linewidths=0.1)
    ff.add_colorbar() 
    ff.colorbar.set_font(size=12)
    ff.colorbar.set_pad(0.5)
    ff.colorbar.set_axis_label_text('K km s$^{-1}$')
    ff.set_tick_labels_font(size=12)
    ff.set_axis_labels_font(size=12)
    ff.add_scalebar(0.286,corner='bottom right',pad=10) # degree for 2pc at 400 pc
#    ff.scalebar.set_corner('left') 
    ff.scalebar.set_label('2 pc') 
    ff.scalebar.set_font_size(12) 
    beamx = 83.41442439
    beamy = -7.022846568
    bmaj = hdu1.header['BMAJ']
    bmin = hdu1.header['BMIN']
    beamangle = hdu1.header['BPA'] 
    ff.show_ellipses(beamx,beamy,bmaj,bmin,angle=beamangle-90,facecolor='black',edgecolor='black')
    ff.add_label(beamx+1.0,beamy+2.0,'0th-moment $^{12}$CO(1-0)',size=12,weight='bold')
    #ff.tick_labels.set_xformat('dd')
    #ff.tick_labels.set_yformat('dd')
    pos = ff._ax1.get_position() # image ratio
    ffax1x0 = pos.x0
    ffax1y0 = pos.y0
    ffax1x1 = pos.x1
    ffax1y1 = pos.y1
    ffax1xc = (ffax1x0+ffax1x1)/2.
    ffax1yc = (ffax1y0+ffax1y1)/2.
    ffax1xfactor = wid/(ffax1x1-ffax1x0)
    ffax1yfactor = hei/(ffax1y1-ffax1y0)
    ##
    boxcenterx = 83.95016414
    boxcentery = -5.654848646
    boxwidth = 0.2056964
    boxheight = 0.3677828
    ff.show_rectangles([boxcenterx],[boxcentery],width=boxwidth,height=boxheight,linestyles='dashed',color='k')
    boxtopleftx = boxcenterx + boxwidth/2.
    boxtoplefty = boxcentery + boxheight/2.
    boxbottomleftx = boxcenterx + boxwidth/2.
    boxbottomlefty = boxcentery - boxheight/2.
    zoombottomleftx = 0.175
    zoombottomlefty = 0.5
    zoomwidth = 0.15
    zoomheight = zoomwidth*wid/hei/boxwidth*boxheight
    zoomtoprightx = (ffax1xc - (zoombottomleftx + zoomwidth)) * ffax1xfactor + xcenter
    zoomtoprighty = ((zoombottomlefty + zoomheight) - ffax1yc) * ffax1yfactor + ycenter
    zoombottomrightx = (ffax1xc - (zoombottomleftx + zoomwidth)) * ffax1xfactor + xcenter
    zoombottomrighty = (zoombottomlefty - ffax1yc) * ffax1yfactor + ycenter
    f2 = aplpy.FITSFigure(hdu1, figure=fig, subplot=[zoombottomleftx,zoombottomlefty,zoomwidth,zoomheight])
    f2.set_theme('publication')
    f2.recenter(boxcenterx,boxcentery,width=boxwidth,height=boxheight)
    f2.show_colorscale(cmap='afmhot', vmin=30, vmax=600, stretch='log')
    f2.axis_labels.hide()
    f2.tick_labels.hide()
    f2.ticks.hide()
    f2.frame.set_color('black')
    ff.show_lines([np.array([[boxtopleftx,zoomtoprightx],[boxtoplefty,zoomtoprighty]])],linestyles='dashed',color='k')
    ff.show_lines([np.array([[boxbottomleftx,zoombottomrightx],[boxbottomlefty,zoombottomrighty]])],linestyles='dashed',color='k')
    ###
    ff.show_lines([pvline],color='blue')
    ff.show_markers(pvra,pvdec,facecolor='blue',edgecolor='none')
    pdfname = 'mom0_12co_pix_2_Tmb.pdf'
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
    
    plt.xlabel(r'$I_{\rm ^{12}CO}~\rm K~km~s^{-1}$')
    plt.ylabel('probability density')
    #plt.xlim(0,20)
    ax.xaxis.set_tick_params(top='on',labeltop='on',direction='in')
    ax.yaxis.set_tick_params(direction='in')
    #plt.grid(True)
    pdfname = 'mom0_12co_hist.pdf'
    os.system('rm '+pdfname)
    plt.savefig(pdfname,bbox_inches='tight')
    os.system('open '+pdfname)
    os.system('cp '+pdfname+os.path.expandvars(' /Users/shuokong/GoogleDrive/imagesCARMAOrion/'))

