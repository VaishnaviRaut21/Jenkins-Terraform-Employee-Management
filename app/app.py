from flask import Flask, render_template, request, redirect, url_for

from database import (
    initialize_database,
    get_all_employees,
    add_employee,
    delete_employee
)


app = Flask(__name__)


initialize_database()


@app.route("/")
def index():
    employees = get_all_employees()

    return render_template(
        "index.html",
        employees=employees
    )


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":

        name = request.form["name"]
        department = request.form["department"]
        email = request.form["email"]
        salary = request.form["salary"]

        add_employee(
            name,
            department,
            email,
            salary
        )

        return redirect(url_for("index"))

    return render_template("add_employee.html")


@app.route("/delete/<int:employee_id>")
def delete(employee_id):

    delete_employee(employee_id)

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)