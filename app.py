from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

employees = [
    {
        "id": 1,
        "name": "Aniket",
        "role": "DevOps Engineer",
        "department": "IT"
    },
    {
        "id": 2,
        "name": "Rahul",
        "role": "Python Developer",
        "department": "Development"
    },
    {
        "id": 3,
        "name": "Priya",
        "role": "QA Engineer",
        "department": "Testing"
    }
]


@app.route("/")
def home():
    return render_template("index.html", employees=employees)


@app.route("/add", methods=["GET", "POST"])
def add_employee():

    if request.method == "POST":

        name = request.form["name"]
        role = request.form["role"]
        department = request.form["department"]

        new_employee = {
            "id": len(employees) + 1,
            "name": name,
            "role": role,
            "department": department
        }

        employees.append(new_employee)

        return redirect(url_for("home"))

    return render_template("add_employee.html")


@app.route("/health")
def health():
    return "Application is healthy"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)