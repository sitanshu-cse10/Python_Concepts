<------------------------------------Python Database Programming(PDBC) ------------------------->
It is very common requirement to save data for the future purpose

1. Temporary Data Storage ---> The storage In the Python Virtual Machine

2. Permanent Data storage --->
                             A.....> The files system 
  
Limitations:
  1.Huge Data
  2.No sql data
  3.Security
  4.prevent duplicate data
  5.data inconsistency data
B.....>  Database
   Etc   Cloud Storage

1. We can store huge amount of data
2. QL support
3. Security is More
4. Tables
 
Limitations
  1. cannot hold very huge of info like tera bytes of data
  2. Structured data but not for unstructured data and semi structured data
  
Next level Advance data (Hadoop ,Cloud,Hana)

PDBC.
     .....>
 Module Name cx_Oracle
  
 Module Name pymysql

<---------------Standard Steps to communicate with Databse------------------->
1. import that database specific module
   import cx_Oracle
   import pymysql
   
2. Establish Connection between Python program and Db
   con=cx_Oracle.connect(database information):
   eg
   con=cx_Oracle.connect('scott/tiger@localhost')
   
3. Cursor object
   cursor =con.cursor()
   
   
4. Execute our  Sql Query
         cursor.execute(sql query) ----> as single query 
	 cursor.executescript(sql queries)---> To excute a string of sql queries 
	 cursor.excuetemany()-----------> to excuete a parameterized query
5. Fetch the Results
    cursor.fetchone()----->TO fetch only one row
    cursor.fetchall()---->TO fetch all rows	
    cursor.fetchmany(n)---->TO fetch n rows

6. commit()
   rollback()
   
7.  cursor.close()
    con.close()
    close()
	
<--------Working with Oracle database------>
 
Example 
import random
import cx_Oracle

<--- USe pip install cx_Oracle---->

1. Program connect with oracle and print its Version

import cx_Oracle
con=cx_Oracle.connect('system/system@localhost')
if con!=None:
   print('Connection Establishment successfully')
   print('Version:',con.version)
else:
    print('Connection Establishment unsuccessfully')
con.close()
   
2. Program to create employee table in the database
  
 ---> create table employee(eno number,ename varchar2(10),esal number(10,2),eaddr varchar2(10))
   

import cx_Oracle
try:
   query="create table employee(eno number,ename varchar2(10),esal number(10,2),eaddr varchar2(10))"
   conn=cx_Oracle.connect('scott/tiger@localhost')
   cursor=con.cursor()
   cursor.excute(query)
   print('Table created successfully')
except cx_Oracle.DatabaseError as e:
    if con:
       con.rollback()
	   print("There is a problem:",e)
	  
finally:
    if cursor:
       cursor.close()
    if con:
       con.close()
	  
3. To drop table
   query ="drop table employee"	


4. Insert row into database 
     query = "insert into employee values(100,'Yash',1000000000,'Kanpur')"
     
import cx_Oracle
try:
   query = "insert into employee values(100,'Yash',1000000000,'Kanpur')"
   conn=cx_Oracle.connect('scott/tiger@localhost')
   cursor=con.cursor()
   cursor.excute(query)
   con.commit()
   print('Table created successfully')
except cx_Oracle.DatabaseError as e:
    if con:
       con.rollback()
	   print("There is a problem:",e)
	  
finally:  #close the  resources
    if cursor:
       cursor.close()
    if con:
       con.close()
	   
	   
5. insert multiple records into database
   executemany() method
   query = "insert into employee values(100,'Yash',1000000000,'Kanpur')"
   records=[(200,'Sunny',2000,'MUmbai'),(300,'Sun',2000,'Delhi'),(200,'Sunny',200,'Hyberbadad')]
   cursor.executemany(query,records)
   con.commit()


6. import cx_Oracle
   try:
      con=cx_Oracle.connect('system/system@localhost')
      cursor=con.create()
      while True:
           eno=int(input('Enter the employee Number'))
           name=input('Enter the employee Number'))
           esal=int(input('Enter the employee Salary'))
           eaddr=input('Enter the employee Number')
           query="insert into employee values(%d,'%s',%f,'%s')"
           cursor.execute(query %(eno,ename,esal,eaddr))
           con.commit()
           print('Records inserted Succesfully)
           option=input('Do you want to insert more?..)
           if option =='No':
              break
   except cx_Oracle.DatabaseError as e:
          if con:
             con.rollback()
             print('There is a problem')   
  finally:  #close the  resources
    if cursor:
       cursor.close()
    if con:t
       con.close()   
  




7.
  import cx_Oracle
try:
   conn=cx_Oracle.connect('scott/tiger@localhost')
   cursor=con.cursor()
   increment=float(input('Enter increment Salary'))
   salrange=float(input('Enter the Salary Range'))
   query="update employee set esal=esal+%f where esal<%f"
   cursor.excute(query %(increment,salrange))
   con.commit()
   print('updates  successfully')
except cx_Oracle.DatabaseError as e:
    if con:
       con.rollback()
	   print("There is a problem:",e)
	  
finally:  #close the  resources
    if cursor:
       cursor.close()
    if con:
       con.close()






















