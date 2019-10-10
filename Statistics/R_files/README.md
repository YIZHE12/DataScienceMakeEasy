# R in statistics
## Common commands 
getwd() # get working directory

read.csv('xxx.csv') # read csv file

dir() # show all files in current directory

na.rm=TRUE # ignore NA values in mean or average oeprations

[seq](https://www.rdocumentation.org/packages/base/versions/3.6.1/topics/seq) is a command to create sequences 

[rbinom](https://www.rdocumentation.org/packages/base/versions/3.6.1/topics/seq) create binomial distribution

[paste and paste0](https://www.r-bloggers.com/difference-between-paste-and-paste0/) to concatenate strings

[rep](https://www.rdocumentation.org/packages/base/versions/3.6.1/topics/rep) to repeat strings

[cut](https://www.rdocumentation.org/packages/base/versions/3.6.1/topics/cut) divide continuous variable into factors

[pretty](https://www.rdocumentation.org/packages/base/versions/3.6.1/topics/pretty) create pretty breakpoints to divide a continuous variable

[cat](https://www.math.ucla.edu/~anderson/rw1001/library/base/html/cat.html) concatenates the objects

[%in%](http://www.datasciencemadesimple.com/in-operator-in-r/) find if an element belong to a vector

[stri_enc_toascii](https://www.rdocumentation.org/packages/stringi/versions/1.4.3/topics/stri_enc_toascii) convert string to ASCII

## Enviroment variables
To get the enviroment variables of a function
```
ls(enviroment(function_name))
```
To get the value of a variable inside a function
```
get('variable_name', enviroment(function_name))
```

## Resources:

[R very short introduction](https://cran.r-project.org/doc/contrib/Torfs+Brauer-Short-R-Intro.pdf)

[R Penn State Statistics](https://newonlinecourses.science.psu.edu/stat484/node/204/)

[R commands](https://d396qusza40orc.cloudfront.net/statistics/lab_resources/RCommands.html)

[R cheat sheet](https://cran.r-project.org/doc/contrib/Short-refcard.pdf)

[R video course](https://www.pluralsight.com/courses/r-programming-fundamentals)

[more video](https://www.youtube.com/playlist?list=PLcgz5kNZFCkzSyBG3H-rUaPHoBXgijHfC)

[R tutorial](https://www.tutorialspoint.com/r/index.htm)

[Beautiful R report](http://swcarpentry.github.io/r-novice-gapminder/)


## Book
[The art of R programming](http://diytranscriptomics.com/Reading/files/The%20Art%20of%20R%20Programming.pdf)

[Advanced R](https://englianhu.files.wordpress.com/2016/05/advanced-r.pdf)

