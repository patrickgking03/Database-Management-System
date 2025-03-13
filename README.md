# Database Management System

## Overview
This is a simple CRUD-based database management system built with Flask and SQLite. It allows users to manage employee records, including adding, updating, and deleting employees.

## Features
- View all employees in the database
- Add new employees with name, position, and salary
- Update existing employee details
- Delete employees from the database
- Simple and responsive UI using Bootstrap
- SQLite database for lightweight storage

## Installation & Setup
### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/Database-Management-System.git
cd Database-Management-System
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install Flask Flask-SQLAlchemy
pip freeze > requirements.txt
```

### 4. Run the Application
```bash
python app.py
```
Then, open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

### 5. Close the Application
To stop the Flask server, press `CTRL+C` in the terminal.

## File Structure
```
Database-Management-System/
├── app.py                # Main Flask application
├── db.db                 # SQLite database (auto-created)
├── templates/            # HTML templates for UI
│   ├── base.html
│   ├── home.html
│   ├── view_employees.html
│   ├── add_employee.html
│   └── update_employee.html
├── .gitignore            # Git ignore file
└── requirements.txt      # Python dependencies
```

## Commit & Push Changes
### 1. Add, Commit, and Push to GitHub
```bash
git add .
git commit -m "Initial commit with working Flask CRUD app"
git push origin main
```

## License
This project is licensed under the MIT License.

## Author
**Patrick King** - 2025