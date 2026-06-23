from career_recommender import recommend_career
from internship_recommender import recommend_internship

skills = input("Enter your skills (comma separated): ")

career = recommend_career(skills)
internship = recommend_internship(skills)

print("Recommended Career:", career)
print("Recommended Internship:", internship)
