import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np

def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).
    Args:
        x: a list with length N, representing the x-coords of N sample points
        y: a list with length N, representing the y-coords of N sample points
        degs: a list of degrees of the fitting polynomial
    Returns:
        a list of numpy arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    # TODO
    models=[]

    for d in degs:
       mod=np.polyfit(x,y,d)
       models.append(mod) 
    return models

