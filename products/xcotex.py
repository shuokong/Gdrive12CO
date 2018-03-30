import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from matplotlib import rc
rc('text', usetex=True)
font = {'weight' : 'normal','size':20,'family':'sans-serif','sans-serif':['Helvetica']}
rc('font', **font)
import math
import pyfits
import statistics_calculation as sc
from scipy import stats

lowtex=math.log(10,10)
hightex=math.log(200,10)
lowi=19.0
highi=22.0

print 'reading fits files'
hdulist1=pyfits.open('mom0_regrid_Stutz_convol18_mask_imfit_12co_pix_2_Tmb.fits')
hdulist2=pyfits.open('carmanro_OrionA_all_spire250_nh_mask_corr_apex.fits')
hdulist3=pyfits.open('regrid_Stutz_convol18_tex12.fits')
hdulist4=pyfits.open('carmanro_OrionA_all_spire250_nh_mask_corr_apex.fits')
print 'finish reading'

print hdulist1[0].shape
print hdulist2[0].shape
print hdulist3[0].shape

mom012=hdulist1[0].data[0,:,:]
nicest=hdulist2[0].data[:,:]
tex=hdulist3[0].data[0,:,:]
av = nicest/9.4e20/2.

hdulist1.close()
hdulist2.close()
hdulist3.close()

hdulist4[0].data = nicest/mom012
hdulist4.writeto('XCO.fits', output_verify='exception', clobber=True, checksum=False)

log_tex=[]
log_xco=[]

#xy=np.loadtxt('boxes.txt',dtype='int',delimiter=',')
#x1=xy[:,0]
#y1=xy[:,1]
#x2=xy[:,2]
#y2=xy[:,3]
#for k in range(0,17): # 0 represents tile 01
#    print 'tile '+str(k+1)
#    for i in range(y1[k],y2[k]+1):
#        for j in range(x1[k],x2[k]+1):
#            if mom012[i,j] > 0 and nicest[i,j] > 0 and tex[i,j] > 0:
#                log_xco.append(math.log(nicest[i,j]*9.4e20/(mom012[i,j]/0.7),10))
#                log_tex.append(math.log(tex[i,j],10))

usedata = (tex>2.75) & (~np.isnan(tex)) & (av>3)
nan_log_xco = np.log10(nicest/mom012)
nan_log_tex = np.log10(tex)
log_xco = nan_log_xco[usedata]
log_tex = nan_log_tex[usedata]

bintex=(hightex-lowtex)/10.
binlowtex=lowtex
binhightex=hightex
binxtex,binytex,yerrtex=sc.sk_bin(bintex,binlowtex,binhightex+bintex,log_tex,log_xco)

print 'plotting'
p=plt.figure(figsize=(7,6))
plt.subplots_adjust(top=0.88,bottom=0.12,left=0.15,right=0.97)

ax1=p.add_subplot(111)
plt.text(0.05, 0.95,'(b)',horizontalalignment='center',verticalalignment='center',transform = ax1.transAxes)
ax1.plot(log_tex,log_xco,'k.',zorder=1,markersize=5,rasterized=True)
ax1.errorbar(binxtex,binytex,yerr=yerrtex,fmt='b.',markersize=7,barsabove=True,zorder=3,elinewidth=1.5,markeredgewidth=1.5,capsize=3)
# fit
## unbinned
slope, intercept, r_value, p_value, std_err = stats.linregress(log_tex,log_xco)
print slope,intercept,r_value
xx=np.arange(lowtex,hightex+bintex,bintex)
yy=xx*slope+intercept
#plt.plot(xx,yy,'r-',linewidth=3)
## binned
slope, intercept, r_value, p_value, std_err = stats.linregress(binxtex,binytex)
print slope,intercept,r_value
xx=np.arange(lowtex,hightex+bintex,bintex)
yy=xx*slope+intercept
plt.plot(xx,yy,'b-',linewidth=3)
# end fit
ax1.set_ylim(lowi,highi)
ax1.set_xlim(lowtex,hightex)
ax1.set_xlabel(r'$\rm log(T_{ex}~(K))$')
ax1.set_ylabel(r'$\rm log(X_{CO}~(cm^{-2}~(K~km~s^{-1})^{-1}))$')
ax2=ax1.twiny()
ax1Xs = ax1.get_xticks()
ax2Xs = []
for X in ax1Xs:
    ax2Xs.append("{0:.1f}".format(10.**X))
ax2.set_xticks(ax1Xs)
ax2.set_xbound(ax1.get_xbound())
ax2.set_xticklabels(ax2Xs)
ax2.set_xlabel(r'$\rm T_{ex}~(K)$')

print 'finish plotting'

print 'saving files'
os.system('rm xcotex.pdf')
plt.savefig('xcotex.pdf',dpi=400)
os.system('open xcotex.pdf')
os.system('cp color_12co_NH_tex.pdf ~/GoogleDrive/imagesSFE/')
#plt.show()


