---
title: 'zELDA : A python package for modeling and fitting Lyman-alpha line profiles.'
tags:
  - Python
  - astronomy
  - radiative transfer
  - galaxies
authors:
  - name: Siddhartha Gurung-Lopez    
    orcid: 0000-0001-9333-8470
    affiliation: "1, 2" # (Multiple affiliations must be quoted)
    corresponding: true # (This is how to denote the corresponding author)
  - name: Chris Byrohl
    affiliation: "3" # (Multiple affiliations must be quoted)
  - name: Max Gronke
    affiliation: "4"
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
Regarding the unobscured Lyα line profiles, `zELDA` includes an MCMC algorithm powered by the python package `EMCEE` [@Foreman-Mackey]
and two artificial neural network models trained in mock spectrum. 
Regarding the IGM attenuated Lyα line profiles, `zELDA` includes four artificial neural network models trained with the `zELDA` 'shell-model' grid and the IGM transmission curves from the TNG100 simulation [@Byrohl2019; @Byrohl2020] .

Tutorials on installation and usage can be found at https://zelda-ii.readthedocs.io/index.html. 

# Statement of need

`zELDA` is an open source Python package to model and fit Lyα line profiles. 
On one hand, the  Lyα modeling through the 'shell-model' enables users to populate galaxy simulations with realistic  Lyα line profiles. 
On the other hand, the fitting procedures provide a robust measurement of the shape of the line. 
Moreover, `zELDA` is able to disentangle between the intergalactic and interestelar medium contribution to the  Lyα line profile. 
One of the advantages of `zELDA` is that it can be used seamlessly in different observational configurations, allowing a direct comparison between different surveys and projects. 

`zELDA` is developed to have a user-friendly interface so that it can be used by researchers and students in astronomy courses. 
`zELDA` has been used already in a number of scientific publications [@gurunglopez2022; @Guaita2022] , mainly to fit observational observations. 
`zELDA` will allow researchers to extract the maximum information from their observed Lyα line profiles. 
Moreover, disentangeling the IGM from the ISM contribution will be key in future surveys to understand the Lyα selection function.

# Installation

`zELDA`, installation is divided in two blocks. First you will need to install the python package.The pyhton package includes all the machine learning models need for fitting and modelling the Lyman-alpha line profiles. In order to install `zELDA`, it can be downloaded from GitHub (`https://github.com/sidgl/zELDA_II/`) or installed using PyPI:

```
    $ python3 -m pip install Lya_zelda_II
```

Once the python pakage is installed, it is necessary to download the grid of Lyman-alpha shell spectrum. The grids are stored in https://zenodo.org/records/4733518. 

![Estructure of functionalities of `zELDA`](docs/figs_and_codes/estructura.png)

# Features and functionalities

The features and functionalities of `zELDA` displayed in Fig.1. Basically `zELDA` has two main goals. First, modelling the Lyman-alpha emission and second, fitting observations of Lyman-alpha emitters. 

## Modelling Lyman-alpha

The modelling of the Lyman-alpha line is made through lineal interpolation in grids of spectrum computed through the Monte Carlo radiative transfer code `LyaRT` [@orsi12]. 

- **Interestellar medium escape fraction** : `zELDA` provides the ISM escape fraction for three outflow geometries. These are a biconical wind, a spherical wind and a thin shell model. These models are presented in [@GurungLopez2019b].  

- **Ideal Lyman-alpha line profiles** : `zELDA` provides the spectrum emerging from the three outflow geometries explained above. Aditionally, for the thin shell model, ideal spectrum is also provided for different intrinsic spectrum, as shown in [@gurunglopez2022]. An example of an ideal line profile is swhon in Fig.2. in orange. 

- **Mock Lyman-alpha line profiles** : `zELDA` provides realistic Lyman-alpha line profiles mimicking the aspects of observations. In particular, the ideal Lyman-alpha line profiles are downgrading by lower their resolution, adding pixelitation and noise,  as shown in [@gurunglopez2022]. The green line in Fig.2. shows the mock line profile of the ideal line profile (orange) after being convolved with an arbitrary intergalactic medium  tranmission curve (blue).

## Fitting observed Lyman-alpha line profiles

The fitting of observed Lyman-alpha line profiles is perform in two different flavors. 

- **Lyman-alpha line profileis wihtout IGM attenuation** : In @gurunglopez2022 we presented two methodologies for fitting Lyman-alpha line profiles clean from the IGM. `zELDA` includes an MCMC pipeline based in the python package `EMCEE` [@Foreman-Mackey] that minimizes the $\xi^2$. The sencond methodology relies in deep learning models powered by scikit-learn [@scikit-learn]. These models were trained using mock Lyman-alpha line profiles produced by `zELDA`. 

- **Lyman-alpha line profileis attenuated by the IGM** : The Lyman-alhpa line profile reconstruction is perform trhough in deep learning models powered by scikit-learn [@scikit-learn]. These models were trained using mock Lyman-alpha line profiles produced by `zELDA` convolved with the IGM tranmission curved from the TNG100 simulation [@Byrohl2019; @Byrohl2020]. The Lyman-alpha line profile reconstruction also provides the IGM escape fraction. An example of reconstruction is shown in red in Fig.2, using as input the mock line profile (green). The reconstructed line profile matches well the true line profile (orange).

![Example of a Lyman-alpha line profile reconstruction. The IGM transmission curve is shown in blue. The intrinsic line profile in shown in orange. The Observed line profile after the IGM attenuation is shown in green. The reconstructed line profile is shown in red.](docs/figs_and_codes/fig_tutorial_fit_IGM_2.png)

# Acknowledgements

We acknowledge contributions from Brigitta Sipocz, Syrtis Major, and Semyeong
Oh, and support from Kathryn Johnston during the genesis of this project.

# References

bibliography:
