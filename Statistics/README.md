# Statistics and probability

## [Permuations & Combinations](https://www.mathsisfun.com/combinatorics/combinations-permutations.html)

## [Data distribution](https://mathbitsnotebook.com/Algebra1/StatisticsData/STShapes.html)

### Binomial distribution

<img src = images/bi1.png height = 200>

<img src = images/bi2.png height = 100>

When p is large, a binominal distribution is similar to a normal distribution. Therefore, instead of calculating the binominal distribution for a certain value, we can calculate the area under the curve using a normal distribution instead. For example:

<img src = images/bi3.png height = 200>

<img src = images/bi4.png height = 200>


## [Experimental Design]

Experimental design has four main components:

(1) Control: compare treatment of interest of a control group

(2) Randomize: randomly assign subjects to treatments

(3) Replicate: collect a sufficiently large sample, or replicate the entrie study

(4) Block: block for variables known or suspected to affect the outcome

For examples, you want to know if an energy gel will enhance your sport performance. Your subjects have amateur athletes and pros. These are your blocks. You will want to randomly assign equal number of amateur athletes and pros into each group (with or without the energy gel). Blocking is like stratifying. 

Blocking vs explanatory variables

(1) explanatory variables: factors, which are conditions that we can impose on experimental units

(2) blocking variables: characteristics that the experimental units come with

## Probability

Disjoint event: two events are mutually exclusive

Disjiont event A and B, P(A or B) = P(A) + P(B)

For all event: P(A or B) = P(A) + P(B) - P(A and B), if A and B are disjoint event, then P(A and B) = 0, therefore, P(A or B) = P(A) + P(B)

Complementary event (A and not A) is always disjoint events

if P(A|B) = P(A), then A and B are independent events

if A and B are independent events, P(A and B) = P(A) x P(B)





## [maximum likelihood](https://towardsdatascience.com/probability-concepts-explained-maximum-likelihood-estimation-c7b4342fdbb1)

## [hypothesis testing](https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/hypothesis-testing/):
    
## Z-test and t-test
<img src = images/PDF_norm.png height = 150>

Before using either Z-test or t-test, always check if the distribution is normal! If the sample size is large or the population variance is known, use Z -test, otherwise use t-test. Often, when n>30, you can use z-test, and use the sample standard deviation/sqrt(sample size) as the estimation of the population standard deviation. Comparing the shape of t-test and z-test: t-test has a larger tail - more uncertainty. Meaning, for the same p-value, the critical value of t-test need to be closer to the center than the z-test.

<img src = images/z-test.png height = 120>

<img src = images/z-test2.png height = 120>

The normal distribution is commonly associated with the 68-95-99.7 rule which you can see in the image above. 68% of the data is within 1 standard deviation (σ) of the mean (μ), 95% of the data is within 2 standard deviations (σ) of the mean (μ), and 99.7% of the data is within 3 standard deviations (σ) of the mean (μ).

<img src = images/rule.png>

## [Chi-sqaure test](https://en.wikipedia.org/wiki/Chi-squared_test)

A chi-square test for independence compares two variables in a contingency table to see if they are related. They degree of freedom is the sum of number of row and columns - 2. 

<img src = images/chi-sqaure.png height = 100>

Example chi-squared test for categorical data
Suppose there is a city of 1,000,000 residents with four neighborhoods: A, B, C, and D. A random sample of 650 residents of the city is taken and their occupation is recorded as "white collar", "blue collar", or "no collar". The null hypothesis is that each person's neighborhood of residence is independent of the person's occupational classification. The data are tabulated as:

<img src = images/chi-sqaure_exp.png height = 200>

The expected values for white collar in neighborhood A will be: (349/650)X150. We can calculated all the expected values and then use the above equation to get the chi-sqaure value. Then we will look at the chi-sqaure table with this value and the degree of freedom to find the p value. 

A related issue is a test of homogeneity. Suppose that instead of giving every resident of each of the four neighborhoods an equal chance of inclusion in the sample, we decide in advance how many residents of each neighborhood to include. Then each resident has the same chance of being chosen as do all residents of the same neighborhood, but residents of different neighborhoods would have different probabilities of being chosen if the four sample sizes are not proportional to the populations of the four neighborhoods. In such a case, we would be testing "homogeneity" rather than "independence". The question is whether the proportions of blue-collar, white-collar, and no-collar workers in the four neighborhoods are the same. However, the test is done in the same way.


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
