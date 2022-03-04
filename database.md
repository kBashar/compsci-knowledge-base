## LIKE  
**LIKE**  keyword matches a string.  
```
SELECT * FROM goal 
    WHERE player LIKE 'Alan%'
```
here any player having a name __starting__ with 'Alan' will match the query.
``` 
SELECT * FROM goal 
    WHERE player LIKE '%Alan'
```
here any player having a name __ending__ with 'Alan' will match the query.

## JOIN 
resource: https://en.wikipedia.org/wiki/Join_(SQL)  

__Cross join__ : cartesian product of the joining tables.  
__Inner join__    
     sql:  
     ```
     select * 
     from table_1 join table_2 on (common_column = common_column)
     ```  
     how it works: two joined tables must have __common column__.  
__Outer join__  
    Two types of outer join  
        1. left outer join  
        2. right outer join  
    left and right is based on the sides of 'join' keyword.  
__Left outer join__:   
    example:   
    <code>A LEFT OUTER JOIN B</code>  
    1. Joined table contains all rows of left table (A) even if there are such rows in right Table (B) that don't satisfy join-condition.  
    2. In case of non matching rows with the right table, joined table makes the row containing left table columns with values and right table columns with NULL.  

__Right outer join__:  
   sql:  
   how it works:
