from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('base.html')

@app.route('/workout', methods=["GET", "POST"])
def workout_plan():
    if request.method == "POST":
        fitness_goal = request.form.get("fitnessGoal")
        fitness_level = request.form.get("fitnessLevel")
        workout_type = request.form.getlist("workoutType")
        workout_time = request.form.get("exerciseHours")
        data = [fitness_goal, fitness_level, workout_type, workout_time]
        return render_template('workout_plan.html', exercises = data)

if __name__ == '__main__':
    app.run(debug=True)
