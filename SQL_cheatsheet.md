# SQL Cheat sheet

## Basic Functions
| What?     | How?     |  
| :------------- | :------------- |  
|Running MySQL	| `mysql -username -password`
|Importing	| `mysql -uusername -ppassword < filename`|
| List all databases | `SHOW DATABASES`|
| Create database	| `CREATE DATABASE database;`|
|Use a database	| `USE database;`	|
|List tables in the database |	`SHOW TABLES;`|
|Show the structure of a table |	`DESCRIBE table; `|
|Show columns |`SHOW COLUMNS FROM table;`|

## Math Functions
| What?     | How?     |  
| :------------- | :------------- |  
|Count rows per group|`COUNT(column `<code>&#124;` *)`|
|Average value of group|	`AVG(column)` |
|Minumum value of group|	`MIN(column)` |
|Maximum value of group|	`MAX(column)`|
|Sum values in a group|	`SUM(column)`|
|Absolute value	|`abs(number)`|
|Rounding numbers|	`round(number)`|
|Largest integer not greater|	`floor(number)`|
|Smallest integer not smaller|	`ceiling(number)`|
|Square root|	`sqrt(number)`|
|nth power	|`pow(base,exponent)`
|random number n, 0<n < 1	| `rand()`|
|sin (similar cos, etc.)|	`sin(number)`|

## String Functions
| What?     | How?     |  
| :------------- | :------------- |  
|Compare strings	|`strcmp(string1,string2)`|
|Convert to lower case|	`lower(string)`|
|Convert to upper case|	`upper(string)`|
|Left-trim whitespace (similar right)|	`ltrim(string)`|
|Substring of string	|`substring(string,index1,index2)`|
|Encrypt password	|`password(string`)|
|Encode string|	`encode(string,key)`|
|Decode string|	`decode(string,key)`|
|Get date	|`curdate()`|
|Get time	|`curtime()`|
|Extract day name from date string|	`dayname(string)`|
|Extract day number from date string|	`dayofweek(string)`|
|Extract month from date string	|`monthname(string)`|


## SQL Commands: Modifying
### Create table
Syntax:
```
CREATE TABLE
  table (column1 type [[NOT] NULL] [AUTO_INCREMENT],
  column2 type [[NOT] NULL] [AUTO_INCREMENT],  
  ...  
  other options,  
  PRIMARY KEY (column(s)));   
```

Example:  
```
CREATE TABLE Students (
  LastName varchar(30) NOT NULL,
  FirstName varchar(30) NOT NULL,
  StudentID int NOT NULL,
  Major varchar(20),
  Dorm varchar(20),
  PRIMARY KEY (StudentID)     );
```
---
### Insert data:
Syntax:
```
Insert data	INSERT INTO table VALUES
  (list of values);
```
```
INSERT INTO table SET
  column1=value1,
  column2=value2,
  ...
  columnk=valuek;
```
```
INSERT INTO table (column1,column2,...)
  VALUES (value1,value2...);	INSERT INTO Students VALUES
  ('Smith','John',123456789,'Math','Selleck');
```
Examples:
```
INSERT INTO Students SET
  FirstName='John',
  LastName='Smith',
  StudentID=123456789,
  Major='Math';
```

```
INSERT INTO Students
  (StudentID,FirstName,LastName)
  VALUES (123456789,'John','Smith');
```
```
Insert/Select
  INSERT INTO table (column1,column2,...)
  SELECT statement;
  (See below)	INSERT INTO Students
  (StudentID,FirstName,LastName)
  SELECT StudentID,FirstName,LastName
  FROM OtherStudentTable;
  WHERE LastName like '%son';
```
---
### Delete Data
```
Delete data
DELETE FROM table [WHERE condition(s)];
```

```
(Omit WHERE to delete all data)
  DELETE FROM Students WHERE LastName='Smith';
```
```
DELETE FROM Students
  WHERE LastName like '%Smith%';
  AND FirstName='John';
```
```
DELETE FROM Students;
Updating Data	UPDATE table SET
  column1=value1,
  column2=value2,
  ...
  columnk=valuek
  [WHERE condition(s)];	UPDATE Students SET
  LastName='Jones' WHERE
  StudentID=987654321;
```
---
### Update Data
```
UPDATE Students SET
  LastName='Jones', Major='Theatre'
  WHERE StudentID=987654321 OR
  (MAJOR='Art' AND FirstName='Pete');
```
```
Insert column	ALTER TABLE table ADD COLUMN
  column type options;	ALTER TABLE Students ADD COLUMN
  Hometown varchar(20);
```

---
### Delete Data

-Delete column
```
DROP COLUMN column;
```

-Delete table (Careful!)
```
DROP TABLE [IF EXISTS] table;
```

---
### Others  

- Comments  
```
/* This is a comment */
```

- To determine what database is in use
```
select database();
```

- Rename a table
```
RENAME TABLE oldTablename TO nemTablename;
```
- Export data to tsv
```
 mysql -u s12 -p -e "USE gene_db; SELECT gene_id , sequence, translation FROM transcript" > geneid_transcript_prot.tsv
```
