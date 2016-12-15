# SQL - Relational database and Structured Query Language

## What is a database?  

- How to organize data?

## Relational database
- Grouping data across tables
- Tables have types:  
  - float, int, date, time, enum, char ..
- Set or subset of columns is a tuple
- Subsets: only row combinations that are *true* according to relational algebra

## Rules which make a database unique
- Avoids redundancy --> never store the same data more than once
- Make all data accessible
- Each entry has a uniq id
- Linked data is connected by associating the uniq id of the data its to be grouped with.


## Init database
- Decide on tables, entries and types of data which are accepted into a table.
- Define relationship between tables:
  - one to one
  - one to many

## SQL - four basic operations

1. `Select` data from a database table

  `SELECT [columns] FROM [table]`  

  `SELECT [columns] FROM [table] WHERE [conditional]`   
  *conditional is filter*

  `SELECT [columns] FROM [table] WHERE [conditional] LIMIT [num]`   
  *limit the number of outputs*

  `SELECT [columns] FROM [table] ORDER by [column]`   

2. `Update`
3. `Insert`
4. `Delete`
