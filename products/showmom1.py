import aplpy
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import sys

hdu1 = fits.open('mom1_12co_pix_2_Tmb.fits')[0]
xcenter=84.
ycenter=-6.
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
ff.show_colorscale(cmap='jet', vmin=5, vmax=13, stretch='linear')
ff.show_regions('olay2.reg')
#ff.show_contour(mask_hdu, levels=1, colors='yellow', linewidths=0.1)
ff.add_colorbar() 
ff.colorbar.set_font(size=12)
ff.colorbar.set_pad(0.5)
ff.colorbar.set_axis_label_text('km s$^{-1}$')
ff.colorbar.set_font(size=12)
ff.set_tick_labels_font(size=12)
ff.set_axis_labels_font(size=12)
ff.add_scalebar(0.286,corner='bottom right',pad=10) # degree for 2pc at 400 pc
ff.scalebar.set_label('2 pc') 
ff.scalebar.set_font_size(12) 
beamx = 83.41442439
beamy = -7.022846568
bmaj = hdu1.header['BMAJ']
bmin = hdu1.header['BMIN']
beamangle = hdu1.header['BPA'] 
ff.show_ellipses(beamx,beamy,bmaj,bmin,angle=beamangle-90,facecolor='black',edgecolor='black')
ff.add_label(beamx+1.12,beamy+1.65,'1st-moment $^{12}$CO(1-0)',size=12,weight='bold')
ax1blx,ax1bly = ff._ax1.transAxes.transform((0,0))
ax1trx,ax1try = ff._ax1.transAxes.transform((1,1))
figtrx,figtry = fig.transFigure.transform((1,1))
pos = ff._ax1.get_position() # image ratio
print pos.x0,pos.x1,pos.width
print pos.y0,pos.y1,pos.height
ffax1x0 = pos.x0
ffax1y0 = pos.y0
ffax1x1 = pos.x1
ffax1y1 = pos.y1
ffax1xc = (ffax1x0+ffax1x1)/2.
ffax1yc = (ffax1y0+ffax1y1)/2.
ffax1xfactor = wid/(ffax1x1-ffax1x0)
ffax1yfactor = hei/(ffax1y1-ffax1y0)
## OMC-2
boxcenterx = 83.87321652
boxcentery = -5.089496481
boxwidth = 0.1565160
boxheight = 0.0731419
ff.show_rectangles([boxcenterx],[boxcentery],width=boxwidth,height=boxheight,linestyles='dashed',color='k')
wcsboxtopleftx = boxcenterx + boxwidth/2.
wcsboxtoplefty = boxcentery + boxheight/2.
wcsboxbottomleftx = boxcenterx + boxwidth/2.
wcsboxbottomlefty = boxcentery - boxheight/2.
zoombottomleftx = 0.175
zoombottomlefty = 0.77
zoomwidth = 0.25
zoomheight = zoomwidth*(1.1*wid)/(hei/1.1)/boxwidth*boxheight
wcszoomtoprightx = (ffax1xc - (zoombottomleftx + zoomwidth)) * ffax1xfactor + xcenter
wcszoomtoprighty = ((zoombottomlefty + zoomheight) - ffax1yc) * ffax1yfactor + ycenter
wcszoombottomrightx = (ffax1xc - (zoombottomleftx + zoomwidth)) * ffax1xfactor + xcenter
wcszoombottomrighty = (zoombottomlefty - ffax1yc) * ffax1yfactor + ycenter
f2 = aplpy.FITSFigure(hdu1, figure=fig, subplot=[zoombottomleftx,zoombottomlefty,zoomwidth,zoomheight])
f2.set_theme('publication')
f2.recenter(boxcenterx,boxcentery,width=boxwidth,height=boxheight)
f2.show_colorscale(cmap='jet', vmin=5, vmax=13, stretch='linear')
f2.axis_labels.hide()
f2.tick_labels.hide()
f2.ticks.hide()
f2.frame.set_color('black')
ff.show_lines([np.array([[wcsboxtopleftx,wcszoomtoprightx-0.05],[wcsboxtoplefty,wcszoomtoprighty]])],linestyles='dashed',color='k')
ff.show_lines([np.array([[wcsboxbottomleftx,wcszoombottomrightx-0.05],[wcsboxbottomlefty,wcszoombottomrighty]])],linestyles='dashed',color='k')
###
## L1641-N
boxcenterx = 84.07050256
boxcentery = -6.396960862
boxwidth = 0.0742788
boxheight = 0.1337776
ff.show_rectangles([boxcenterx],[boxcentery],width=boxwidth,height=boxheight,linestyles='dashed',color='k')
boxtopleftx = boxcenterx + boxwidth/2.
boxtoplefty = boxcentery + boxheight/2.
boxbottomleftx = boxcenterx + boxwidth/2.
boxbottomlefty = boxcentery - boxheight/2.
zoombottomleftx = 0.18
zoombottomlefty = 0.35
zoomwidth = 0.12
zoomheight = zoomwidth*(1.1*wid)/(hei/1.1)/boxwidth*boxheight
zoomtoprightx = (ffax1xc - (zoombottomleftx + zoomwidth)) * ffax1xfactor + xcenter
zoomtoprighty = ((zoombottomlefty + zoomheight) - ffax1yc) * ffax1yfactor + ycenter
zoombottomrightx = (ffax1xc - (zoombottomleftx + zoomwidth)) * ffax1xfactor + xcenter
zoombottomrighty = (zoombottomlefty - ffax1yc) * ffax1yfactor + ycenter
f3 = aplpy.FITSFigure(hdu1, figure=fig, subplot=[zoombottomleftx,zoombottomlefty,zoomwidth,zoomheight])
f3.set_theme('publication')
f3.recenter(boxcenterx,boxcentery,width=boxwidth,height=boxheight)
f3.show_colorscale(cmap='jet', vmin=5, vmax=13, stretch='linear')
f3.axis_labels.hide()
f3.tick_labels.hide()
f3.ticks.hide()
f3.frame.set_color('black')
ff.show_lines([np.array([[boxtopleftx,zoomtoprightx],[boxtoplefty,zoomtoprighty]])],linestyles='dashed',color='k')
ff.show_lines([np.array([[boxbottomleftx,zoombottomrightx],[boxbottomlefty,zoombottomrighty]])],linestyles='dashed',color='k')
####
## V380
boxcenterx = 84.15042383
boxcentery = -6.644701128
boxwidth = 0.0426345
boxheight = 0.0865954
ff.show_rectangles([boxcenterx],[boxcentery],width=boxwidth,height=boxheight,linestyles='dashed',color='k')
boxtoprightx = boxcenterx - boxwidth/2.
boxtoprighty = boxcentery + boxheight/2.
boxbottomrightx = boxcenterx - boxwidth/2.
boxbottomrighty = boxcentery - boxheight/2.
zoombottomleftx = 0.65
zoombottomlefty = 0.25
zoomwidth = 0.12
zoomheight = zoomwidth*(1.1*wid)/(hei/1.1)/boxwidth*boxheight
wcszoomtopleftx = (ffax1xc - zoombottomleftx) * ffax1xfactor + xcenter
wcszoomtoplefty = ((zoombottomlefty + zoomheight) - ffax1yc) * ffax1yfactor + ycenter
wcszoombottomleftx = (ffax1xc - zoombottomleftx) * ffax1xfactor + xcenter
wcszoombottomlefty = (zoombottomlefty - ffax1yc) * ffax1yfactor + ycenter
f4 = aplpy.FITSFigure(hdu1, figure=fig, subplot=[zoombottomleftx,zoombottomlefty,zoomwidth,zoomheight])
f4.set_theme('publication')
f4.recenter(boxcenterx,boxcentery,width=boxwidth,height=boxheight)
f4.show_colorscale(cmap='jet', vmin=5, vmax=13, stretch='linear')
f4.axis_labels.hide()
f4.tick_labels.hide()
f4.ticks.hide()
f4.frame.set_color('black')
ff.show_lines([np.array([[boxtoprightx,wcszoomtopleftx-0.1],[boxtoprighty,wcszoomtoplefty]])],linestyles='dashed',color='k')
ff.show_lines([np.array([[boxbottomrightx,wcszoombottomleftx-0.1],[boxbottomrighty,wcszoombottomlefty]])],linestyles='dashed',color='k')
###
pdfname = 'mom1_12co_pix_2_Tmb.pdf'
os.system('rm '+pdfname)
plt.savefig(pdfname,bbox_inches='tight')
os.system('open '+pdfname)
os.system('cp '+pdfname+os.path.expandvars(' /Users/shuokong/GoogleDrive/imagesCARMAOrion/'))
sys.exit()

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

plt.xlabel(r'$v_{\rm lsr}~\rm km~s^{-1}$')
plt.ylabel('probability density')
plt.xlim(0,20)
ax.xaxis.set_tick_params(top='on',labeltop='on',direction='in')
ax.yaxis.set_tick_params(direction='in')
#plt.grid(True)
pdfname = 'mom1_12co_hist.pdf'
os.system('rm '+pdfname)
plt.savefig(pdfname,bbox_inches='tight')
os.system('open '+pdfname)
os.system('cp '+pdfname+os.path.expandvars(' /Users/shuokong/GoogleDrive/imagesCARMAOrion/'))

