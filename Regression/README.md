# Regression Notebooks

## Posts on Regression Analysis
- [Simple Regression in Python with scikit-learn](https://www.wintellect.com/creating-a-simple-linear-regression-machine-learning-model-with-scikit-learn/)
- [Creating a Machine Learning Web API with Flask](https://www.wintellect.com/creating-machine-learning-web-api-flask/)

Special thanks to [Super DataScience](https://www.superdatascience.com/) for offering their data and @Wintellect for sharing its code

## Reproducing this notebooks

We are showing how to create a prediction service from a notebook in a reproducible manner.

The only prerequesite is to have [Docker](http://www.docker.com) installed

Step:

* Start notebook service to work interactively with data: clean, analize, model and evaluate
    
        docker run -it --rm -p 8888:8888 -v $PWD/:/home/jovyan/work -e NB_UID=`id -u` --net=host jupyter/scipy-notebook

* Build and persist model and dependencies scripted

        docker build -f Dockerfile.notebook -t slr-model .
        docker run -it --rm -v $PWD/data:/home/jovyan/data -v $PWD/model:/home/jovyan/model -e NB_UID=`id -u` slr-model

* Build and start prediction service

        docker build -f Dockerfile.api -t slr-api .
        docker run -p 5000 --net=host slr-api

* Test prediction service using notebook

        docker build -f Dockerfile.test -t slr-test .
        docker run -it --rm -v $PWD/test:/home/jovyan/test -e NB_UID=`id -u` --net=host slr-test

These docker images are available in https://hub.docker.com/r/gmiretti/
