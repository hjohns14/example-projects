import pandas as pd
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

df = pd.read_excel('data/z_Masterfile.xlsx').dropna()
features_considered = ["WTI_price"]
features = df[features_considered]
features.index = df["Date"]

X = features.values

size = int(len(X) * 0.66)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()
order = (5, 1, 0)
for t in range(len(test)):
    model = ARIMA(history, order=order)
    model_fit = model.fit(disp=0)
    output = model_fit.forecast()
    yhat = output[0]
    predictions.append(yhat)
    obs = test[t]
    history.append(obs)
    print('predicted=%f, expected=%f' % (yhat, obs))
# plot
error = mean_squared_error(test, predictions)
pyplot.plot(test)
pyplot.plot(predictions, color='red')
pyplot.ylabel("US Dollars")
pyplot.xlabel("Months")
name = str(order)
pyplot.suptitle('Test MSE: %.3f' % error + '   (p, d, q) = ' + name)
pyplot.savefig("graphs/ARIMA/" + name)
print('Test MSE: %.3f' % error)
pyplot.show()
