The main principle behind the ensemble model is that a group of weak learners come together to form a strong learner, 
thus increasing the accuracy of the model

### Bootstrapping
Bootstrap refers to random sampling with replacement - total number of examples in the sampling pool doesn't change. 
This method can help to better understand the mean and standand deviation from the dataset. Think about student t-test.

### Bagging and random forest
Bagging is short for Bootstrap Aggregation.
Bagging used a series of weak learner built (often in parallel) by subsampling examples (with replacement). 
The original bagging trees used all features, 
but random forest used bagging on featuers too, to reduce the corelation between different trees. Random forest does not use purning.

### Boosting
Boosting does not involve bootstrap sampling. In boosting, each model that runs, dictates what features the next model will focus on. 
The next model always focus what was wrongly predictive by the previous models.

Bagging and Boosting both decreased the variance of your model, thus resulting in higher stability. 
However, bagging is not as effective as boosting in reducing bias. 
On the contrast, if the model is overfitting, then bagging is more effective. 
Unlike bagging and random forests, boosting can overfit if there are too many trees.

### Fine tuning
An optimal number of hyperparameters can be found using cross-validation, or by observing the out-of-bag error in bagging and random forest: 
the mean prediction error on each training sample xᵢ, using only the trees that did not have xᵢ in their bootstrap sample.

For boosting, the fine tuning value is often the depth of the trees.

### Comparing several algorithm

#### Random forest

Advantages:
No need for normalization, can handle missing data, can run in parallel, 
very good in reducing dimension, 
can added class weight to handle class imbalance, 
good perforamnce in both variance and bias.

Disadvantages:
No as good in regression than in classification - not continuous output and cannot handle if y is out of range.
Low interpretability. 

#### AdaBoost
Used stump tree (only has one node and two leaves). 
Unlike random forest which each tree has equal vote, some Adaboost tree can have more votes than others.
The trees are related and the order of the trees is important. 
The vote that a tree can have is related to the error it produced. 
Note the vote can be negative. We can also called the vote as the amount of say.

Amount of say = 1/2 log((1- te)/te), where te is the total error

<img src = ../images/amount-of-say.png height = 100>
<img src = ../images/amount-of-say2.png height = 300>

After each iteration, we changed the sample weights:

For the wrongly classified examples:

New sample weight = sample wieght x exp(amount of say)

<img src = ../images/new-weight.png height = 300>

In this way, if the previous classifier is good, the amount of say is high, 
then the new sample weight will be much larger. However, if the previous classifier is bad,
the amount of say is low, then the new sample weight will only increase little.

For the correctly classified examples:

New sample weight = sample wieght x exp(-amount of say)

All the sample weight need to be rescaled to make it sum up to 1 before each iteration.

We can either used a weighted gini index for the next tree or we can resample the data with weights 
and use the normal gini index formular. 

[Video](https://www.youtube.com/watch?v=LsK-xG1cLYA)

#### Gradient Boosting Decision Tree (GBDT)

1. Regression:

GBDT starts at making a single leaf, which is the averaged of all output values if they are continuous variables. This leaf represents an initial guess ofr the target values of all the samples. Then gradient boost build a tree, usually has 8 - 32 leaves. GBDT build the next trees based on the error from the previous tree. After the first tree, we calculated the residual of the predictions and built the second tree based on the residual and not the target variables. Note that the number of residual is smaller than the number of leaves, so we will merge some residuals and put them in the same leaves by using the averaged number. Now, comnbined with the previous tree, we have a new value, which is the output of tree1 + learning rate * residual predition of tree2. The learning rate is 0 - 1. Most of time, we take 100 trees.

[Example](https://www.youtube.com/watch?v=3CC4N4z3GJc)

[Math](https://www.youtube.com/watch?v=2xudPOBz-vs)

2. Classification

Odds is the number of positive examples/ number of negative examples. The log(odd) is our initial prediction (leave).

Just as in logistic regression, the easiest way ot use the log(odds) for classification is to convert it to probability and we do that with a logistic function:

Probability = exp(log(odds))/(1+exp(log(odds)) = 1/(1+exp(-log(odds))

So now if this probability is > 0.5 (or other threshold you chose), then the output is 1. 

So now we calculated the pseudo residuals just as in regression (0 or 1 - predictions) and build the next tree to predict the residuals.

However, unlike regression, now we cannot simplily sum up prediction and residuals.

[Example](https://www.youtube.com/watch?v=jxuNLH5dXCs)

[Math](https://www.youtube.com/watch?v=StWY5QWMXCw)



For more on this: https://blog.csdn.net/zwqjoy/article/details/82150528 (in Chinese)
