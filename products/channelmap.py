import numpy as np
import os
import sys
import math
import aplpy
import matplotlib as mpl
import matplotlib.pyplot as plt
import pyfits

fitsfiles={'color':{'fname':'chan1_mask_imfit_12co_pix_2_Tmb.fits','title':'12CO(1-0)','bmaj':0,'bmin':0,'galpa':0},
        'template':{'fname':'chan1_mask_imfit_12co_pix_2_Tmb.fits'},
         'channel':{'fname':'mask_imfit_12co_pix_2_Tmb.fits','title':r'12CO(1-0)','mincolor':0,'maxcolor':200},
           }

os.system('cp '+fitsfiles['template']['fname']+' '+'template_'+fitsfiles['template']['fname'])
templatehdulist = pyfits.open('template_'+fitsfiles['template']['fname'])
templatedata = templatehdulist[0].data
channelhdulist = pyfits.open(fitsfiles['channel']['fname'])
channeldata = channelhdulist[0].data

def currentvel(hdulistheader,currentchannel):
    vref = hdulistheader['CRVAL3']
    vdelt= hdulistheader['CDELT3']
    return (vref + (currentchannel - 1) * vdelt)/1.e3

ypanels=3
xpanels=4
aspectratio=1.5
xcenter=28.323
ycenter=0.0675

firstchannelstart=39
lastchannel=50

for startchan in range(firstchannelstart,lastchannel,ypanels*xpanels):

    channelstart=startchan # start from which channel, note the different starting index. tbd
    currentchannel=channelstart
    pdfname='chan12co'+str(startchan)+'.pdf'
    
    fig=plt.figure(figsize=(3*xpanels,3*ypanels*aspectratio))
    for j in range(0,ypanels): # this order first follows row
        for i in range(0,xpanels):
            templatedata[0,0,:,:]=channeldata[0,currentchannel-1,:,:]
            templatehdulist.writeto('template_channel.fits',output_verify='exception',clobber=True,checksum=False) # use this as template to output every single channel
            subpos=[0.1+0.8/xpanels*i,0.1+0.9/ypanels*(ypanels-1-j),0.8/xpanels,0.9/ypanels]
            ff = aplpy.FITSFigure('template_channel.fits',figure=fig,subplot=subpos)
            ff.set_theme('publication')
            mincolor = fitsfiles['channel']['mincolor']
            maxcolor = fitsfiles['channel']['maxcolor']
            ff.show_colorscale(vmin=mincolor,vmax=maxcolor,cmap='afmhot',stretch='sqrt')
            ff.tick_labels.set_yformat('dd:mm')
            ff.tick_labels.set_xformat('hh:mm')
            beamx = 83.41442439
            beamy = -7.022846568
            bmaj = channelhdulist[0].header['BMAJ']
            bmin = channelhdulist[0].header['BMIN']
            beamangle = channelhdulist[0].header['BPA'] 
            ff.show_ellipses(beamx,beamy,bmaj,bmin,angle=beamangle-90,facecolor='black',edgecolor='black')
            ff.add_label(beamx+1.2,beamy+2.0,'{0:.2f}'.format(currentvel(channelhdulist[0].header,currentchannel))+'km/s',color='black',horizontalalignment='left')
            if j != ypanels-1:
                ff.hide_xaxis_label()
                ff.hide_xtick_labels()
            if i != 0:
                ff.hide_yaxis_label()
                ff.hide_ytick_labels()
            currentchannel = currentchannel + 1
            os.system('rm template_channel.fits')
    ax1 = fig.add_axes([0.92,0.7,0.01,0.9/ypanels])
    cmap = mpl.cm.afmhot
    norm = mpl.colors.Normalize(vmin=mincolor, vmax=maxcolor)
    cb1 = mpl.colorbar.ColorbarBase(ax1, cmap=cmap,norm=norm,orientation='vertical')#,ticks=colorticks)
    
    # close and save file
    fig.canvas.draw()
    os.system('rm '+pdfname)
    #plt.savefig(pdfname)
    plt.savefig(pdfname,bbox_inches='tight')
    plt.close(fig)
    os.system('open '+pdfname)

templatehdulist.close()
channelhdulist.close()


