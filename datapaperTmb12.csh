#!/bin/csh

set images = 0
set mom0 = 0
set mom1three = 0
set mom2three = 0
set noisetype = "vary"
set mom1five = 1
set mom2five = 1
set velocityrange = 0

### Tpeak images for 12co
if ($images) then
  rm -rf products/peak_12co_pix_2_Tmb.mir
  moment in=products/mask_12co_pix_2_Tmb.mir mom=-2 out=products/peak_12co_pix_2_Tmb.mir
  fits in=products/peak_12co_pix_2_Tmb.mir op=xyout out=products/peak_12co_pix_2_Tmb.fits
endif

### 0th-moment images for 12co
if ($mom0) then
  rm -rf products/mom0_12co_pix_2_Tmb.mir
  moment in=products/mask_12co_pix_2_Tmb.mir mom=0 region="kms,images(0,17)" out=products/mom0_12co_pix_2_Tmb.mir
  fits in=products/mom0_12co_pix_2_Tmb.mir op=xyout out=products/mom0_12co_pix_2_Tmb.fits
endif

### velocity range 0th-moment images for 12co
if ($velocityrange) then

  set mom0name = "mom0_28_37"
  #set mom0region = "abspix,images(28,37)"
  set mom0region = "kms,images(4.81,7.06)"
  rm -rf products/${mom0name}_12co_pix_2_Tmb.mir
  moment in=products/mask_12co_pix_2_Tmb.mir mom=0 out=products/${mom0name}_12co_pix_2_Tmb.mir region=${mom0region}
  rm -rf products/${mom0name}_12co_pix_2_Tmb.fits
  fits in=products/${mom0name}_12co_pix_2_Tmb.mir op=xyout out=products/${mom0name}_12co_pix_2_Tmb.fits

  set mom0name = "mom0_38_47"
  #set mom0region = "abspix,images(38,47)"
  set mom0region = "kms,images(7.31,9.56)"
  rm -rf products/${mom0name}_12co_pix_2_Tmb.mir
  moment in=products/mask_12co_pix_2_Tmb.mir mom=0 out=products/${mom0name}_12co_pix_2_Tmb.mir region=${mom0region}
  rm -rf products/${mom0name}_12co_pix_2_Tmb.fits
  fits in=products/${mom0name}_12co_pix_2_Tmb.mir op=xyout out=products/${mom0name}_12co_pix_2_Tmb.fits

  set mom0name = "mom0_48_57"
  #set mom0region = "abspix,images(48,57)"
  set mom0region = "kms,images(9.81,12.07)"
  rm -rf products/${mom0name}_12co_pix_2_Tmb.mir
  moment in=products/mask_12co_pix_2_Tmb.mir mom=0 out=products/${mom0name}_12co_pix_2_Tmb.mir region=${mom0region}
  rm -rf products/${mom0name}_12co_pix_2_Tmb.fits
  fits in=products/${mom0name}_12co_pix_2_Tmb.mir op=xyout out=products/${mom0name}_12co_pix_2_Tmb.fits

endif

### 1st-moment images for 12co

# clip at 3sigma
if ($mom1three) then
  rm -rf products/mom1_12co_pix_2_Tmb.mir
  moment in=products/clip3sigma_mask_12co_pix_2_Tmb.mir mom=1 out=products/mom1_12co_pix_2_Tmb.mir 
  fits in=products/mom1_12co_pix_2_Tmb.mir op=xyout out=products/mom1_12co_pix_2_Tmb.fits
endif

# clip at 5sigma
if ($mom1five) then
  rm -rf products/mom1_12co_pix_2_Tmb.mir
  moment in=products/clip5sigma_mask_12co_pix_2_Tmb.mir mom=1 out=products/mom1_12co_pix_2_Tmb.mir 
  fits in=products/mom1_12co_pix_2_Tmb.mir op=xyout out=products/mom1_12co_pix_2_Tmb.fits
endif

### 2nd-moment images for 12co

# clip at 3sigma
if ($mom2three) then
  rm -rf products/mom2_12co_pix_2_Tmb.mir
  moment in=products/clip3sigma_mask_12co_pix_2_Tmb.mir mom=2 out=products/mom2_12co_pix_2_Tmb.mir 
  fits in=products/mom2_12co_pix_2_Tmb.mir op=xyout out=products/mom2_12co_pix_2_Tmb.fits
endif

# clip at 5sigma
if ($mom2five) then
  rm -rf products/mom2_12co_pix_2_Tmb.mir
  moment in=products/clip5sigma_mask_12co_pix_2_Tmb.mir mom=2 out=products/mom2_12co_pix_2_Tmb.mir 
  fits in=products/mom2_12co_pix_2_Tmb.mir op=xyout out=products/mom2_12co_pix_2_Tmb.fits
endif

