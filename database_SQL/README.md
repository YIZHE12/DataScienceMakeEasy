## Database
What is a database?

It is a repository of data. Data stored in tabular form is a relational atabase.

RDBMS = Relational databse management system. 

Three main building block for a data model: Entity, Attribute and relationship (one to one, one to many or many to many).
A entity is a table in the database, and attribute is a column. For example, book as an entity, may have attributes as book_id, book_title, etc.

Rules for normalized tables:

1. Every row has the same number of columns.

2. There is a unique key and everything in a row says something about the key.

3. Facts that don't relate to the key belong in different tables.

4. Tables shouldn't imply relationships that don't exist.

## SQL (Structured Query Language)
### Basic SQL
The five basic command of SQL CREATE, INSERT, SELECT, UPDATE and DELETE

1. SELECT

<img src = images/SQL_limit.png height = 200>

2. CREATE
<img src = images/SQL_create.png height = 200>

create temporally table:

<img src = images/SQL_temp_table.png height = 150>

3. INSERT
<img src = images/SQL_insert1.png height = 160>
<img src = images/SQL_insert2.png height = 300>

4. Comments
```
- - for one line 
/* 
*/ for a section
```

### Filter SQL

You often do 
```
SELECT column1_name, column2_name, column3_name
FROM table_name
WHERE column1_name =/>/< number/string
```
<img src = images/WHERE.png height = 150>

<> means do not inlcude

<img src = images/WHERE2.png height = 150>

You can also use 'between ... and ...' instead of operators


## NoSQL (Not only SQL)




## Further reading
https://lagunita.stanford.edu/courses/DB/SQL/SelfPaced/courseware/ch-sql/seq-exercise-sql_movie_query_core/

Execise:
https://www.hackerrank.com/challenges/harry-potter-and-wands/problem
https://www.techbeamers.com/sql-query-questions-answers-for-practice/
https://www.w3schools.com/sql/sql_update.asp

Window function:
https://classroom.udacity.com/courses/ud198/lessons/fec9c33e-daea-4a5d-827e-41a09c6fe371/concepts/4c71795c-8ebf-4a3f-b951-494220b702cc
SQLite: https://www.tutorialspoint.com/sqlite/index.htm




