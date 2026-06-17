def recommend_internship(skills):
    if "Python" in skills:
        return "AI/ML Internship"
    elif "Web Development" in skills:
        return "Frontend Developer Internship"
    else:
        return "General Internship Opportunities"
