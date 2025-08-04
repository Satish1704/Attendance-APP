from flask import Flask, render_template, request, redirect, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = "secretkey"

members = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
duties = ["Dustbin Clearing", "Water Taking"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = {duty: [] for duty in duties}

        for duty in duties:
            selected = request.form.getlist(duty)
            data[duty] = selected

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("room_duty_log.txt", "a") as f:
            f.write(f"--- Duties at {now} ---\n")
            for duty, assigned_members in data.items():
                f.write(f"{duty}:\n")
                for member in assigned_members:
                    f.write(f"  - {member}\n")
            f.write("\n")

        flash("Duties recorded successfully!", "success")
        return redirect("/")

    return render_template("duty_form.html", members=members, duties=duties)