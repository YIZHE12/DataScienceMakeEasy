Machine learning

# Part 1: What is Machine Learning?

Arthur Samuel: "the field of study that gives computers the ability to learn without being explicitly programmed." What set aside machine learning from other computer sience method is the ability to adapt. 

Tom Mitchell: "A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E."

### Supervised and unsupervised learning

The major difference between supervised and unsupervised learning is if there is a target variable. Two common tasks in unsupervised learning: clustering and association. 

### Unsupervised learning:
Clustering: given a data set, one can cluster the samples into groups, based on the similarities among the samples within the data set. 

Association:  given a data set, the association task is to uncover the hidden association patterns among the attributes of a sample.

### Supervised learning:
If the output of a machine learning model is discrete values, e.g. a boolean value, we then call it a classification model. While we call the model that outputs continuous values as regression model.

### Semi-supervised learning
In a scenario where the data set is massive but the labeled sample are few, one might find the application of both supervised and unsupervised learning. We can call this task as semi-supervised learning. 

For example, one would like to predict the label of images, but only 10% of the images are labeled. By applying supervised learning, we train a model with the labeled data, then we apply the model to predict the unlabeled data. It would be hard to convince ourselves that the model would be general enough, after all we learnt from only the minority of data set. A better strategy could be to first cluster the images into groups (unsupervised learning), and then apply the supervised learning algorithm on each of the groups individually. The unsupervised learning in the first stage could help us to narrow down the scope of learning so that the supervised learning in the second stage could obtain better accuracy.

## Bias and variance
Bias is a learner’s tendency to consistently learn the same wrong thing. Variance is the tendency to learn random things unrelated to the real signal

<img src = images/bias.png>

<img src = images/variance.png>

# Part 2: Gradient Descent and regression models

1. The general equation of gradient descent is:

<img src = images/gd_eq.gif>

It is a function to update our hypothesis parameter in the cost function space:

<img src = images/gd_graph.png height = 200>


2. Gradient Descent For Linear Regression:

<img src = images/gd_linear_regression1.png height = 100>

<img src = images/gd_linear_regression2.png height = 200>

3. Multivariable linear regression:

This is a vectorization of our hypothesis function for one training example:

<img src = images/gd_linear_regression3.png height = 100>

Note that X0 = 1

Applying gradient descent, we will have:

<img src = images/gd_linear_regression4.png height = 600>

You must perform feature normalization or scaling before the linear regression with gradient descent

For different gradient descent algorithm:

http://ruder.io/optimizing-gradient-descent/


4. Features and Polynomial Regression

In order to bring non-linearity to linear regression, one can do feature engineering, such as sqrt(x1) or x1 * x2, x1^2 etc. However, one must remember to scale each engineered features.


## Further reading

Books: http://faculty.marshall.usc.edu/gareth-james/ISL/ISLR%20Seventh%20Printing.pdf

https://developers.google.com/machine-learning/glossary/

https://developers.google.com/machine-learning/guides/rules-of-ml/

