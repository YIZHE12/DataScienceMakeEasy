# Gradient Descent and regression models

1. The general equation of gradient descent is:

<img src = ../images/gd_eq.gif>

It is a function to update our hypothesis parameter in the cost function space:

<img src = ../images/gd_graph.png height = 200>


2. Gradient Descent For Linear Regression:

<img src = ../images/gd_linear_regression1.png height = 100>

<img src = ../images/gd_linear_regression2.png height = 200>

3. Multivariable linear regression:

This is a vectorization of our hypothesis function for one training example:

<img src = ../images/gd_linear_regression3.png height = 100>

Note that X0 = 1

Applying gradient descent, we will have:

<img src = ../images/gd_linear_regression4.png height = 600>

You must perform feature normalization or scaling before the linear regression with gradient descent

For different gradient descent algorithm:

http://ruder.io/optimizing-gradient-descent/


4. Features and Polynomial Regression

In order to bring non-linearity to linear regression, one can do feature engineering, such as sqrt(x1) or x1 * x2, x1^2 etc. However, one must remember to scale each engineered features.

