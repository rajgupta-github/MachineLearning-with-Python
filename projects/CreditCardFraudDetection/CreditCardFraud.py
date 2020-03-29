import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,auc,roc_auc_score, classification_report
from sklearn.metrics import recall_score, precision_score, accuracy_score, f1_score

cc = pd.read_csv("https://raw.githubusercontent.com/insaid2018/Term-2/master/Data/credit_fraud.csv")
print(cc.head())

print(len(cc[cc['Class']==1]))

print(cc.Class.value_counts())

sns.countplot(x="Class",data=cc)

print(cc.columns)

print(cc.shape)

print(cc.describe())

print(cc.info())

print(cc.isnull().sum().any())