# Linear Regression in Python 
# Author - Mahendra Kumar

#-------------------------------------------------------
# Arguments:
# X - Observations in training data.
# - A 2D numpy array of shape (num of observations, num of features)
# Y - True values corresponding to each observation.
# - A 2D numpy array of shape (num of observations, 1)
# W - Weights of features.
# - A 2D numpy array of shape (num of features + 1, 1)
# num_iterations - Number of iterations in gradient descent
# - int
# learning_rate - Learning rate in gradient descent
# - float
# ------------------------------------------------------

global n_inputs, n_features;

# Import Libraries required 
import numpy as np 
# from scan_utils import scan_X, scan_Y, scan_W

# To Calculate Hypothesis Function Value (i.e. predicted value)  in linear Regression
def compute_hypothesis(X,W):
    return  np.matmul(X,W)
    
    
# To Calculate Cost Function in linear Regression 
def compute_cost(X, Y, W):
    hypothesis_value = compute_hypothesis(X,W)
    error = (hypothesis_value - Y)
    return np.matmul(error.T,error)/(2*X.shape[0])     # Formula of Cost
   
    
# To Calculate Gradient of Cost Function in linear Regression
def compute_gradient_of_cost_function(X, Y, W):
    predicted_Y = compute_hypothesis(X,W);
    grad_W = np.matmul(X.T, predicted_Y-Y)/n_inputs;
    grad_W = grad_W.reshape(1,grad_W.shape[0])[0]
    return grad_W


# Perform Gradient Descent in Linear Regression and return Optimized Weights 
def optimize_weights_using_gradient_descent(X, Y, W, num_iterations, learning_rate):
    for _ in range(num_iterations):
        grad_J = compute_gradient_of_cost_function(X,Y,W)
        W = W - (learning_rate*grad_J);
    return W


if __name__ == "__main__" :
    
    
    X = np.array([])
    W = np.array([])
    global n_inputs,n_features;
    n_inputs = int(input())
    
    for i in range(1,n_inputs+1):
        tmp = np.array(input().split(),dtype='float') ; 
        tmp = tmp.reshape(1,tmp.shape[0])
        if i==1 : 
            X = tmp;
        else : 
            X = np.vstack([X,tmp])
    
    X = np.insert(X,0,1,axis=1)  # Add Column of 1s to X
    
    # Weights Inputs
    W = np.array(input().split(),dtype='float')
    W.reshape(W.shape[0],1)
    
    n_features = W.shape[0];
    
    # Actual Y   
    Y = np.array(input().split(),dtype='float')
    Y.reshape(Y.shape[0],1)
    
    # 1 - Hypothesis Function : 
    hypothesis_value = compute_hypothesis(X,W);
    hypothesis_value = np.round(hypothesis_value, 2)
    print("Initial Predicted Y : " ,*hypothesis_value,sep=' ')
    
    # 2 - Cost Function 
    cost = compute_cost(X,Y,W);
    cost = np.round(cost, 2)
    print("Initial Cost : " , cost)
    
    # Gradient of cost Function 
    gradients = compute_gradient_of_cost_function(X,Y,W)
    gradients = np.round(gradients, 3)
    print("Initial Gradients : ", *gradients,sep=" ")
    
    # Optimized Weights 
    num_iterations = 10 
    learning_rate = 0.01
    optimized_weights = optimize_weights_using_gradient_descent(X, Y, W, num_iterations, learning_rate)
    optimized_weights = np.round(optimized_weights, 3)
    print("\n optimized_weights : ", *optimized_weights,sep=" ")