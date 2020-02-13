import pyodbc

# Look at our package for the documentation to connect our SPECIFIC database


# get the parameters it's looking for...
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
# conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server +';DATABASE=' + database + ';UID=' + username + ';PWD=' + password  )

# like a password, as user name and location to communicate

# use the pydbc to create a instance of the DB
docker_new_conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

# Create cursor object /// MAintains state! meaning whem ypou fetch a record
cursor = docker_new_conn.cursor()

# Try to get all the products out

# query = 'SELECT * FROM Products'
# cursor.execute(query)

# Get one row from the db
# row = cursor.fetchone()
# print(row)

# When we do fetchone() on the same cursor we get the second row
# row = cursor.fetchone()
# print(row)
# use their methods to send in requests

# Get all customers using fetchall
# BAD: IT is dangerous to fetchall() you are most likely to crash your server.
# new_cursor = docker_new_conn.cursor()
# customer_cursor = new_cursor.execute('SELECT * FROM Customers').fetchall()
#
# print(customer_cursor)
#
# for item in customer_cursor:
#     print(item)

# Better way of using fetchone()
rows = cursor.execute('SELECT * FROM Products')

# print(rows.fetchone())
while True:
    records = rows.fetchone()
    if records == None:
        break
    else:
        print(records)
