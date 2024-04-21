import pandas as pd
import statsmodels.api as sm

# Read the data from the file
data = pd.read_excel("fish.xls")  # Replace "your_file.csv" with the actual file path

# Perform the regression
X = data[['mon', 'tues', 'wed', 'thurs','t']]
X = sm.add_constant(X)  # Add a constant term
y = data['lavgprc']
model = sm.OLS(y, X).fit()

# Print the results
print(model.summary())

# Perform the regression 2
X = data[['mon', 'tues', 'wed', 'thurs','wave2','wave3','t']]
X = sm.add_constant(X)  # Add a constant term
y = data['lavgprc']
model = sm.OLS(y, X).fit()

# Print the results
print(model.summary())

residuals=model.resid
model_AR=sm.OLS(y,residuals).fit()
print(model_AR.summary())

residuals=model.resid
y=residuals.dropna()
print(y)
residuals_1=residuals.shift(1)
x=sm.add_constant(residuals_1)
x.dropna()
model_AR=sm.OLS(y,x).fit()
print(model_AR.summary())
