fits in=019004.w16.fits op=xyin out=019004.w16.mir
fits in=w16.fits op=xyin out=w16.mir
convol map=019004.w16.mir fwhm=6 out=convol_019004.w16.mir options=final
regrid in=convol_019004.w16.mir tin=w16.mir out=regrid_convol_019004.w16.mir axes="1,2,3"
fits in=regrid_convol_019004.w16.mir op=xyout out=regrid_convol_019004.w16.fits
ds9 regrid_convol_019004.w16.fits w16.fits
