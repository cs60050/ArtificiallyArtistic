import numpy as np
import scipy
from numpy import *
from PIL import Image
from scipy.misc import imread
from scipy.misc import imshow
from scipy.misc import toimage
from scipy import sparse 
def pca(X):
  # Principal Component Analysis
  # input: X, matrix with training data as flattened arrays in rows
  # return: projection matrix (with important dimensions first),
  # variance and mean

  #get dimensions
  num_data,dim = X.shape		

  #center data
  mean_X = X.mean(axis=0)
  for i in range(num_data):
      X[i] -= mean_X

  if dim>100:
      U,S,V = scipy.sparse.linalg.svds(X)
      '''
      M = dot(X,X.T) #covariance matrix
      e,EV = linalg.eigh(M) #eigenvalues and eigenvectors
      tmp = dot(X.T,EV).T #this is the compact trick
      V = tmp[::-1] #reverse since last eigenvectors are the ones we want
      S = sqrt(e)[::-1] #reverse since eigenvalues are in increasing order
      '''
  else:
      U,S,V = linalg.svd(X)
      V = V[:num_data] #only makes sense to return the first num_data

  return U,V,S,mean_X
#end of PCA

  
imgarr = np.zeros((15,256*256*3))
for i in range(1,16):
   imgarr[i-1] = imread("VanGogh/img"+str(i)+".jpg").flatten()

U,V,S,immean = pca(imgarr)

immean = immean.reshape(256,256,3)
mode = V[0].reshape(256,256,3)

#toimage(immean).show()
#toimage(mode).show()

A = U[:15]
b = dot(S, V)
#toimage(b.reshape(256,256,3)).show()
content = imread("Test/content.jpg")
toimage(content).show()
toimage(immean*content).show()


















