import sqlite3
import pandas as pd
conn = sqlite3.connect('data.sqlite')


# ---- One to One Relationships ----

# Sales Rep Employees
q = """
SELECT firstName, lastName, email
FROM employees
WHERE jobTitle = 'Sales Rep'
;
"""
df = pd.read_sql(q, conn)
print("Number of results:", len(df))
print(df.head())


# Cities for Sales Rep Employees - join offices table to display city as well
q = """
SELECT firstName, lastName, email, city
FROM employees
JOIN offices
   USING(officeCode)
WHERE jobTitle = 'Sales Rep'
;
"""
df = pd.read_sql(q, conn)
print("Number of results:", len(df))
print(df.head())


# ---- One to Many Relationships ----

# selecting the product line name and text description for all product lines.
q = """
SELECT productLine, textDescription
FROM productlines
;
"""
df = pd.read_sql(q, conn)
print("Number of results:", len(df))
print(df)


# ---- Joining with Products ----

# join that table with the products table, and select the vendor and product description.
q = """
SELECT productLine, textDescription, productVendor, productDescription
FROM productlines
JOIN products
    USING(productLine)
;
"""
df = pd.read_sql(q, conn)
print("Number of results:", len(df))
print (df.head())


# ---- Many to Many Relationships ----

# Just Offices
q = """
SELECT *
FROM offices
;
"""

df = pd.read_sql(q, conn)
print('Number of results:', len(df))


# Just Customers
q = """
SELECT *
FROM customers
;
"""

df = pd.read_sql(q, conn)
print('Number of results:', len(df))


# Joined Officesand Customers
q = """
SELECT *
FROM offices
JOIN customers
    USING(state)
;
"""

df = pd.read_sql(q, conn)
print('Number of results:', len(df))
print(df.head())


conn.close()