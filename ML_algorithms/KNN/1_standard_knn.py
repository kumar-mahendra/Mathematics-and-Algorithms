# file name : knn.py

# Author : Mahendra Kumar

import numpy as np

def import_train_data(train_X_path,train_Y_path):
    X = np.genfromtxt(train_X_path,delimiter=',', skip_header=1)
    Y = np.genfromtxt(train_Y_path, delimiter=',').reshape(len(X),1)
    return X,Y


def Ln_norm(vector1, vector2, n):
    vector1 = np.array(vector1)
    vector2 = np.array(vector2)
    Norm = np.sum((abs(vector1 - vector2))**n,axis=1)**(1/n)
    return Norm


def find_k_nearest_neighbors(train_X,test_example,k,n):
    ln_norms = Ln_norm(train_X,test_example,n)
    # print(len(ln_norms),ln_norms)
    indices_inc_orderOfnorms = sorted([ [ln_norms[index],index] for index in range(len(ln_norms)) ], key = lambda x : x[0])
    first_k_indices = [ x[1] for x in indices_inc_orderOfnorms][:k]
    return first_k_indices


def classify_points_using_knn(train_X,train_Y,test_X,k,n):
    train_X,train_Y,test_X = np.array(train_X),np.array(train_Y),np.array(test_X)
    predictions = []
    for test_ex in test_X : 
        knns_idx = find_k_nearest_neighbors(train_X,test_ex,k,n)
        labels = list(np.array(train_Y[knns_idx]).reshape(-1))
        pred_label_of_test_ex = max([[x,labels.count(x)] for x in set(labels)],key= lambda y : y[1])[0]   # label of maximum occurring neighborhood
        predictions.append(pred_label_of_test_ex)
    return predictions 

def check_weighted_f1_score(pred_Y, actual_Y):
    from sklearn.metrics import f1_score
    weighted_f1_score = f1_score(actual_Y, pred_Y, average = 'weighted')
    
    print("Weighted F1 score", weighted_f1_score)
    return weighted_f1_score  

def write_to_csv_file(pred_Y, predicted_Y_file_name):
    pred_Y = pred_Y.reshape(len(pred_Y), 1)
    with open(predicted_Y_file_name, 'w', newline='') as csv_file:
        wr = csv.writer(csv_file)
        wr.writerows(pred_Y)
        csv_file.close()

train_X_path = ""  # add path to train_X
train_Y_path = "" # add path to train_Y/labels
train_X,train_Y = import_train_data(train_X_path,train_Y_path)

# Hyperparameters 
k = 4 
n = 3 

test_X_path = ""  # add path to validation dataset  Or make do train-test split on train_X
test_Y_path = ""
test_X = np.genfromtxt(test_X_path,delimiter=",",skip_header=1) 

pred_Y = classify_points_using_knn(train_X,train_Y,test_X,k,n)
write_to_csv_file(pred_Y,'predicted_test_Y_knn.csv')
weighted_f1_score = check_weighted_f1_score(test_Y_path,'predicted_test_Y_knn.csv')                                             
