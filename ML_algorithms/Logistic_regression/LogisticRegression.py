
# Logistic Regression - One vs All Method
# Author - Mahendra Kumar

# file_name : train.py

# libraries required
import numpy as np
import csv
import pandas as pd


def import_train_data(path_trainX, path_trainY):
    X = np.genfromtxt(path_trainX,skip_header=1,delimiter=',')
    Y = np.genfromtxt(path_trainY,delimiter=',')
    return X,Y


def sigmoid(Z):
    return 1/(1+ np.exp(-Z))


def compute_cost(X, Y, W, b):
    prediction = sigmoid(np.matmul(X,W) + b).reshape(-1)
    log_y = np.log(prediction).reshape(len(prediction),1)
    log_one_minus_y = np.log(1-prediction).reshape(len(prediction),1)
    cost = -( np.matmul(Y.T,log_y) + np.matmul(1-Y.T,log_one_minus_y) ) / X.shape[0]
    return cost[0]; 


def compute_gradient_of_cost_function(X, Y, W, b):
    prediction = sigmoid(np.matmul(X,W) + b).reshape(-1)
    diff =  (prediction - Y).T
    diff = diff.reshape(diff.shape[0],1).T
    db = np.sum(diff)/X.shape[0]  
    dw = np.dot(diff,X)/X.shape[0];
    return dw.T,db


def predict_labels(X, W, b):
    prediction = sigmoid(np.matmul(X,W)+b)
    prediction = np.array([1  if x>=0.5 else 0 for x in prediction])
    return prediction


def optimize_weights_using_gradient_descent(X, Y, W,b, num_iterations, learning_rate):
    for _ in range(1,num_iterations+1):
        dW,db = compute_gradient_of_cost_function(X,Y,W,b)
        b = b - (learning_rate*db);
        W = W - (learning_rate*dW);
    return W,b



def check_weighted_f1_score(pred_Y, actual_Y):
    from sklearn.metrics import f1_score
    weighted_f1_score = f1_score(actual_Y, pred_Y, average = 'weighted')
    print("Weighted F1 score", weighted_f1_score)
    return weighted_f1_score





train_X_path = ""  # add path to train_X
train_Y_path = "" # add path to train_Y/labels
X,Y = import_train_data(train_X_path,train_Y_path)
n_classes = len(set(Y))

num_iterations=1000000
learning_rate = 0.001
predictions =[]

with open('WEIGHTS_FILE.csv','w') as f :     
    
    wr = csv.writer(f)   
    
    for i in range(n_classes):
      y = np.array([ 1 if x == True else 0 for x in (Y==i)])
      W = 2*np.random.rand(X.shape[1],1)-1
      b = 2*np.random.rand() - 1
      W,b = optimize_weights_using_gradient_descent(X,y,W,b,num_iterations,learning_rate)
      W = W.reshape(-1)
      wr.writerow(np.insert(W,0,b))

    f.close()
        





# Label Prediction and F-Score Calculation

# --- Uncomment to add test_X , test_Y file paths

# test_X  = np.genfromtxt(test_X_path,delimiter=',',skip_header=1)
# test_Y = np.genfromtxt(test_Y_path,delimiter=',')
# weights = np.genfromtxt('WEIGHTS_FILE.csv',delimiter=',')  # b corresponding to each hypothesis function h_i{theta} is at 0th index

# predictions=[]
# prediction = sigmoid(np.matmul(X,weights.T)
# predictions.append(prediction)
# predictions = np.array(predictions).T
# labels = []
# for pred in predictions : 
#   labels.append(np.where(pred==max(pred)))
# labels =  np.array(labels).reshape(-1)

# print("weighted F Score : ",check_weighted_f1_score(labels,Y_test))

