# polynomial Linear Recursive in scikit-learn

# Import packages and classes
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Provide data
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([15, 11, 2, 8, 25, 32])

# Transform input data
transformer = PolynomialFeatures(degree=2, include_bias=False)
transformer.fit(x)
x_ = transformer.transform(x)
x_ = PolynomialFeatures(degree=2, include_bias=False).fit_transform(x)

print('x:', x_)

# Create a model and fit it
model = LinearRegression()
model.fit(x_, y)
model = LinearRegression().fit(x_, y)

# Get Results
r_sq = model.score(x_, y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
x_ = PolynomialFeatures(degree=2, include_bias=True).fit_transform(x)
print(x_)

model = LinearRegression(fit_intercept=False).fit(x_, y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)


# Predict response
y_pred = model.predict(x_)
print('predicted response:', y_pred, sep='\n')
y_pred = model.intercept_ + model.coef_ * x_
print('predicted response:', y_pred, sep='\n')
