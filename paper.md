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


# Citations

Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

If you want to cite a software repository URL (e.g. something on GitHub without a preferred
citation) then you can do it with the example BibTeX entry below for @fidgit.

For a quick reference, the following citation commands can be used:
- `@author:2001`  ->  "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"

# Figures

Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Figure sizes can be customized by adding an optional second parameter:
![Caption for example figure.](figure.png){ width=20% }

# Acknowledgements

We acknowledge contributions from Brigitta Sipocz, Syrtis Major, and Semyeong
Oh, and support from Kathryn Johnston during the genesis of this project.

# References
