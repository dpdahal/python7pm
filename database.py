import mysql.connector

# database connection
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='python7pm'
)

obj = connection.cursor()
# database query
db_query = "CREATE DATABASE IF NOT EXISTS python7pm"
obj.execute(db_query)

# table query
tableQuery = "CREATE TABLE IF NOT EXISTS users(id int  AUTO_INCREMENT PRIMARY KEY,name varchar(100),email varchar(100))"
obj.execute(tableQuery)

# insert query

insertQuery = "INSERT INTO users(name,email)VALUES('ram','ram@gmail.com')"
obj.execute(insertQuery)
connection.commit()

# select query

selectQuery = "SELECT * FROM users"

obj.execute(selectQuery)

print(obj.fetchmany(2))

# update query


# delete query
