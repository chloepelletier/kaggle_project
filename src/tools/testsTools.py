from sklearn.metrics import mean_squared_error

def getRMSE(a, b):
    np.sqrt(mean_squared_error(a.values.astype(int), b))
