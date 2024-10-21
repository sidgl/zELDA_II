---
title: 'zELDA : A python package for modeling and fitting Lyman-alpha line profiles.'
tags:
  - Python
  - astronomy
  - radiative transfer
  - galaxies
authors:
  - name: Siddhrtha Gurung-Lopez    
    orcid: 0000-0001-9333-8470
    affiliation: "1, 2" # (Multiple affiliations must be quoted)
    corresponding: true # (This is how to denote the corresponding author)
  - name: Chris Byrohl
    affiliation: "3" # (Multiple affiliations must be quoted)
  - name: Max Gronke
    affiliation: "4"
  - given-names: Ludwig
    dropping-particle: van
    surname: Beethoven
    affiliation: 1
affiliations:
 - name: Observatori Astronomic de la Universitat de Valencia, Ed. Instituts d’Investigacio, Parc Cientific. C/ Catedratico Jose Beltran, n2, 46980 Paterna, Valencia, Spain
   index: 1
 - name: Departament d Astronomia i Astrofisica, Universitat de Valencia, 46100 Burjassot, Spain
   index: 2
 - name: Universität Heidelberg, Institut für Theoretische Astrophysik, ZAH, Albert-Ueberle-Str. 2, 69120 Heidelberg, Germany
   index: 3
date: 31 October 2024
bibliography: paper.bib

# Optional fields if submitting to a AAS journal too, see this blog post:
# https://blog.joss.theoj.org/2018/12/a-new-collaboration-with-aas-publishing
#aas-doi: 10.3847/xxxxx <- update this with the DOI from AAS once you know it.
#aas-journal: Astrophysical Journal <- The name of the AAS journal.
---

# Summary

We present `zELDA` (redshift Estimator for Line profiles of Distant Lyman Alpha emitters), an open source code to model and fit Lyman-alpha (Lyα) line profiles. 
The main motivation is to provide the community with an easy to use and fast tool to analyze Lyα line profiles uniformly to improve the understanding of Lyα emitting galaxies. 
In first place, concerning the Lyα line modeling, `zELDA` is based on line profiles of the commonly used 'shell-model' pre-computed with the full Monte Carlo radiative transfer code LyaRT.
The 'shell-model' represents the contribution of the interstellar medium (ISM) and circumgalactic medium (CGM) to the Lyα line profile.
Thus, `zELDA` provides a regular grid of 'shell-model' spectrum ranging expansion velocity from -1000 km/s to 1000 km/s, neutral hydrogen column density from $10^{17.0}cm^{-2}$ to $10^{21.5}cm^{-2}$, dust optical depth  from $10^{-4}$ to 1, intrinsic equivalent width from 0.1 to 1000 Ángstrom and intrinsic line width from 0.01 to 6.0 angstroms.This gives a total of  3,132,000 grid nodes. 
The line Lyα line profiles in an arbitrary position inside the grid is computed via lineal interpolation. 
`zELDA` also includes the algorithms to transform the ideal Lyα line profiles into realistic profiles mocking observations. 
In second place, the fitting of observed line profiles is handled with several methodologies. 
`zELDA` includes the fitting of Lyα line profiles obscured and unobscured by the intergalactic medium (IGM). 
Regarding the unobscured Lyα line profiles, `zELDA` includes an MCMC algorithm powered by the python package `EMCEE` `[@Foreman-Mackey]` and two artificial neural network models trained in mock spectrum. 
Regarding the IGM attenuated Lyα line profiles, `zELDA` includes four artificial neural network models trained with the `zELDA` 'shell-model' grid and the IGM transmission curves from the TNG100 simulation `[@Byrohl2019; @Byrohl_2020]`.

Tutorials on installation and usage can be found at https://zelda-ii.readthedocs.io/index.html. 

# Statement of need

`zELDA` is an open source Python package to model and fit Lyα line profiles. 
On one hand, the  Lyα modeling through the 'shell-model' enables users to populate galaxy simulations with realistic  Lyα line profiles. 
On the other hand, the fitting procedures provide a robust measurement of the shape of the line. 
Moreover, `zELDA` is able to disentangle between the intergalactic and interestelar medium contribution to the  Lyα line profile. 
One of the advantages of `zELDA` is that it can be used seamlessly in different observational configurations, allowing a direct comparison between different surveys and projects. 

`zELDA` is developed to have a user-friendly interface so that it can be used by researchers and students in astronomy courses. 
`zELDA` has been used already in a number of scientific publications `[gurung_lopez_2022; Guaita_2022]`, mainly to fit observational observations. 
`zELDA` will allow researchers to extract the maximum information from their observed Lyα line profiles. 
Moreover, disentangeling the IGM from the ISM contribution will be key in future surveys to understand the Lyα selection function.

coordinate systems in the `Astropy` package [@astropy] (`astropy.units` and
`astropy.coordinates`).


# Installation

`zELDA`, installation is divided in two blocks. First you will need to install the python package.The pyhton package includes all the machine learning models need for fitting and modelling the Lyman-alpha line profiles. In order to install `zELDA`, it can be downloaded from GitHub:

.. code:: python

          $ git clone https://github.com/sidgl/zELDA_II/
          $ cd zELDA_II
          $ pip install .

Another option for the installation is using PyPI: 

.. code:: python

          python3 -m pip install Lya_zelda_II

Once the python pakage is installed, it is necessary to download the grid of Lyman-alpha shell spectrum. The grids are stored in https://zenodo.org/records/4733518. The grids can be downloaded by running

.. code:: python

          $ wget https://zenodo.org/record/4733518/files/Grids.zip

Then, extract the Grids.zip content in the folder in which the grids will be saved and loaded from.

# How to reconstruct IGM attenuated Lyman-alpha line profiles 

In this tutorial we show how fit Lyman-alpha line profiles using deep learning with `zELDA`. The first step is to load the  `zELDA` grids by running

.. code:: python

          import Lya_zelda_II as Lya
          import numpy as np

          your_grids_location = '/This/Folder/Contains/The/Grids/'
          Lya.funcs.Data_location = your_grids_location

          Geometry = 'Thin_Shell_Cont'
          LyaRT_Grid = Lya.load_Grid_Line( Geometry )

where `/This/Folder/Contains/The/Grids/` is the location of your computer where the LyaRT data grids are stored. The redshift and shell model parameters must be set, as well as the quality of the desired mock line profile:

.. code:: python

          # Defining the model parameters:
          z_t      = 3.0   # redshift of the source
          V_t      = 50.0  # Outflow expansion velocity [km/s]
          log_N_t  = 20.   # Logarithmic of the neutral hydrogen column density [cm**-2]
          t_t      = 0.01  # Dust optical depth
          log_EW_t = 1.5   # Logarithmic the intrinsic equivalent width [A]
          W_t      = 0.5   # Intrinsic width of the line [A]
          F_t      = 1.    # Total flux of the line

          # Defining the quality of the line profile:
          PNR_t  = 20.0 # Signal to noise ratio of the maximum of the line.
          FWHM_t = 0.1  # Full width half maximum diluting the line. Mimics finite resolution. [A]
          PIX_t  = 0.1  # Wavelength binning of the line. [A]

          np.random.seed(5) # Set a numpy random seed for replicating this tutorial.

In this tutorial we used a simple toy model for an IGM transmission curve. We set the IGM transmission bluer than Lyman-alpha to 0 and for redder than Lyman-alpha to 1.

.. code:: python

          w_Lya = 1215.68
          w_IGM_rest_Arr = np.linspace( w_Lya-20.0 , w_Lya+20.0 , 1000 )
          T_IGM_Arr = np.ones( len( w_IGM_rest_Arr ) )

          T_IGM_Arr[ w_IGM_rest_Arr < w_Lya ] = 0

Now let's generate the observed Lyman-alpha line profile:

.. code:: python

          w_IGM_Arr , f_IGM_Arr , s_IGM_Arr , info = Lya.Generate_a_real_line( z_t , V_t, log_N_t, t_t, F_t, log_EW_t, W_t , PNR_t, FWHM_t , PIX_t , LyaRT_Grid, Geometry ,  T_IGM_Arr=T_IGM_Arr , w_IGM_Arr=w_IGM_rest_Arr , RETURN_ALL=True )


`w_IGM_Arr` is a numpy array that contains the wavelength where the line profile is evaluated. Meanwhile, `f_IGM_Arr` is the actual line profile. `s_IGM_Arr` is the uncertainty of the flux density. `info` is a python dictinary that contains a lot of information about how the line was computed, like the ideal line profile, the true IGM escape fraction, etc. 

We can obtain the intrinsic line profile with ideal conditions as...

.. code:: python

          w_INT_Arr = info[ 'w_obs' ] # wavelength array of the intrinsic line
          f_INT_Arr = info[ 'Intrinsic' ] # flux array of the intrinsic line

The true IGM escape fraction is...

.. code:: python

          print( info['f_IGM_4.0'] )
          0.8827655503368276


Now that we have our mock line profile, we can fit it. In this example we are going to use `MODE='IGM-z'`. There are three possible modes: `MODE='IGM+z'` , `MODE='IGM-z'` and `MODE='NoIGM'` . Each of these `MODE` use a differente machine learning model with a different training set. `MODE='IGM+z'` is trained so that the IGM transmission curves in the training set match the real IGM evolution with redshift. `MODE='IGM-z'` uses an IGM that is constant with redshift, and therefore it is more unbiased to redshift dependence than `MODE='IGM+z'`. Note that `MODE='IGM+z'` should be baised towards reallity. Then, `MODE='NoIGM'` was trained wihtout the IGM absorption, only the ISM part.

.. code:: python

          N_ITER = 10000 # Number of times to pertube the line profile

          RESULTS = Lya.Fit_Observed_line_with_IGM( w_IGM_Arr , f_IGM_Arr , s_IGM_Arr , PIX_t , FWHM_t , MODE='IGM-z' , N_ITER=N_ITER )

The function `Fit_Observed_line_with_IGM` is used to fit 1 line and it loads the NN and PCA models every time that it is called. This is not a problem if only a handful of lines are fitted at the same time. However, if the user wants to fit many lin    es, it could be better to load the NN and PCA models outside the function and pass it as an agument. This is done as...

.. code:: python

          DIC_loaded_models , my_PCA_model = Lya.Pipieline_Zelda_2_Load_Models( 'IGM-z' )

          RESULTS = Lya.Fit_Observed_line_with_IGM( w_IGM_Arr , f_IGM_Arr , s_IGM_Arr , PIX_t , FWHM_t , MODE='IGM-z' , N_ITER=N_ITER , DIC_loaded_models=DIC_loaded_models , my_PCA_model=my_PCA_model )

`RESULTS` is a python dictionaty that stores all the information of the fit. The percentile 50 is stored as `x_Q50`, the percentile 16 as `x_Q16`, etc, where `x` is a fitted varible, like redshift, etc. Therefore, the fitted outflow values are

.. code:: python

          z_sol     = RESULTS[    'z_Q50' ] # redshift
          log_V_sol = RESULTS[ 'logV_Q50' ] # logarith of expansion velocity.
          log_N_sol = RESULTS[ 'logN_Q50' ] # logarith of neutral hydrogen column density.
          log_t_sol = RESULTS[ 'logt_Q50' ] # logarith of dust optical depth.
          log_E_sol = RESULTS[ 'logE_Q50' ] # logarith of intrinsic equivalent width.
          log_W_sol = RESULTS[ 'logW_Q50' ] # logarith of intrinsic width.
          f_ig1_sol = RESULTS[  'f1A_Q50' ] # IGM Lya escape fraction 1A arround Lya.
          f_ig2_sol = RESULTS[  'f2A_Q50' ] # IGM Lya escape fraction 2A arround Lya.
          f_ig4_sol = RESULTS[  'f4A_Q50' ] # IGM Lya escape fraction 4A arround Lya.

Then, the measured IGM Lya escape fraction 4 amstrongs arround Lya is

.. code:: python

          print( RESULTS['f4A_Q50'] , '+-' , RESULTS['f4A_Q84']-RESULTS['f4A_Q16'] )
          0.8047662675380707 +- [0.06671568]

We can compute the solution line profile as...

.. code:: python

          w_SOL_OBSERVED_Arr , f_SOL_OBSERVED_Arr , s_SOL_OBSERVED_Arr , sol_info = Lya.Generate_a_real_line( z_sol , 10**log_V_sol , log_N_sol, 10**log_t_sol, F_t, log_E_sol, 10**log_W_sol , 1000. , FWHM_t , PIX_t , LyaRT_Grid, Geometry , RETURN_AL    L=True )

And we can plot it to compare with the actual intrinsic line profile:

.. code:: python

          f_SOL_OBSERVED_Arr = f_SOL_OBSERVED_Arr * 1. / np.amax(f_SOL_OBSERVED_Arr) # rescaling to be comparable

          w_SOL_OBSERVED_pix_Arr  , f_SOL_OBSERVED_pix_Arr  = Lya.plot_a_rebinned_line( w_SOL_OBSERVED_Arr , f_SOL_OBSERVED_Arr , PIX_t )

          plt.plot( w_IGM_rest_Arr*(1+z_t) , T_IGM_Arr , label='IGM tranmission' )
          plt.plot( w_INT_Arr , f_INT_Arr , label='Intrinsic' )
          plt.plot( w_IGM_pix_Arr , f_IGM_pix_Arr , label='IGM attenuated' )
          plt.plot( w_SOL_OBSERVED_pix_Arr , f_SOL_OBSERVED_pix_Arr , label='Reconstruction' )
          plt.legend(loc=0)
          plt.xlabel('wavelength[A]' , size=15 )
          plt.ylabel('Flux density [a.u.]' , size=15 )
          plt.xlim( ( w_Lya - 5 ) * (1+z_t) , ( w_Lya + 5 ) * (1+z_t) )
          plt.show()


You should get something like:

![Example of a Lyman-alpha line profile reconstruction. The IGM transmission curve is shown in blue. The intrinsic line profile in shown in orange. The Observed line profile after the IGM attenuation is shown in green. The reconstructed line profile is shown in red.](docs/figs_and_codes/fig_tutorial_fit_IGM_2.png)

# Acknowledgements

We acknowledge contributions from Brigitta Sipocz, Syrtis Major, and Semyeong
Oh, and support from Kathryn Johnston during the genesis of this project.

# References

bibliography:
