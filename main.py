from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)
df = pd.read_csv("data/dictionary.csv")

@app.route("/")
def home():
    return render_template("dictionary.html")


@app.route("/api/v1/<word>")
def api(word):
    definition = df.loc[df['word'] == word]['definition'].squeeze()
    if isinstance(definition, str):
        status = 'OK'
    else:
        definition = "word not found"
        status = "Word not found"


    return {
            "definition": definition,
            "word": word}



app.run(debug=True, port=5001)