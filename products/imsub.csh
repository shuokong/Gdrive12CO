rm -rf north_sen_gt2_12co_pix_2_Tmb.mir
rm -rf central_sen_gt2_12co_pix_2_Tmb.mir
rm -rf south_sen_gt2_12co_pix_2_Tmb.mir
rm -rf furthersouth_sen_gt2_12co_pix_2_Tmb.mir
imsub in=sen_gt2_12co_pix_2_Tmb.mir region="abspix,boxes(1,3349,2557,4273)" out=north_sen_gt2_12co_pix_2_Tmb.mir
imsub in=sen_gt2_12co_pix_2_Tmb.mir region="abspix,boxes(1,2910,2557,3348)" out=central_sen_gt2_12co_pix_2_Tmb.mir
imsub in=sen_gt2_12co_pix_2_Tmb.mir region="abspix,boxes(1,1620,2557,2909)" out=south_sen_gt2_12co_pix_2_Tmb.mir
imsub in=sen_gt2_12co_pix_2_Tmb.mir region="abspix,boxes(1,1,2557,1619)" out=furthersouth_sen_gt2_12co_pix_2_Tmb.mir
fits op=xyout in=north_sen_gt2_12co_pix_2_Tmb.mir out=north_sen_gt2_12co_pix_2_Tmb.fits
fits op=xyout in=central_sen_gt2_12co_pix_2_Tmb.mir out=central_sen_gt2_12co_pix_2_Tmb.fits
fits op=xyout in=south_sen_gt2_12co_pix_2_Tmb.mir out=south_sen_gt2_12co_pix_2_Tmb.fits
fits op=xyout in=furthersouth_sen_gt2_12co_pix_2_Tmb.mir out=furthersouth_sen_gt2_12co_pix_2_Tmb.fits
