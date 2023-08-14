from flask import Flask, render_template, request, redirect, url_for, flash
from textSummarization.pipeline.predict import PredictionPipeline
import os

app = Flask(__name__)
app.secret_key = 'some_secret_key'

@app.route("/", methods=['GET'])
def index():
    return redirect(url_for('docs'))

@app.route("/docs", methods=['GET', 'POST'])
def docs():
    text = ""
    summary = ""
    if request.method == 'POST':
        text = request.form['text']
        try:
            obj = PredictionPipeline()
            raw_summary = obj.predict(text)
            summary = format_conversation(raw_summary)
        except Exception as e:
            flash(f"Error Occurred! {str(e)}")
    return render_template('docs.html', summary=summary, original_text=text)

@app.route("/train", methods=['GET'])
def training():
    try:
        os.system("python main.py")
        flash("Training successful !!")
        return redirect(url_for('docs'))
    except Exception as e:
        flash(f"Error Occurred! {str(e)}")
        return redirect(url_for('docs'))

def format_conversation(output: str) -> str:
    segments = output.split("<n>")
    formatted_segments = []
    for segment in segments:
        segment = segment.strip()
        if segment:
            formatted_segments.append(segment[0].upper() + segment[1:])
    return "\n".join(formatted_segments)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2080, debug=True)
