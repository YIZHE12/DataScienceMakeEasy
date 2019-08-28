# What is Machine Learning?

Arthur Samuel: "the field of study that gives computers the ability to learn without being explicitly programmed." What set aside machine learning from other computer sience method is the ability to adapt. 

Tom Mitchell: "A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E."

## Part 1: Supervised and unsupervised learning

The major difference between supervised and unsupervised learning is if there is a target variable. Two common tasks in unsupervised learning: clustering and association. 

### Unsupervised learning:
Clustering: given a data set, one can cluster the samples into groups, based on the similarities among the samples within the data set. 

Association:  given a data set, the association task is to uncover the hidden association patterns among the attributes of a sample.

### Supervised learning:
If the output of a machine learning model is discrete values, e.g. a boolean value, we then call it a classification model. While we call the model that outputs continuous values as regression model.

### Semi-supervised learning
In a scenario where the data set is massive but the labeled sample are few, one might find the application of both supervised and unsupervised learning. We can call this task as semi-supervised learning. 

For example, one would like to predict the label of images, but only 10% of the images are labeled. By applying supervised learning, we train a model with the labeled data, then we apply the model to predict the unlabeled data. It would be hard to convince ourselves that the model would be general enough, after all we learnt from only the minority of data set. A better strategy could be to first cluster the images into groups (unsupervised learning), and then apply the supervised learning algorithm on each of the groups individually. The unsupervised learning in the first stage could help us to narrow down the scope of learning so that the supervised learning in the second stage could obtain better accuracy.

## Part 2: Bias and variance
Bias is a learner’s tendency to consistently learn the same wrong thing. Variance is the tendency to learn random things unrelated to the real signal

<img src = images/bias.png>

<img src = images/variance.png>

<img src = images/trade-off.png height = 300>

<img src = images/error-eq.png height = 30>

## Part 3: Data Hanlding

[Missind data](https://www.kaggle.com/dansbecker/handling-missing-values)

[Resampling](https://medium.com/analytics-vidhya/resampling-methods-statistical-learning-8c3da6fe6d24)

[Imbalanced data](https://machinelearningmastery.com/tactics-to-combat-imbalanced-classes-in-your-machine-learning-dataset/)

## Part 4: Generative VS Discriminative Models
In General, A Discriminative model models the decision boundary between the classes. A Generative Model explicitly models the actual distribution of each class. A Generative Model learns the joint probability distribution p(x,y). It predicts the conditional probability with the help of Bayes Theorem. A Discriminative model learns the conditional probability distribution p(y|x). For example, Generative adversarial network, Variational autoencoder, Boltzmann machine, Latent Dirichlet allocation, Gaussian mixture model, Naïve Bayes, Bayesian networks, Markov random fields and Hidden Markov Models (HMM) are generative classifiers, while logistic regression,traditional neural networks, k-nearest nearest neighbour, Support Vector Machines and conditional Random Fields (CRF)s are discriminative classifiers. k-nearest neighbors algorithm

a generative model is a model of the conditional probability of the observable X, given a target y, symbolically, P(X|Y = y)

a discriminative model is a model of the conditional probability of the target Y, given an observation x, symbolically, P(Y|X = x)

## Part 5: Feature selection

Feature selection approaches try to find a subset of the features. The three strategies are: the filter strategy (e.g. information gain), the wrapper strategy (e.g. search guided by accuracy), and the embedded strategy (selected features add or are removed while building the model based on prediction errors).

In [sklearn](https://scikit-learn.org/stable/modules/feature_selection.html), there are several implementation of feature selection, for examples: 

#### Filter strategy

1. Removing features with low variance 

2. Univariate feature selection based on statistical elements, such as correlation between variables

#### Wrapper strategy

1. Recursive feature elimination is to select features by recursively considering smaller and smaller sets of features.

2. Feature selection using SelectFromModel in sklearn - two common models (L1 and trees), but can use any other models.

#### Embedded strategy

PCA, LDA, GDA, Autoencoder, tSNE etc.





## Further reading

Books: http://faculty.marshall.usc.edu/gareth-james/ISL/ISLR%20Seventh%20Printing.pdf

https://developers.google.com/machine-learning/glossary/

https://developers.google.com/machine-learning/guides/rules-of-ml/

Video: https://www.youtube.com/watch?v=Gv9_4yMHFhI&list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF
