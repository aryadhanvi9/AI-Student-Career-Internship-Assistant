from flask import Flask, render_template, request
from career_recommender import recommend_career
from internship_recommender import recommend_internship
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
    career = ""
    internship = ""
    if request.method == "POST":
        skills = request.form["skills"]
        career = recommend_career(skills)
        internship = recommend_internship(skills)
    return render_template(
        "index.html",
        career=career,
     internship=internship
    )
if __name__ == "__main__":
    app.run(debug=True)
