# DSA MCQ Quiz CLI App

A command-line quiz application for Data Structures and Algorithms (DSA) multiple-choice questions, with user authentication and MySQL database integration.

## Features

- User signup and login with secure password hashing
- Multiple-choice DSA quiz questions
- Tracks user answers and scores
- Stores user data and quiz results in MySQL

## Requirements

- Python 3.8+
- MySQL server
- [mysql-connector-python](https://pypi.org/project/mysql-connector-python/) 

## Installation

Install dependencies:
```sh
pip install -r requirements.txt
```

## Setup

### Database Setup

Create the database and tables by running the SQL script:
```sh
mysql -u <username> -p < questions.sql
```

Update the database credentials in `config.py`.

### Run the Application

```sh
python main.py
```

## File Structure

- `main.py`: Entry point, CLI menu
- `auth.py`: User signup and login logic
- `quiz.py`: Quiz logic and user answer tracking
- `db.py`: Database connection helper
- `config.py`: Database configuration
- `questions.sql`: SQL schema for users, questions, and answers

## Usage

Start the app:
```sh
python main.py
```
- Choose to Signup or Login.
- After login, take the quiz and view your score.

## License

MIT License

