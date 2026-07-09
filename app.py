from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    answer = ""

    if request.method == "POST":
        question = request.form["question"].lower()

        if "python" in question:
            answer = "Python is an easy-to-learn programming language widely used for AI, web development, automation, and data science."

        elif "machine learning" in question:
            answer = "Machine Learning is a branch of Artificial Intelligence that enables computers to learn patterns from data and make predictions."

        elif "ai" in question or "artificial intelligence" in question:
            answer = "Artificial Intelligence (AI) allows machines to perform tasks that normally require human intelligence, such as learning, reasoning, and problem-solving."

        elif "sdg" in question:
            answer = "SDG 4 focuses on ensuring inclusive and equitable quality education and promoting lifelong learning opportunities for everyone."

        elif "hello" in question or "hi" in question:
            answer = "Hello! 👋 Welcome to StudyMate AI. How can I help you today?"

        else:
            answer = "Thank you for your question. Study regularly, practice daily, and keep learning. 😊"

    return render_template("chatbot.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)