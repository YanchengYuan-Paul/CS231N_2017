import numpy as np
from random import shuffle
#from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  for i in range(X.shape[0]):
    scores = X[i].dot(W)
    sum_exp_scores = np.sum(np.exp(scores))
    loss += (-scores[y[i]] + np.log(sum_exp_scores))
    for j in range(W.shape[1]):
        if j == y[i]:
            dW[:, j] -= X[i]
            
        dW[:, j] += (np.exp(scores[j])/sum_exp_scores)*X[i]
        
  dW /= float(X.shape[0])
  dW += 2*reg*W
  loss /= float(X.shape[0])
  loss += reg*np.sum(W*W)
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  scores = X.dot(W)
  loss -= np.sum(scores[range(X.shape[0]), y])
  exp_scores = np.exp(scores)
  sum_exp_scores = np.sum(exp_scores, axis = 1)
  weight_exp_scores = exp_scores/np.reshape(sum_exp_scores, (len(sum_exp_scores),1))
  weight_exp_scores[range(X.shape[0]),y] -= 1
  dW += (X.T).dot(weight_exp_scores)
  loss += np.sum(np.log(sum_exp_scores))
  loss /= float(X.shape[0])
  dW /= float(X.shape[0])
  loss += reg*np.sum(W*W)
  dW += 2*reg*W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

