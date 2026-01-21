# INTERNSHIP_TASK_BACKEND-PROJECT-1
# Flask Regex Tester Web Application
## Project Overview

This project is a lightweight web application built using Python and Flask that replicates the core functionality of regex101.com. It allows users to input a test string and a regular expression pattern, and dynamically displays all matching results.

The goal of this project is to strengthen hands-on understanding of regular expressions, form handling, backend processing, and web application development.

## Features

✔️ Accepts user input for test string and regex pattern

✔️ Displays all matched substrings instantly

✔️ Handles invalid regex patterns gracefully

✔️ Clean and simple UI

✔️ Beginner-friendly codebase

✔️ Built entirely in Python using Flask

## Technologies Used

Python

Flask

Regular Expressions (re module)

HTML (inline templates)

Jupyter Notebook

## Project Structure
flask-regex-tester/
│
├── notebook.ipynb     # Jupyter Notebook with Flask application
├── README.md          # Project documentation

## How to Run the Project (Jupyter Notebook)
Step 1: Install Flask

Run in a notebook cell:

!pip install flask

Step 2: Paste Application Code
from flask import Flask, request
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def regex_tester():
    matches = []
    error = None
    test_string = ""
    pattern = ""

    if request.method == "POST":
        test_string = request.form.get("test_string")
        pattern = request.form.get("pattern")

        try:
            matches = re.findall(pattern, test_string)
        except re.error as e:
            error = str(e)

    return f"""
    <h2> Regex Matcher App</h2>

    <form method="post">
        <label><b>Test String:</b></label><br>
        <textarea name="test_string" rows="4" cols="60">{test_string}</textarea><br><br>

        <label><b>Regular Expression:</b></label><br>
        <input type="text" name="pattern" value="{pattern}" size="50"><br><br>

        <button type="submit">Submit</button>
    </form>

    <hr>

    <h3> Matches:</h3>
    <p>{matches if matches else "No matches found"}</p>

    <h3 style="color:red;">{error if error else ""}</h3>
    """

if __name__ == "__main__":
    app.run(port=5001)

Step 3: Start Server
app.run(port=5001)


Open browser:

http://127.0.0.1:5001/

## Sample Test Case

Test String:

Contact: test@gmail.com, admin@company.org


Regex Pattern:

[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}


Output:

['test@gmail.com', 'admin@company.org']

## Future Enhancements

Add syntax highlighting

Display match count

Color-highlight matched text

Save regex history

Deploy to cloud

# Author

Bathula Venu Gopal
Data Science Intern – Innomatics Research Labs
Batch 419
