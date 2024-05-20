# Yelp-Database-Management

## Introduction

This project, Yelp Database Management, is a Python-based application that interacts with a SQL Server yelp database. It provides a graphical user interface for users to log in, search for businesses and users, make friends with other users, and review businesses.

## Requirements

- Python 3.8 or higher
- pyodbc library
- tkinter library
- A SQL Server database with the necessary tables and data

## Installation

1. Clone the repository or download the zip file and extract it.
2. Navigate to the project directory.
3. Install the required Python libraries using pip:

```python
pip install pyodbc
pip install tkinter
```

## Usage

1. Run the `main.py` file in your Python environment:

```python
python main.py
```

2. The application will start and display a login window. Enter your user ID to log in.

### Login

- The login function allows the user to log in to the interface to have access to all other functionalities. The user must be remembered by the system for further operations in the same session.
- If the user ID is invalid, an appropriate message will be shown to the user.

### Search Business

- This function allows the user to search for businesses that satisfy certain criteria.
- A user should be able to set the following filters as their search criteria: minimum number of stars, city, and name (or part of the name). The search is not case-sensitive.
- After the search is complete, a list of search results will be shown to the user. The list includes the following information for each business: id, name, address, city, and number of stars. The results are ordered according to the chosen attribute.
- If the search result is empty, an appropriate message will be shown to the user.

### Search Users

- This function allows the user to search for users that satisfy certain criteria.
- A user should be able to set the following filters as their search criteria: name (or a part of the name), minimum review count, minimum average stars. The search is not case-sensitive.
- After the search is complete, a list of search results will be shown to the user. The list includes the following information for each user: id, name, review count, useful, funny, cool, average stars, and the date when the user was registered at Yelp. The results are ordered by name.
- If the search result is empty, an appropriate message will be shown to the user.

### Make Friend

- A user must be able to select another user from the results of the function Search Users and create a friendship. This can be done by entering the user’s ID.
- The friendship is recorded in the Friendship table.

### Review Business

- A user should be able to review a business.
- To make a review, a user must enter the business’s ID.
- The user must provide the number of stars (integer between 1 and 5).
- The review is recorded in the Review table. The ID of the logged user and the current date are considered.
- The program updates the number of stars and the count of reviews for the reviewed business.
