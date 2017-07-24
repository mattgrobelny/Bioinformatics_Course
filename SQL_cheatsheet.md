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
### Import local data:
Example:
```
LOAD DATA LOCAL INFILE '/home/grobeln2/gene_db_prot_vs_hsa_blast_out.tsv'
INTO TABLE Blast_output
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n';
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

---
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

### Create, Select and Insert at the same time
```
CREATE TABLE interests
(
int_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
interest VARCHAR(50) NOT NULL,
contact_id INT NOT NULL,
)

AS
SELECT some_field FROM my_contacts;
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
```
Insert data into a table

INSERT INTO table 
(column1,column2, ... )
VALUES
(value1, value2, ...);
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
## Alter a Table

Add a column to table, make it an auto incrementing int placing the column first.
Also make the column a primary key. 
```
ALTER TABLE my_contacts
ADD COLUMN contacts_id INT NOT NULL AUTO_INCREMENT FIRST, 
ADD PRIMARY KEY (contacts_id);
```  

### Change name of table  

```
ALTER TABLE projects
RENAME TO project_list;
```  

### Change column to Auto-incrementing values

```
ALTER TABLE project_list
CHANGE COLUMN number project_id INT NOT NULL AUTO_INCREMENT
ADD PRIMARY KEY (project_id);
```

### Change two columns to Auto-incrementing values

```
ALTER TABLE project_list
CHANGE COLUMN decription_info project_details VARCHAR(100)
CHANGE COLUMN job con_name VARCHAR(30);
```

### Change column type  

```
ALTER TABLE project_list
MODIFY COLUMN project_details BLOB; # new column type here
```

### Delete column  

```
ALTER TABLE project_list
DROP COLUMN project_details;
```

---
## Flow Control

```
Output into a table. 

SELECT ISO,
CASE 
    WHEN ISO = 'BT' THEN Population
    ELSE ''
  END AS 'Asia', # using END AS outputs all TRUE conditionals to be under the column its labeled as 
CASE 
    WHEN ISO = 'DE' THEN Population
    ELSE ''
  END AS 'Europe',
CASE 
    WHEN ISO = 'CA' THEN Population
    WHEN ISO = 'MX' THEN Population
    ELSE ''
  END AS 'North America',
CASE 
    WHEN ISO = 'AR' THEN Population
    WHEN ISO = 'BR' THEN Population
    ELSE ''
  END AS 'South America'
FROM Country;

```  

---  
## Foreign key
Creating  a table with a foreign key
```
CREATE TABLE interests(
int_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
interest VARCHAR(50) NOT NULL,
contact_id INT NOT NULL,
CONSTRAINT my_contacts_contact_id_fk FOREIGN KEY (contact_id)
REFERNCES my_contacts (contacts_id) # where the FK references to 
);
```    

---  
## Joining
Join data from multiple tables
```
SELECT ingredients_table3.ingredient_name, Cooking_Dir_Table.dir_usage FROM ingredients_table3
INNER JOIN Cooking_Dir_Table 
ON
ingredients_table3.Dir_usage_key_fk = Cooking_Dir_Table.Dir_id_key; # where values equals
```    

```
SELECT ingredients_table3.ingredient_name, Cooking_Dir_Table.dir_usage FROM ingredients_table3
INNER JOIN Cooking_Dir_Table 
ON
ingredients_table3.Dir_usage_key_fk <> Cooking_Dir_Table.Dir_id_key;  # where values do not equal
```
Useful to identify which combinations are absent 
---  
## Other Useful Functions  

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

- Show first 10 rows  
```
SELECT * FROM [TABLE] LIMIT 10;
```

- Copy a table from one database to another
```
CREATE TABLE db2.table LIKE db1.table;
INSERT INTO db2.table SELECT * FROM db1.table;
```

- Select Unique rows
```
SELECT DISTINCT fieldName FROM tableName;
```

- Select only duplicate rows and count them 
```
SELECT COUNT(state) as numberOfcustomers FROM Customers
WHERE state IN (Select state FROM Customers 
GROUP BY state 
HAVING COUNT(state) > 1);```

- Table Aliases

```
Select profession AS mc_prof
FROM my_contacts AS mc 
GROUP BY mc_prof
ORDER BY mc_prof
```
