from flask import Flask, jsonify, request, render_template
from fitness_logic import calculate_bmi, membership_status, calculate_bmi_value

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    bmi = None
    category = None

    if request.method == "POST":
        weight = float(request.form["weight"])
        height = float(request.form["height"])

        try:
            bmi_value = calculate_bmi_value(weight, height)
            bmi = round(bmi_value, 2)
            category = calculate_bmi(weight,height)
        except ValueError as e:
            bmi = str(e)

    return render_template("index.html", bmi=bmi, category=category)


@app.route("/bmi")
def bmi():
    weight = float(request.args.get("weight"))
    height = float(request.args.get("height"))

    result = calculate_bmi(weight, height)

    return jsonify({
        "weight": weight,
        "height": height,
        "category": result
    })


@app.route("/membership")
def membership():
    end_date = request.args.get("end")

    status = membership_status(end_date)

    return jsonify({
        "membership_end": end_date,
        "status": status
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)