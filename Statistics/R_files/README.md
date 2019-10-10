# Introduction of R
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

## String
[regular expression](https://rstudio-pubs-static.s3.amazonaws.com/74603_76cd14d5983f47408fdf0b323550b846.html)
```
\': single quote. You don’t need to escape single quote inside a double-quoted string, so we can also use "'" in the previous example.
\": double quote. Similarly, double quotes can be used inside a single-quoted string, i.e. '"'.
\n: newline.
\r: carriage return.
\t: tab character.

*: matches at least 0 times.
+: matches at least 1 times.
?: matches at most 1 times.
{n}: matches exactly n times.
{n,}: matches at least n times.
{n,m}: matches between n and m times.

[:digit:] or \d: digits, 0 1 2 3 4 5 6 7 8 9, equivalent to [0-9].
\D: non-digits, equivalent to [^0-9].
[:lower:]: lower-case letters, equivalent to [a-z].
[:upper:]: upper-case letters, equivalent to [A-Z].
[:alpha:]: alphabetic characters, equivalent to [[:lower:][:upper:]] or [A-z].
[:alnum:]: alphanumeric characters, equivalent to [[:alpha:][:digit:]] or [A-z0-9].
\w: word characters, equivalent to [[:alnum:]_] or [A-z0-9_].
\W: not word, equivalent to [^A-z0-9_].
[:xdigit:]: hexadecimal digits (base 16), 0 1 2 3 4 5 6 7 8 9 A B C D E F a b c d e f, equivalent to [0-9A-Fa-f].
[:blank:]: blank characters, i.e. space and tab.
[:space:]: space characters: tab, newline, vertical tab, form feed, carriage return, space.
\s: space, ` `.
\S: not space.
[:punct:]: punctuation characters, ! " # $ % & ’ ( ) * + , - . / : ; < = > ? @ [  ] ^ _ ` { | } ~.
[:graph:]: graphical (human readable) characters: equivalent to [[:alnum:][:punct:]].
[:print:]: printable characters, equivalent to [[:alnum:][:punct:]\\s].
[:cntrl:]: control characters, like \n or \r, [\x00-\x1F\x7F].
Note:

[:...:] has to be used inside square brackets, e.g. [[:digit:]].
\ itself is a special character that needs escape, e.g. \\d. Do not confuse these regular expressions with R escape sequences such as \t.
```

[pattern matching](https://stat.ethz.ch/R-manual/R-devel/library/base/html/grep.html)
```
grep, grepl, regexpr, gregexpr and regexec search for matches to argument pattern within each element of a character vector: they differ in the format of and amount of detail in the results.

sub and gsub perform replacement of the first and all matches respectively.
```


## Common approach
[mean(..., trim = True)](https://garstats.wordpress.com/2017/11/28/trimmed-means/) calculate the trim mean instead of the standard mean. An extreme example of trim mean is the median. 

## Cluster
[cluster::clar](https://www.datanovia.com/en/lessons/clara-in-r-clustering-large-applications/) is an extension to k-medoids (PAM) methods to deal with data containing a large number of objects (more than several thousand observations). 

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

