# Data Science Make Easy
The purpose of this github repo is to put some basic topics in data science together

## Data Hanlding
[Missind data](https://www.kaggle.com/dansbecker/handling-missing-values)

[Resampling](https://medium.com/analytics-vidhya/resampling-methods-statistical-learning-8c3da6fe6d24)

[Imbalanced data](https://machinelearningmastery.com/tactics-to-combat-imbalanced-classes-in-your-machine-learning-dataset/)


## [Statistic](https://github.com/YIZHE12/DataScienceMakeEasy/tree/master/Statistics)
 
## [Data Structure](https://github.com/YIZHE12/DataScienceMakeEasy/tree/master/data_structures)

## [Algorithm](https://github.com/YIZHE12/DataScienceMakeEasy/blob/master/algorithm/README.md)

## Machine Learning 

Books: http://faculty.marshall.usc.edu/gareth-james/ISL/ISLR%20Seventh%20Printing.pdf

https://developers.google.com/machine-learning/glossary/

https://developers.google.com/machine-learning/guides/rules-of-ml/

#### What is Machine Learning?

Arthur Samuel: "the field of study that gives computers the ability to learn without being explicitly programmed." What set aside machine learning from other computer sience method is the ability to adapt. 

Tom Mitchell: "A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E."

#### Supervised and unsupervised learning

The major difference between supervised and unsupervised learning is if there is a target variable. Two common tasks in unsupervised learning: clustering and association. 


##### Unsupervised learning:
Clustering: given a data set, one can cluster the samples into groups, based on the similarities among the samples within the data set. 

Association:  given a data set, the association task is to uncover the hidden association patterns among the attributes of a sample.

##### Supervised learning:
If the output of a machine learning model is discrete values, e.g. a boolean value, we then call it a classification model. While we call the model that outputs continuous values as regression model.

##### Semi-supervised learning
In a scenario where the data set is massive but the labeled sample are few, one might find the application of both supervised and unsupervised learning. We can call this task as semi-supervised learning. 

For example, one would like to predict the label of images, but only 10% of the images are labeled. By applying supervised learning, we train a model with the labeled data, then we apply the model to predict the unlabeled data. It would be hard to convince ourselves that the model would be general enough, after all we learnt from only the minority of data set. A better strategy could be to first cluster the images into groups (unsupervised learning), and then apply the supervised learning algorithm on each of the groups individually. The unsupervised learning in the first stage could help us to narrow down the scope of learning so that the supervised learning in the second stage could obtain better accuracy.




## Deep Learning

## System design

## SQL
https://lagunita.stanford.edu/courses/DB/SQL/SelfPaced/courseware/ch-sql/seq-exercise-sql_movie_query_core/

Execise:
https://www.hackerrank.com/challenges/harry-potter-and-wands/problem
https://www.techbeamers.com/sql-query-questions-answers-for-practice/
https://www.w3schools.com/sql/sql_update.asp

Window function:
https://classroom.udacity.com/courses/ud198/lessons/fec9c33e-daea-4a5d-827e-41a09c6fe371/concepts/4c71795c-8ebf-4a3f-b951-494220b702cc

Rules for normalized tables:

1. Every row has the same number of columns.

2. There is a unique key and everything in a row says something about the key.

3. Facts that don't relate to the key belong in different tables.

4. Tables shouldn't imply relationships that don't exist.


## Case study

Resource:

https://www.analyticsvidhya.com/blog/tag/case-study/

## Python

#### Panda tricks
https://www.youtube.com/watch?v=RlIiVeig3hc

