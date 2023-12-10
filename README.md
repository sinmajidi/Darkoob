# Darkoob Framework

Welcome to Darkoob Framework by AFRA IOT! 🚀

Darkoob is a Python backend framework designed to simplify web development 
and provide developers with powerful tools for building robust web applications. 
It allows you to define routes easily and handle different HTTP methods such as GET, 
POST, PUT, and DELETE.

## Features

- Simple and intuitive routing system
- Support for multiple HTTP methods: GET, POST, PUT, DELETE
- Template rendering using Jinja2
- Basic error handling for 404 and 405 responses

## Getting Started

    
### Install the required dependencies listed in `requirements.txt` using pip:
      pip install -r requirements.txt

### Define your routes in `routes.py` and implement corresponding view functions in `views.py`.

### Run your Darkoob server using the following command:
    
    python routes.py

Visit http://127.0.0.1:8080 in your web browser to see your Darkoob application in action!

Project Structure
### Define your application routes and start the server.
- `routes.py`

### Implement your route functions for handling different paths and HTTP methods.
- `views.py`

### Core framework file containing the server logic and request handling.
- `Darkoob.py`

### Directory to store your HTML templates.
- `templates/`

DarkoobSQLITE
Integrate DarkoobSQLITE for easy interaction with SQLite databases in Darkoob.

### Example usage of DarkoobSQLITE
from Darkoob_sqlite import DarkoobSQLIT

### Initialize DarkoobSQLITE
orm = DarkoobSQLIT()

### Create a table named 'users'
orm.create_table(table_name='users', id='INTEGER PRIMARY KEY', name='TEXT', age='INTEGER')

### Insert data into the 'users' table
orm.insert('users', name='John', age=25)

### Select data from the 'users' table where name is 'John'
print(orm.select('users', name='John'))

### Update data in the 'users' table where name is 'John'
orm.update('users', {'age': 30}, name='John')

### Delete data from the 'users' table where name is 'John'
orm.delete('users', name='John')

### Close the database connection
orm.close_connection()


Contributing
Darkoob is an open-source project, and we welcome contributions from the community. If you have any suggestions, bug reports, or feature requests, please create an issue or submit a pull request.

Happy coding! 😊

For more information, visit https://afraiot.org.
