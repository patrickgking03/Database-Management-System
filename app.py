from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configure the SQLite database
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, 'db.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# -------------------------
# MODELS
# -------------------------
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Employee {self.name}>"

# -------------------------
# ROUTES
# -------------------------
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/employees')
def view_employees():
    employees = Employee.query.all()
    return render_template('view_employees.html', employees=employees)

@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        position = request.form['position']
        salary = request.form['salary']

        new_employee = Employee(name=name, position=position, salary=float(salary))
        db.session.add(new_employee)
        db.session.commit()
        return redirect(url_for('view_employees'))
    return render_template('add_employee.html')

@app.route('/update/<int:employee_id>', methods=['GET', 'POST'])
def update_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    if request.method == 'POST':
        employee.name = request.form['name']
        employee.position = request.form['position']
        employee.salary = float(request.form['salary'])
        db.session.commit()
        return redirect(url_for('view_employees'))
    return render_template('update_employee.html', employee=employee)

@app.route('/delete/<int:employee_id>')
def delete_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for('view_employees'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
