def recommend_career(skills):
    if "python" in skills.lower():
        return "Software Developer"
    elif "design" in skills.lower():
        return "UI/UX Designer"
    else:
        return "General Tech Career"
