from flask import Flask
from flask import request, render_template
import cohereimplement

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template("index.html", output_content="Output: <br/><br/>{}".format("No Output yet."))


@app.route('/generate', methods=["POST"])
def generate():
    prompt = request.form["prompt"]
    keywords_raw = request.form["keywords"]
    if prompt.replace(" ", "") == "":
        return render_template("index.html", prompt_value="", keywords_value=keywords_raw,
                               output_content="Error: Please input a valid prompt.")
    elif keywords_raw.replace(" ", "") == "":
        return render_template("index.html", prompt_value=prompt, keywords_value="",
                               output_content="Error: Please input valid keyword(s).")
    keywords = keywords_raw.replace(" ", "").split(",")
    print(prompt, keywords)

    output = cohereimplement.creating_string(prompt.replace(" ", ""));
    # TODO: Generate Output

    return render_template("index.html", prompt_value=prompt, keywords_value=keywords_raw,
                           output_content="Output: <br/><br/>{}".format(output))


if __name__ == '__main__':
    app.run(debug=True)
