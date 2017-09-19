#!/bin/csh

smir
rm -r carma.mir
maths exp="<products/12co_CARMAonly_pix_1.mir>" region="abspix,boxes(2219,5377,3818,6976)(45,46)" out=carma.mir
fits in=carma.mir op=xyout out=carma.fits # for CASA importfits, remember to dropstokes
#rm -r convol_carma.mir
#convol map=carma.mir fwhm=21.6 out=convol_carma.mir
#fits in=convol_carma.mir op=xyout out=convol_carma.fits # for CASA importfits, remember to dropstokes
rm -r nro_jy.mir
maths exp="<regrid_12CO_specsmooth.mir>*5.0" region="abspix,images(45,46)" out=nro_jy.mir # scale to Jy/beam
rm -r regrid_nro_jy.mir
regrid in=nro_jy.mir tin=carma.mir out=regrid_nro_jy.mir
fits in=regrid_nro_jy.mir op=xyout out=regrid_nro_jy.fits # change header in bunit.py
python bunit.py
#rm -r regrid_nro_jy.mir
#fits in=regrid_nro_jy.fits op=xyin out=regrid_nro_jy.mir
#rm -r convol_regrid_nro_jy.mir
#convol map=regrid_nro_jy.mir fwhm="7.83,6.10" pa=-10.57 out=convol_regrid_nro_jy.mir # from casaviewer
#fits in=convol_regrid_nro_jy.mir op=xyout out=convol_regrid_nro_jy.fits # for CASA importfits

