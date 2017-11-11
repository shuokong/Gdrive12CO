rm -rf north_mask_12co_pix_2_Tmb.mir
rm -rf central_mask_12co_pix_2_Tmb.mir
rm -rf south_mask_12co_pix_2_Tmb.mir
rm -rf furthersouth_mask_12co_pix_2_Tmb.mir
imsub in=mask_imfit_12co_pix_2_Tmb.mir region="abspix,boxes(1,3349,2557,4273)" out=north_mask_12co_pix_2_Tmb.mir
imsub in=mask_imfit_12co_pix_2_Tmb.mir region="abspix,boxes(1,2910,2557,3348)" out=central_mask_12co_pix_2_Tmb.mir
imsub in=mask_imfit_12co_pix_2_Tmb.mir region="abspix,boxes(1,1620,2557,2909)" out=south_mask_12co_pix_2_Tmb.mir
imsub in=mask_imfit_12co_pix_2_Tmb.mir region="abspix,boxes(1,1,2557,1619)" out=furthersouth_mask_12co_pix_2_Tmb.mir
fits op=xyout in=north_mask_12co_pix_2_Tmb.mir out=north_mask_12co_pix_2_Tmb.fits
fits op=xyout in=central_mask_12co_pix_2_Tmb.mir out=central_mask_12co_pix_2_Tmb.fits
fits op=xyout in=south_mask_12co_pix_2_Tmb.mir out=south_mask_12co_pix_2_Tmb.fits
fits op=xyout in=furthersouth_mask_12co_pix_2_Tmb.mir out=furthersouth_mask_12co_pix_2_Tmb.fits
