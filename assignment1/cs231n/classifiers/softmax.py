import numpy as np
from random import shuffle
from past.builtins import xrange


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
    num_train = X.shape[0]
    num_classes = W.shape[1]
    for i in xrange(num_train):
        scores = X[i].dot(W)
        scores = scores-np.max(scores)
        scores = np.exp(scores)
        scores /= np.sum(scores)
        loss -= np.log(scores[y[i]])
        for j in xrange(num_classes):
            constant = scores[j]
            if j == y[i]:
                dW[:, j] += (constant-1) * X[i]
            else:
                dW[:, j] += constant * X[i]

    pass
    #############################################################################
    #                          END OF YOUR CODE                                 #
    #############################################################################
    loss /= num_train
    dW /= num_train
    loss += reg * np.sum(W * W)
    dW += 2*reg*W
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
    num_train = X.shape[0]
    scores = np.dot(X, W)
    scores -= np.reshape(np.max(scores, axis=1), (-1, 1))
    scores = np.exp(scores)
    scores /= np.sum(scores, axis=1).reshape(-1,1)
    real_classes_scores = scores[np.arange(num_train), y]
    loss -= np.sum(np.log(real_classes_scores))
    loss /= num_train
    loss += reg * np.sum(W * W)
    scores[np.arange(num_train),y]-=1
    dW+=np.dot(X.T,scores)/num_train+2*reg*W
    pass
    #############################################################################
    #                          END OF YOUR CODE                                 #
    #############################################################################
    
    return loss, dW
