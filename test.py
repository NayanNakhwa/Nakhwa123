from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Resume Portfolio</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f4f4f4; }
        .container { background: #fff; padding: 30px; border-radius: 8px; max-width: 700px; margin: auto; }
        h1 { color: #333; }
        h2 { color: #555; }
        ul { list-style-type: square; }
    </style>
</head>
<body>
    <div class="container">
        <h1>{{ name }}</h1>
        <p><strong>Email:</strong> {{ email }}</p>
        <p><strong>Phone:</strong> {{ phone }}</p>
        <h2>Summary</h2>
        <p>{{ summary }}</p>
        <h2>Skills</h2>
        <ul>
            {% for skill in skills %}
            <li>{{ skill }}</li>
            {% endfor %}
        </ul>
        <h2>Experience</h2>
        <ul>
            {% for job in experience %}
            <li>
                <strong>{{ job['role'] }}</strong> at {{ job['company'] }} ({{ job['years'] }})<br>
                {{ job['desc'] }}
            </li>
            {% endfor %}
        </ul>
        <h2>Education</h2>
        <ul>
            {% for edu in education %}
            <li>
                <strong>{{ edu['degree'] }}</strong> - {{ edu['school'] }} ({{ edu['year'] }})
            </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
"""

@app.route("/")
def resume():
    data = {
        "name": "John Doe",
        "email": "john.doe@email.com",
        "phone": "+1234567890",
        "summary": "Experienced software developer with a passion for building web applications.",
        "skills": ["Python", "Flask", "JavaScript", "HTML/CSS", "SQL"],
        "experience": [
            {"role": "Software Engineer", "company": "TechCorp", "years": "2021-2024", "desc": "Developed web applications using Flask and React."},
            {"role": "Intern", "company": "WebStart", "years": "2020-2021", "desc": "Assisted in building REST APIs and frontend interfaces."}
        ],
        "education": [
            {"degree": "B.Sc. in Computer Science", "school": "ABC University", "year": "2020"}
        ]
    }
    return render_template_string(HTML, **data)

if __name__ == "__main__":
    app.run(debug=True)