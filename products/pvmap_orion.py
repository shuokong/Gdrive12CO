import numpy as np
import math
import scipy.optimize as optimize
import matplotlib.pylab as plt

#import pyspeckit
import pyfits
import pylab
import aplpy
from numpy import ma
from matplotlib.pyplot import step, legend, xlim, ylim, show
import os
import radiomodule_orion as rmod
import posvel_orion as pv
#from matplotlib.backends.backend_pdf import PdfPages

def main():

    name_cube = 'mask_imfit_12co_pix_2_Tmb.fits'
    name_out = 'pv_mask_imfit_12co_pix_2_Tmb.fits'
    
    ra_list = np.array([83.52329236,83.57316692,83.62030445,83.66706130,83.71382045,83.75252857,83.79620141,83.82111418,83.84564682,83.86251383,83.86210348,83.85289673,83.84292146,83.82604083,83.80992492,83.80935538,83.80014058,83.79092437,83.77326557,83.76327770,83.74561138,83.73638688,83.73637222,83.74557319,83.75323795,83.77088618,83.79621755,83.82001665,83.84612392,83.87838040])
    
    dec_list = np.array([-4.876200218,-4.879461026,-4.897820323,-4.915411506,-4.93299871,-4.965857804,-4.99067018,-5.033833723,-5.076613716,-5.123974925,-5.173573767,-5.222459592,-5.271344718,-5.318700697,-5.36452826,-5.412955261,-5.461988054,-5.510106789,-5.555931851,-5.605577113,-5.6519109,-5.701555547,-5.752730272,-5.801156183,-5.84927762,-5.897401317,-5.940943148,-5.986011267,-6.029551074,-6.068507208])

    vel_range = [0,16] #kms
    
    vel_rms = [-2,0.5] #kms
    
    mapa_maker = 'miriad'
    
    beam_param = []
    
    center_coord = [83.806,-5.368]
    
    
    pvmap_orion = pv.pos_vel(name_cube,name_out,ra_list,dec_list,vel_range,vel_rms,mapa_maker,beam_param,center_coord)
    
    fig=plt.figure()
    gc=aplpy.FITSFigure(name_out,dimensions=[0,1],figure=fig,hdu=0)
    gc.show_colorscale(aspect='auto')
    
    gc.ticks.show()
    gc.ticks.set_color('black')
    gc.ticks.set_length(10)
    gc.ticks.set_linewidth(2)
    gc.add_colorbar()
    gc.set_theme('publication')
    gc.colorbar.set_width(0.5)
    plt.savefig('pv12.pdf',bbox_inches='tight')
    #plt.show()
    





if __name__=='__main__':
  main()

