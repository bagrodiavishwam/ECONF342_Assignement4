import pandas as pd
from statsmodels.formula.api import ols
from scipy.stats import jarque_bera

data = pd.read_excel("nyse.xls")
data

print("Quadratic Model Summary:")
model = ols("Return ~ Return_1 + Return_12", data=data).fit()
model.summary()

print("Two-Lagged Model Summary:")
two_lagged=data['Return_1'].shift(1)*data['Return_1']
model = ols("Return ~ Return_1 + two_lagged", data=data).fit()
model.summary()

model = ols("Return ~ Return_1 + Return_12", data=data).fit()
residuals = (model.resid)**2
df2=pd.read_excel("nyse.xls", usecols='C,D,J')
data1=pd.concat([residuals,df2])
model_2=ols(residuals,df2).fit()
model_2.summary()
