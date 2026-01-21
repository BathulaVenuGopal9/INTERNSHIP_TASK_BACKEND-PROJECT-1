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
    <h2>🔍 Regex Matcher App</h2>

    <form method="post">
        <label><b>Test String:</b></label><br>
        <textarea name="test_string" rows="4" cols="60">{test_string}</textarea><br><br>

        <label><b>Regular Expression:</b></label><br>
        <input type="text" name="pattern" value="{pattern}" size="50"><br><br>

        <button type="submit">Submit</button>
    </form>

    <hr>

    <h3>✅ Matches:</h3>
    <p>{matches if matches else "No matches found"}</p>

    <h3 style="color:red;">{error if error else ""}</h3>
    """

if __name__ == "__main__":
    app.run(port=5001)
