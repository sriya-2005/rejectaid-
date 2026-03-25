from Flask import Flask, render_template, request
import json

app = Flask(__name__)

# Load scheme rules
with open("schemes.json", "r") as file:
    schemes = json.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    age = int(request.form["age"])
    income = int(request.form["income"])
    category = request.form["category"]

    scheme = schemes["Scholarship_A"]
    reasons = []

    if age < scheme["min_age"] or age > scheme["max_age"]:
        reasons.append("Age is not within the allowed range.")

    if income > scheme["income_limit"]:
        reasons.append("Income exceeds the allowed limit.")

    if category not in scheme["allowed_categories"]:
        reasons.append("Category is not eligible.")

    return render_template("result.html", reasons=reasons)

if __name__ == "__main__":
    app.run(debug=True)