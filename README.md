# Two solutions for the database summary problem

The book itself has a solution for making summaries of a given table named driver_log which 
can be found [on its official download website.](http://www.kitebird.com/mysql-cookbook/downloads-3ed.php)

## First solution

Create an **infinite generator** which iterates through the rows and compare it to a list of the 
employees who are in the records to create the summary on the fly.

## Second solution

Create a **list of employees** and for each one execute a query to get all of their data and summarize 
all the data also on the fly.

***I saw that the given solution would consume a lot of memory and resources making it unable to 
handle tables with a conconsiderable amount of rows.***

## [LINK TO THE BOOK ON AMAZON](https://www.amazon.com/MySQL-Cookbook-Paul-DuBois/dp/059652708X)
