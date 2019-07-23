# Statistics and probability

## [Permuations & Combinations](https://www.mathsisfun.com/combinatorics/combinations-permutations.html)

## [Data distribution](https://mathbitsnotebook.com/Algebra1/StatisticsData/STShapes.html)

## [maximum likelihood](https://towardsdatascience.com/probability-concepts-explained-maximum-likelihood-estimation-c7b4342fdbb1)

## [hypothesis testing](https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/hypothesis-testing/):
    
## Z-test

## t-test

## [Chi-sqaure test](https://en.wikipedia.org/wiki/Chi-squared_test)

A chi-square test for independence compares two variables in a contingency table to see if they are related. They degree of freedom is the sum of number of row and columns - 2. 

<img src = images/chi-sqaure.png height = 100>



## Fisher's Exact test 
The test is useful for categorical data that result from classifying objects in two different ways. It has small number of examples and it is also a rather conservative method, meaning the p value it calcultaed is usually large. The origin Fisher's exact test is like this: 

There is a women who claimed that she can tell the difference if the milk is put before the tea or after. Fisher asked her to drink 8 cup of teas, and told her that 4 of them have milk first and 4 of them have tea first. The null hypothesis is that, there is no difference between whether it is tea or milk being added first. He chose p<0.05 then he is confident to reject the null hypothesis. If the women's guess is random, in total, there are 8 chose 4, which is 8*7*6*5/4*3*2 = 70 difference combination, among which, there is only 1 that is the correct combination. Therefore, if the women guessed all correct, the p values is 1/70, which is around 0.014 < 0.5. Therefore, he will rejected the hypothesis. However, if the women only guessed three that is correct, then there are 4 choose 1 that is A but she guessed B and 4 choose 1 that is B but she guessed A, therefore, there are 4X4 = 16 combinations. Then the p values is 16/70, which is around 0.23 > 0.05, therefore, he will reject the null. 

Another example is that:
We have half female and male students. The null hypothesis is that they are equally likely to be studying at this time. We have observation number as followed:

<img src = images/fisher.png height = 200>

The p value will be:

<img src = images/fisher2.png height = 100>

Differnece between Fisher and Chi-square test:

They are calculating the same thing using different ways. The Fisher's exact test always give the correct p value while the chi-sqaure test on;y gives you an approximate, which doesn't work for small dataset. The Fisher's exact test is more computationally expensive, therefore, often it is only be used for a small data set. However, it is recommended, when it is possible, used Fisher's exact test instead of Chi-sqaure test. 


## Type I error

## Type II error

## p value

## Recall, Percision, F1 score

## [A/B testing](https://conversionxl.com/blog/testing-statistics-mistakes/)

## [Designing an Experiment, Power Analysis](http://www.statsoft.com/Textbook/Power-Analysis)

## [Nonparametric statistics](https://en.wikipedia.org/wiki/Nonparametric_statistics)

## [Comparing two distribution: The Kullback Leibler distance (KL) and Kolmogorov–Smirnov test (KS)](https://stats.stackexchange.com/questions/9311/kullback-leibler-vs-kolmogorov-smirnov-distance)

## [Markov chain](https://en.wikipedia.org/wiki/Markov_chain)
