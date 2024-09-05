import setuptools

#from setuptools.command.develop import develop
#from setuptools.command.install import install

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Lya_zelda_II",
    version="0.0.01",
    author="Siddhartha Gurung Lopez",
    author_email="gurung.lopez@gmail.com",
    description="Fast Lyman alpha Radiative Transfer for everyone!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sidgl/zELDA_II",
    download_url = 'https://github.com/sidgl/zELDA_II',
    packages=setuptools.find_packages(),
    #install_requires=[ 'sklearn>=20.0' ],
    #scikit-learn==0.22.1
    install_requires=[ 'setuptools>66' , 'scikit-learn==1.5', 'pyswarms==1.3.0'  , 'emcee==3.1.2' , 'numpy<2.0'],
    include_package_data = True,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    #cmdclass={ 'develop': PostDevelopCommand,
    #           'install': PostInstallCommand, },
)

