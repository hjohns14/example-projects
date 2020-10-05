import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


''' This program downloads a dataset of google's stock prices from quandl using an API call
    and uses linear regression and a Support Vector Machine to predict the future stock price (10 days).
    The confidence is printed for each mehtod. '''

quandl.ApiConfig.api_key = 'xghgkDWWtaWv3cMiAd_4'
df = quandl.get('WIKI/GOOGL')

df = df[["Adj. Open", "Adj. High", "Adj. Low", "Adj. Close" , "Adj. Volume"]]
df['HL_PCT'] = (df["Adj. High"] - df["Adj. Low"])/ df["Adj. Close"] * 100
df["PCT_change"] = (df["Adj. Close"] - df["Adj. Open"])/ df["Adj. Open"] * 100

#Features - what may cause the adj close price to change in 10 days
df = df[['Adj. Close', "HL_PCT", "PCT_change", "Adj. Volume"]]

forcast_col = "Adj. Close"
df.fillna(value=-99999, inplace=True)

#Rounds up to the nearest whole// 10% length of df
forecast_out = int(math.ceil(0.01*len(df)))



#labels
df["label"] = df[forcast_col].shift(-forecast_out)
df.dropna(inplace=True)
X = np.array(df.drop(["label"],1),)
y = np.array(df["label"])
X = preprocessing.scale(X)
y = np.array(df['label'])


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print(len(X), len(y))


clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
clf2 = svm.SVR()
clf2.fit(X_train, y_train)

svr_conf = clf2.score(X_test, y_test)
confidence  = clf.score(X_test, y_test)
print("Confidence -  Linear Regression: ", confidence)
print("Confidence - SVM: ", svr_conf)
