from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

questions = [
    {
        "question": "Aren't you supposed to be reviewing resumes right now?",
        "options": ["Yes", "No", "Maybe"],
        "answer": "Yes"
    },
    {
        "question": "Are you sure you want to play this game?",
        "options": ["Yes", "No"],
        "answer": "Yes"
    },
    {
        "question": "Are you sure you have some free time?",
        "options": ["Yes", "No"],
        "answer": "Yes"
    }
]

final_redirect_url = "https://dinosaur-game.io/"  # Change this to your desired final web address

@app.route("/", methods=["GET", "POST"])
def game():
    message = ""
    question_index = int(request.form.get("question_index", 0))

    if request.method == "POST":
        user_answer = request.form.get("answer")

        if user_answer == questions[question_index]["answer"]:
            message = "Correct!"
            question_index += 1  # Move to the next question

            if question_index >= len(questions):  # If it was the last question, redirect
                return redirect(final_redirect_url)

        else:
            message = "Wrong! The correct answer was: " + questions[question_index]["answer"]

        return render_template("index.html", message=message, question=questions[question_index]["question"], 
                               options=questions[question_index]["options"], question_index=question_index)

    return render_template("index.html", question=questions[0]["question"], options=questions[0]["options"], question_index=0)

@app.route("/")
def home():
    return "Hello, Render!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render provides a PORT environment variable
    app.run(debug=False, host="0.0.0.0", port=port)
