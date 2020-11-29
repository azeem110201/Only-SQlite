from flask import Flask,render_template,request
import sqlite3
from employee_class import Employee


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_method():

    first_name = str(request.form['first_name'])
    last_name = str(request.form['last_name'])
    age = float(request.form['age'])

    conn = sqlite3.connect('employee.db')
    c = conn.cursor()


#c.execute("""CREATE TABLE employees  (
#            first text,
#            last text,
#            pay integer
#            )""")


    def insert_emp(emp):
        with conn:
            c.execute("INSERT INTO employees  VALUES (:first, :last, :pay)", {
                  'first': emp.first, 'last': emp.last, 'pay': emp.pay})


    #def get_emps_by_name(lastname):
    #    c.execute("SELECT * FROM employees  WHERE last=:last", {'last': lastname})
    #    return c.fetchall()


    #def update_age(emp, pay):
    #    with conn:
    #        c.execute("""UPDATE employees  SET pay = :pay
    #                WHERE first = :first AND last = :last""",
    #              {'first': emp.first, 'last': emp.last, 'pay': pay})


    #def remove_emp(emp):
    #    with conn:
    #        c.execute("DELETE from employees  WHERE first = :first AND last = :last",
    #              {'first': emp.first, 'last': emp.last})

    emp_1 = Employee(first_name, last_name, age)
    insert_emp(emp_1)

    conn.close()

    return render_template('results.html',first_name=first_name,last_name=last_name,age=age)




if __name__ == '__main__':
    app.run(debug=True)    
