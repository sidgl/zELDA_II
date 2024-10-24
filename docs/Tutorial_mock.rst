Tutorial : Computing mock line profiles
========================================

In this tutorial you will, hopefully, learn how to compute mock line Lyman-alpha line profiles with `zELDA`. The lines computed in this tutorial suffer from the typical artifacts caused by the fact the instruments are not perfect.

Mocking Lyman-alpha line profiles
*********************************

Let's start by loading `zELDA` and setting the location of the LyaRT grids:

.. code:: python

          import Lya_zelda_II as Lya

          your_grids_location = '/This/Folder/Contains/The/Grids/'

          Lya.funcs.Data_location = your_grids_location

where `/This/Folder/Contains/The/Grids/` is the place where you store the LyaRT data grids, as shown in the :doc:`Installation <installation>` section.

Now, let's decide which outflow geometry we want to use. For this tutorial we will use the gas geometry known as Thin Shell in which the intrinsic continuum is a gaussian and a continuum with a give equivalent width.

.. code:: python

          Geometry = 'Thin_Shell_Cont'

Let's load the data containing the grid:

.. code:: python

          LyaRT_Grid = Lya.load_Grid_Line( Geometry )

This contains all the necessary information to compute the line profiles. To learn more about the grids of line profiles go to :doc:`About the LyaRT data grids <About_the_data_grids>` . Remeber that if you want to use the line profile grid with lower RAM memory occupation you must pass `MODE='LIGHT'` to `Lya.load_Grid_Line`.

Now let's define the parameters of the shell model that we want. these are five:

.. code:: python

          z_t      = 0.5   # redshift of the source
          V_t      = 50.0  # Outfloe expansion velocity [km/s]
          log_N_t  = 20.   # Logarithmic of the neutral hydrogen column density [cm**-2]
          t_t      = 0.01  # Dust optical depth
          log_EW_t = 1.5   # Logarithmic the intrinsic equivalent width [A]
          W_t      = 0.5   # Intrinsic width of the line [A]
          F_t      = 1.    # Total flux of the line

Now let's set the quality of the line profile:

.. code:: python

          PNR_t  = 20.0 # Signal to noise ratio of the maximum of the line.
          FWHM_t = 0.2  # Full width half maximum diluting the line. Mimics finite resolution. [A]
          PIX_t  = 0.1  # Wavelength binning of the line. [A]

Now he have everything, let's compute the line simply by doing:

.. code:: python

          w_Arr , f_Arr , _ = Lya.Generate_a_real_line( z_t , V_t, log_N_t, t_t, F_t, log_EW_t, W_t , PNR_t, FWHM_t, PIX_t, LyaRT_Grid, Geometry )

And... It's done! `w_Arr` is a numpy array that contains the wavelength where the line profile is evaluated. Meanwhile, `f_Arr` is the actual line profile. 

Let's plot the line by doing

.. code:: python

          import pylab as plt
          plt.plot( w_Arr , f_Arr )
          plt.xlabel('wavelength[A]' , size=15 )
          plt.ylabel('Flux density [a.u.]' , size=15 )
          plt.xlim(1815,1835)
          plt.show()

This should show something like this

.. image:: figs_and_codes/fig_Tutorial_2_1.png
   :width: 600

Now let's create an IGM transmission curve. This is a simple toy model. For this example we are going to set the IGM transmission bluer than Lyman-alpha to 0.3 and for redder than Lyman-alpha to 1.

.. code:: python

          import numpy as np
          w_Lya = 1215.68
          w_IGM_rest_Arr = np.linspace( w_Lya-20.0 , w_Lya+20.0 , 1000 )
          T_IGM_Arr = np.ones( len( w_IGM_rest_Arr ) )

          T_IGM_Arr[ w_IGM_rest_Arr < w_Lya ] = 0.3

Now let's generate the IGM attenuated line

.. code:: python

    w_IGM_Arr , f_IGM_Arr , _ = Lya.Generate_a_real_line( z_t , V_t, log_N_t, t_t, F_t, log_EW_t, W_t , PNR_t, FWHM_t, PIX_t, LyaRT_Grid, Geometry , T_IGM_Arr=T_IGM_Arr , w_IGM_Arr=w_IGM_rest_Arr )

and this is how they look

.. code:: python

    f_Arr     = f_Arr     *1. / np.amax( f_Arr     )
    f_IGM_Arr = f_IGM_Arr *1. / np.amax( f_IGM_Arr )

    plt.plot( w_Arr     , f_Arr     , label='No IGM' )
    plt.plot( w_IGM_Arr , f_IGM_Arr , label='IGM' )
    plt.plot( w_IGM_rest_Arr * (1+z_t) , T_IGM_Arr , label='IGM transmission' )
    plt.legend( loc=0 )
    plt.xlabel('wavelength[A]' , size=15 )
    plt.ylabel('Flux density [a.u.]' , size=15 )
    plt.xlim(1815,1835)
    plt.show()

.. image:: figs_and_codes/fig_Tutorial_2_2.png
   :width: 600

Plotting cooler line profiles
*****************************

If you want a cooler and more 'accurate' plot of the line profile you can use:

.. code:: python

          w_INT_pix_Arr , f_INT_pix_Arr = Lya.plot_a_rebinned_line( w_Arr , f_Arr , PIX_t )
          w_IGM_pix_Arr , f_IGM_pix_Arr = Lya.plot_a_rebinned_line( w_IGM_Arr , f_IGM_Arr , PIX_t )

          plt.plot( w_INT_pix_Arr , f_INT_pix_Arr , label='Intrinsic' )
          plt.plot( w_IGM_pix_Arr , f_IGM_pix_Arr , label='IGM attenuated' )
          plt.xlabel('wavelength[A]' , size=15 )
          plt.ylabel('Flux density [a.u.]' , size=15 )
          plt.xlim(1815,1835)
          plt.show()

.. image:: figs_and_codes/fig_Tutorial_2_3.png
   :width: 600

`Lya.plot_a_rebinned_line` is just a function that returns the line profile and wavelength array in a cool way to plot them. You probably shouldn't use for science the output of `Lya.plot_a_rebinned_line`, just for plotting. 








